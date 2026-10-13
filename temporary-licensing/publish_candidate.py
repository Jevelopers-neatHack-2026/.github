"""Publish one prevalidated licensing tree on a new branch; never merge or change settings."""
import copy, hashlib, importlib.util, json, os, re, subprocess, sys, tempfile
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
ORG='Jevelopers-neatHack-2026'
SOURCE='22734cb3eaf234f03bc3ad6ccb2a4d86baf6d546'
EXPECTED={
'.github':'79da830bfa8232666a6f68f9581a2400ca9bda2f',
'Jevelopers-GetTicketStub.com-Submission':'f48e8d8050c7079d8c78e84530198d8134a44ca5',
'brand-kit':'874f5ea90127dd30db6448fad84021fcfd68c9f3',
'cost-intelligence':'9e2a001772cf8d16b5161571c16ae09f3225d147',
'creative-engine':'0dd66fd80f100d2835bbb84d32c7a0fcd572e0ad',
'event-intelligence':'b0072f164e0c918dfbc80a85fc7ea1da18cb28f5',
'fulfillment-connectors':'2a044a5083911da9e1af6b50067000147720e479',
'getticketstub.com':'1c361370f84566ab790a93af6eb93e0578cc1fb8',
'integration-evals':'b8c35ef833b91be50669a73df448ff23b0acd3fd',
'landing-page-repo':'0add049ed669b8f1a67da9d8c6f3b3892ff5d0b9',
'marketing-material':'3cc9fd88f00baa776a849affc1c737f1908915c6',
'print-production':'09c913d56ce1c635515853150b491ddfb05d0ec2',
'shared-contracts':'f4a6357f8d1fdfeb660d212515089dc9db2f9ae0',
'team-dashboard':'1aa964caea464aaea378458e66ebc2ff6e33a3da'}
TOKEN=os.environ['GH_TOKEN'];FULL=os.environ['GITHUB_REPOSITORY']
if not FULL.startswith(ORG+'/') or FULL.split('/')[1] not in EXPECTED:raise SystemExit('Unapproved repository')
NAME=FULL.split('/')[1];ROOT=Path.cwd().resolve();BRANCH='docs/jevelopers-license-copyright-20261013'
def raw(path):
    url=f'https://raw.githubusercontent.com/{ORG}/.github/{SOURCE}/temporary-licensing/{path}'
    with urlopen(Request(url,headers={'User-Agent':'Jevelopers-license-preparation'}),timeout=30) as r:
        if r.url!=url:raise ValueError('Unexpected source redirect')
        data=r.read(200001)
    if len(data)>200000:raise ValueError('Source size')
    return data
def api(path='',method='GET',value=None):
    url=f'https://api.github.com/repos/{FULL}'+path
    headers={'User-Agent':'Jevelopers-license-preparation','Accept':'application/vnd.github+json','Authorization':'Bearer '+TOKEN}
    data=None if value is None else json.dumps(value,ensure_ascii=False).encode()
    if data is not None:headers['Content-Type']='application/json'
    with urlopen(Request(url,data=data,headers=headers,method=method),timeout=45) as r:
        return json.load(r)
def command(args):
    p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120)
    if p.returncode:
        sys.stderr.write(p.stderr.decode(errors='replace')[:12000]);raise RuntimeError('Check failed: '+args[0])
    return p.stdout.decode().strip()
configs={}
for f in ['core.json','runtime.json','sites.json','services.json']:
    configs.update(json.loads(raw(f))['repositories'])
cfg=configs[NAME]
assert command(['git','rev-parse','HEAD'])==cfg['base_sha'],'Wrong checkout'
assert command(['git','rev-parse','HEAD^{tree}'])==cfg['base_tree'],'Wrong base tree'
assert command(['git','status','--porcelain'])=='','Dirty checkout'
info=api();assert info['full_name']==FULL and not info['archived']
base_branch=info['default_branch']
assert api('/git/ref/heads/'+base_branch)['object']['sha']==cfg['base_sha'],'Default branch advanced; re-audit required'
try:
    api('/git/ref/heads/'+BRANCH)
except HTTPError as e:
    if e.code!=404:raise
else:raise ValueError('Candidate branch already exists; do not overwrite')
with tempfile.TemporaryDirectory(prefix='licensing-source-') as tmp:
    p=Path(tmp)/'prepare.py';p.write_bytes(raw('prepare.py'))
    spec=importlib.util.spec_from_file_location('licensing_prepare',p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    changes=mod.prepare(ROOT,NAME,cfg)
    assert set(changes)<=set(cfg['allowed_paths'])
    assert changes['LICENSE']==mod.MIT.encode()
    for path,data in changes.items():
        if not data.endswith(b'\n'):raise ValueError('Missing final newline: '+path)
        if path.endswith('.json'):json.loads(data)
        target=ROOT/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    command(['git','add','-f','--',*changes])
    command(['git','diff','--cached','--check'])
    actual=command(['git','write-tree'])
    assert actual==EXPECTED[NAME],f'Prepared tree mismatch: {actual}'
    new_md=[p for p in changes if p.endswith('.md') and p!='README.md' and not p.endswith('/NOTICE.md')]
    if new_md:command(['npx','--yes','markdownlint-cli@0.45.0',*new_md,'--disable','MD013'])
    tests=['canonical MIT equality','pinned base and full candidate tree equality','git diff --cached --check','JSON parsing','markdownlint-cli 0.45.0 new documents (MD013 disabled)']
    diff=command(['git','diff','--cached','--full-index','--no-renames'])+'\n'
    assert api('/git/ref/heads/'+base_branch)['object']['sha']==cfg['base_sha'],'Base advanced before publication'
    entries=[];file_results=[]
    for path,data in sorted(changes.items()):
        mode=command(['git','ls-files','--stage','--',path]).split()[0]
        entries.append({'path':path,'mode':mode,'type':'blob','content':data.decode()})
        file_results.append({'path':path,'blob_sha':mod.blob(data),'sha256':mod.digest(data),'bytes':len(data)})
    tree=api('/git/trees','POST',{'base_tree':cfg['base_tree'],'tree':entries})
    assert tree['sha']==EXPECTED[NAME],'GitHub tree differs'
    commit=api('/git/commits','POST',{'message':'docs: add Jevelopers license and copyright attribution\n\nPreserve separately owned notices and unresolved asset rights.\nNo runtime, dependency version, deployment or approval changes.','tree':tree['sha'],'parents':[cfg['base_sha']]})
    ref=api('/git/refs','POST',{'ref':'refs/heads/'+BRANCH,'sha':commit['sha']})
    assert ref['object']['sha']==commit['sha']
    result={'repository':FULL,'base_sha':cfg['base_sha'],'commit_sha':commit['sha'],'tree_sha':tree['sha'],'branch':BRANCH,'files':file_results,'executed_checks':tests,'not_run':['full application build and runtime test suites','independent review','GitHub default-branch license detection (PR not merged)'],'workflow_run':f'https://github.com/{FULL}/actions/runs/'+os.environ['GITHUB_RUN_ID'],'merged':False}
    out=Path(os.environ['RUNNER_TEMP'])/'licensing-result';out.mkdir(exist_ok=True)
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n');(out/'licensing.patch').write_text(diff)
    print(json.dumps(result,indent=2))
