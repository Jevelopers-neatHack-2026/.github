"""Prepare a bounded, repository-specific licensing change; never publish or merge.

Inputs are an explicitly reviewed JSON configuration and a pinned source checkout.
Only allowlisted license, metadata, and attribution paths may change. Network reads
are optional, restricted to checksum-pinned upstream license texts on GitHub.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ORG = 'Jevelopers-neatHack-2026'
MIT = '''MIT License

Copyright (c) 2026 Jevelopers contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
ENTIRE_REF = '22e6f50f56b9e6d9fd740c5c54c3a42b94d3a282'
ROSTER = f'https://github.com/{ORG}/.github/blob/c9b08a1c2a7e3e1e0f49051fce0be0603d3e138c/profile/README.md'
PEOPLE = '''| Name | Team role | GitHub | LinkedIn | X / Twitter | Website | Email | Project-level contribution evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Timothy Wayne Gregg | Team Captain | [CompleteDotTech](https://github.com/CompleteDotTech) | [Profile](https://www.linkedin.com/in/timothy-gregg/) | [CompleteTechLLC](https://x.com/CompleteTechLLC) | Not publicly listed | Not publicly listed | Team coordination; agent-harness [runtime](https://github.com/Jevelopers-neatHack-2026/agent-harness/commit/b249c25775eabe72b8b5b2eae4fce9bcb841d98a) and [documentation](https://github.com/Jevelopers-neatHack-2026/agent-harness/commit/dfa6be738beb8f48ebcccbcd16766721567f7c0e) history. |
| Lars van der Zande | Team member | [lmvdz](https://github.com/lmvdz) | [Profile](https://www.linkedin.com/in/lmvanderzande/) | [Lmvdzande](https://x.com/Lmvdzande) | Not publicly listed | Not publicly listed | Brand, editions and studio design credited in the [organization roster][roster]. |
| Zachary Wright | Team member | [zwright8](https://github.com/zwright8) | [Profile](https://www.linkedin.com/in/zachary-d-wright/) | [ZacharyDWright](https://x.com/ZacharyDWright) | Not publicly listed | Not publicly listed | Confirmed hackathon team membership; no more specific repository contribution is asserted. |
| Crystal Aguilar | Team member | [lajefahemp-collab](https://github.com/lajefahemp-collab) | [Profile](https://www.linkedin.com/in/crystal-aguilar-la-jefa-hemp-llc-721514b8/) | [lajefahemp](https://x.com/lajefahemp) | Not publicly listed | Not publicly listed | TicketStub landing-page [artifact and documentation history](https://github.com/Jevelopers-neatHack-2026/landing-page-repo/commit/09e1cfc2e5a15e1f639559307309826315e79a8a). |
'''

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def valid_path(path: str) -> bool:
    p = PurePosixPath(path)
    return bool(path) and not p.is_absolute() and '\\' not in path and all(x not in {'.','..',''} for x in p.parts)

def dump(value: object, indent: str | int = 2) -> str:
    return json.dumps(value, ensure_ascii=False, indent=indent) + '\n'

def json_span(text: str, path: tuple[str, ...]) -> tuple[int, int]:
    """Locate an exact object member without reformatting unrelated JSON."""
    decoder = json.JSONDecoder()
    start = len(text) - len(text.lstrip())
    end = decoder.raw_decode(text, start)[1]
    for wanted in path:
        if text[start] != '{':
            raise ValueError('Expected JSON object')
        pos = start + 1
        while True:
            while text[pos].isspace() or text[pos] == ',':
                pos += 1
            if text[pos] == '}':
                raise KeyError(wanted)
            key, pos = decoder.raw_decode(text, pos)
            while text[pos].isspace(): pos += 1
            if text[pos] != ':': raise ValueError('Expected colon')
            pos += 1
            while text[pos].isspace(): pos += 1
            value_start = pos
            _, pos = decoder.raw_decode(text, pos)
            if key == wanted:
                start, end = value_start, pos
                break
    return start, end

def set_license(text: str, path: tuple[str,...] = ()) -> str:
    before = json.loads(text)
    target = before
    for key in path: target = target[key]
    if 'license' in target:
        if target['license'] != 'MIT':
            raise ValueError('Existing license requires a separate owner decision')
        return text
    start, _ = json_span(text, path)
    ws = re.match(r'\s*', text[start + 1:]).group()
    if not ws or '\n' not in ws:
        raise ValueError('Expected multiline JSON metadata')
    at = start + 1 + len(ws)
    candidate = text[:at] + '"license": "MIT",' + ws + text[at:]
    actual = json.loads(candidate)
    check = actual
    for key in path: check = check[key]
    del check['license']
    if actual != before: raise ValueError('Unrelated manifest change')
    return candidate

def add_package_files(text: str, paths: list[str]) -> str:
    obj = json.loads(text)
    if not isinstance(obj.get('files'), list): return text
    added = [p for p in paths if p not in obj['files']]
    if not added: return text
    start, end = json_span(text, ('files',))
    original = text[start:end]
    if '\n' in original:
        indent = re.search(r'\n([ \t]+)"', original).group(1)
        closing = re.search(r'\n([ \t]*)\]$', original).group(1)
        replacement = '[\n' + ',\n'.join(indent + json.dumps(p) for p in obj['files'] + added) + '\n' + closing + ']'
    else:
        replacement = json.dumps(obj['files'] + added, ensure_ascii=False)
    return text[:start] + replacement + text[end:]

def read_pinned(item: dict, cache: Path | None) -> bytes:
    url = item['url']
    parsed = urlparse(url)
    if parsed.scheme != 'https' or parsed.hostname != 'raw.githubusercontent.com' or not re.search(r'/[0-9a-f]{40}/', parsed.path):
        raise ValueError('License source must be an immutable GitHub raw URL')
    local = cache / item['local_path'] if cache else None
    if local and local.is_file(): data = local.read_bytes()
    else:
        with urlopen(Request(url, headers={'User-Agent':'Jevelopers-licensing'}), timeout=30) as response:
            if response.url != url: raise ValueError('Unexpected license redirect')
            data = response.read(250001)
    if len(data) > 250000 or digest(data) != item['sha256']:
        raise ValueError('Upstream license checksum mismatch')
    data.decode('utf-8')
    return data

def copyright_text(name: str, cfg: dict, has_notices: bool) -> str:
    url = f'https://github.com/{ORG}/{name}'
    scope_rows = '\n'.join(f'| {path} | {meaning} |' for path, meaning in cfg['scope'])
    evidence = '\n'.join('- ' + line for line in cfg['audit'])
    third = ('See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the component-specific notices, source references and local paths.' if has_notices else 'No additional copied third-party software requiring a new notice was identified in the reviewed first-party text scope. Existing asset permissions and separately sourced material remain outside this grant.')
    return f'''# Copyright and Jevelopers team attribution

**Repository:** [{ORG}/{name}]({url})

**Project:** TicketStub — Jevelopers — neatHack 2026

**Licensing review:** October 13, 2026

## Copyright statement

Copyright (c) 2026 Jevelopers contributors.

The [MIT License](LICENSE), SPDX identifier `MIT`, applies to {cfg['grant']}.
The material identified below is not relicensed by the project notice.

“Jevelopers contributors” refers collectively to the respective rights holders
in their own contributions, not to a newly established legal entity. This notice
neither transfers intellectual property to the team or GitHub organization nor
declares all team members joint owners of every file. Commit authorship, review
activity and hackathon membership do not by themselves establish legal ownership.
Individual copyright allocations, assignments and four-way joint ownership have
not been established by the reviewed records. Relevant rights holders must confirm
those matters before individual legal ownership is added to the notice.

### License scope and preserved rights

| Material / local paths | Treatment |
| --- | --- |
{scope_rows}

Rights and permission questions for excluded material remain with its actual
owners. Existing content is not cleared for redistribution merely because it is
tracked here. This scope statement adds no restrictions to the canonical MIT
terms for the software that is covered.

## Project attribution

**Jevelopers — neatHack 2026** is the team building **TicketStub**.
{cfg['purpose']}
The [repository README](README.md) describes the implementation and its limitations;
this attribution document does not certify a completed integration, deployment,
product release or accepted hackathon submission.

The [official event](https://neatlogs.com/hackathon) ran **October 10–12, 2026**.
Its published submission window extended into October 13, 2026; the public page
now reports submissions closed. This licensing update is not evidence that code
was written within the event window or that a submission met its cutoff.
See the [registration page](https://luma.com/s5blr882),
[Jevelopers organization](https://github.com/{ORG}),
[main application](https://github.com/{ORG}/getticketstub.com) and
[original agent-harness runtime](https://github.com/{ORG}/agent-harness).

## Team members and contacts

The [organization roster][roster] corroborates these four GitHub identities.
Captaincy and Crystal's name-to-handle mapping also use the team-supplied inventory.
The contribution descriptions below concern TicketStub across the organization;
they do not assert that every person authored code in this repository.

{PEOPLE}
### Verification and publication limits

The roster's public name **Zachary Wright** is retained rather than inferring an
expanded legal name from a handle. LinkedIn and X URLs are the team-supplied
professional links. The earlier agent-harness attribution review corroborated
LinkedIn titles, Timothy's GitHub-to-X link and Lars's indexed X handle; automated
profile retrieval was limited. Zachary's and Crystal's X profiles remain
team-supplied rather than independently corroborated. This review does not claim
fresh independent access to every social profile.

No individual email publication consent was established, so no supplied contact
address or Git author email is republished. “Not publicly listed” means omitted
from this document, not that a person has no email or website. Additional contact
information requires verification and the applicable person's publication approval.

## License and usage rights

Original software within the scope above may be used, copied, modified, merged,
published, distributed, sublicensed and sold under MIT. Preserve the copyright
notice and the full license text in copies or substantial portions as required.
The complete warranty disclaimer is in [LICENSE](LICENSE). No extra attribution,
branding, noncommercial or approval condition is inserted into that license.
Separately licensed content retains its own notices and distribution conditions.

### MIT selection and authoritative sources

Reviewed **October 13, 2026**: the public [neatHack rules](https://neatlogs.com/hackathon),
[Luma event description](https://luma.com/s5blr882), and
[official build companion](https://neatlogs.com/hackathon/skill) do not prescribe
a source-code license. MIT is the repository owner's explicitly requested fallback,
not a license attributed to a different event or inferred from sponsor publicity
permissions. Unpublished agreements and later rule changes are not covered by
this finding. [GitHub's license guidance](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)
and the [SPDX MIT text](https://spdx.org/licenses/MIT.html) identify the standard
license and its machine-readable identifier. The root license body is unmodified
apart from the year and collective copyright notice.

## Third-party attribution

{third}

The audit is tied to [source revision `{cfg['base_sha'][:7]}`]({url}/tree/{cfg['base_sha']}).
It inspected the tracked inventory, applicable instructions, manifests, relevant
source headers, existing notices and provenance records. It does not establish
an exhaustive chain of title or reclassify unknown asset rights as approved.

{evidence}

Package-manager references are distinct from copying dependency files. When a
package, archive, container or generated bundle actually includes external code,
retain its applicable license, copyright and NOTICE text. A later license on an
upstream default branch does not silently relicense an older pinned snapshot.
Existing source archives, evidence pins and asset bytes are preserved by this change.

## Branding and trademarks

Software copyright permissions do not grant trademark rights, rights to individuals'
identities, or permission to imply endorsement, sponsorship or affiliation.
Jevelopers, TicketStub, neatHack and referenced providers identify their respective
projects or services; no exclusive trademark ownership is asserted here.
Brand assets and any unresolved distribution or font-delivery decisions remain
with the [brand-kit owners](https://github.com/{ORG}/brand-kit).
This distinction does not restrict software uses already permitted by MIT.

## Project and team contact

The canonical project source for issues and contributions is
[getticketstub.com](https://github.com/{ORG}/getticketstub.com).
Use [project issues](https://github.com/{ORG}/getticketstub.com/issues) for project
coordination and [this repository's issues]({url}/issues) for repository-specific
questions or attribution corrections. Follow the
[organization contribution guidance](https://github.com/{ORG}/.github/blob/main/CONTRIBUTING.md).
The organization and member profiles above are the listed public contact routes;
no individual email address is published here.

[roster]: {ROSTER}
'''

def prepare(root: Path, name: str, cfg: dict, cache: Path | None = None) -> dict[str, bytes]:
    changes: dict[str, bytes] = {}
    def current(path: str) -> bytes:
        if path in changes: return changes[path]
        return (root / path).read_bytes()
    def put(path: str, value: str | bytes) -> None:
        if not valid_path(path) or path not in cfg['allowed_paths']:
            raise ValueError('Write outside reviewed licensing scope: ' + path)
        data = value.encode() if isinstance(value, str) else value
        original = root / path
        if original.is_symlink() or not original.resolve().is_relative_to(root.resolve()): raise ValueError('Unsafe target')
        if not original.is_file() or original.read_bytes() != data: changes[path] = data
    if (root/'LICENSE').exists(): raise ValueError('Existing root license must not be replaced')
    put('LICENSE', MIT)
    notice_sections = list(cfg.get('notice_sections', []))
    if cfg.get('entire'):
        guide = root/'.entire/graph-agent.md'
        if blob(guide.read_bytes()) != 'c2a3257cac08c6ef63b4884a61e2c4fd884028f7':
            raise ValueError('Entire guide differs from the reviewed upstream template')
        local = ['`.entire/graph-agent.md`']
        for path in ['AGENTS.md','CLAUDE.md']:
            if (root/path).exists() and '<!-- entire-graph:begin -->' in (root/path).read_text(): local.append(f'the `entire-graph` block in `{path}`')
        notice_sections.insert(0, f'''## Entire graph instructions

- **Component / original organization:** Entire graph agent guide; Entire Inc.
- **License:** MIT (SPDX `MIT`).
- **Local paths:** {', '.join(local)}.
- **Matching upstream source:** [agentGuide and instruction blocks](https://github.com/entireio/entire-graph/blob/{ENTIRE_REF}/internal/cli/agents.go).
- **Upstream license:** [LICENSE at `{ENTIRE_REF[:7]}`](https://github.com/entireio/entire-graph/blob/{ENTIRE_REF}/LICENSE).

The guide matches the reviewed upstream text. This identifies a source for the
copied documentation, not proof of the originally installed plugin version.
The complete upstream notice is retained without changing the instructions:

```text
{MIT.replace('2026 Jevelopers contributors','2026 Entire Inc.').rstrip()}
```
''')
    for item in cfg.get('upstream_files', []):
        data = read_pinned(item, cache)
        if item.get('normalize_trailing_whitespace'):
            data = ('\n'.join(line.rstrip() for line in data.decode().splitlines()) + '\n').encode()
        put(item['target'], data)
    for item in cfg.get('literal_files', []): put(item['path'], item['content'])
    if notice_sections:
        put('THIRD_PARTY_NOTICES.md', '# Third-party notices\n\nThese notices preserve separately owned material; they do not replace the project\n[LICENSE](LICENSE). See [COPYRIGHT.md](COPYRIGHT.md) for scope and unresolved rights.\n\n' + '\n\n'.join(notice_sections).rstrip() + '\n')
    put('COPYRIGHT.md', copyright_text(name, cfg, bool(notice_sections)))
    readme = current('README.md').decode()
    for old, new in cfg.get('readme_replacements', []):
        if readme.count(old) != 1: raise ValueError('README replacement anchor drift')
        readme = readme.replace(old, new, 1)
    if '[COPYRIGHT.md](COPYRIGHT.md)' not in readme:
        readme = readme.rstrip() + '\n\n## License and attribution\n\n' + cfg.get('readme_license', 'Original project code and technical documentation are licensed under the [MIT License](LICENSE).') + '\nSee [COPYRIGHT.md](COPYRIGHT.md) for Jevelopers team attribution, the exact scope,\nthird-party obligations and unresolved asset rights.\n'
    put('README.md', readme.rstrip() + '\n')
    for path in cfg.get('packages', []):
        text = current(path).decode()
        updated = set_license(text)
        if path == 'package.json':
            to_pack = ['LICENSE','COPYRIGHT.md']
            if notice_sections: to_pack.append('THIRD_PARTY_NOTICES.md')
            if any(p.startswith('licenses/') for p in changes): to_pack.append('licenses')
            updated = add_package_files(updated, to_pack)
        put(path, updated)
        lock_path = str(PurePosixPath(path).with_name('package-lock.json'))
        if (root/lock_path).is_file(): put(lock_path, set_license(current(lock_path).decode(), ('packages','')))
    if name == 'integration-evals':
        text=current('pyproject.toml').decode()
        if re.search(r'^license\s*=',text,re.M): raise ValueError('Existing Python license')
        anchor='version = "0.1.0"\n'
        if text.count(anchor)!=1: raise ValueError('Python metadata drift')
        put('pyproject.toml',text.replace(anchor,anchor+'license = "MIT"\nlicense-files = ["LICENSE", "COPYRIGHT.md", "THIRD_PARTY_NOTICES.md"]\n',1))
    if name == 'brand-kit':
        inv=json.loads(current('inventory/brand-inventory.json'))
        for path in ['LICENSE','COPYRIGHT.md','THIRD_PARTY_NOTICES.md']:
            inv['entries'].append({'id':path,'path':path,'type':'text' if path=='LICENSE' else 'markdown','category':'licensing','classification':'licence-provenance','description':'Software licensing and attribution; no brand asset approval or rights clearance.','owner_role':'Product and frontend (brand-system maintainer)','approval_status':'unknown','provenance_status':'licence-text-present','release_class':'internal','canonical_authority':path})
        put('inventory/brand-inventory.json',dump(inv))
    if name == 'marketing-material':
        inv=json.loads(current('docs/collateral-inventory.json'));prov=json.loads(current('review/provenance.json'))
        row=next(x for x in inv['trackedFiles'] if x['path']=='README.md')
        row['sha256']=digest(current('README.md'))
        row['trackedAtRevision']=cfg['base_sha'];row['pathAvailability']='created_in_candidate'
        for path in ['LICENSE','COPYRIGHT.md']:
            inv['trackedFiles'].append({'fileId':'LICENSING-'+path.replace('.','-').upper(),'path':path,'classification':'software_licensing_document','pathAvailability':'created_in_candidate','lifecycleState':'not_applicable','exists':True,'releaseEligible':False,'trackedAtRevision':cfg['base_sha'],'sha256':digest(current(path))})
        put('docs/collateral-inventory.json',dump(inv))
        for path in ['README.md','docs/collateral-inventory.json']:
            record=next(x for x in prov['records'] if x.get('source',{}).get('path')==path)
            value=digest(current(path));record['source']['revision']='sha256:'+value;record['source']['revisionKind']='sha256_content_digest';record['checksum']['value']=value
            record['lineage']['transformations'].append('2026-10-13: licensing navigation/inventory alignment only; existing collateral permissions, blockers and review state preserved.')
        put('review/provenance.json',dump(prov))
    if name == 'shared-contracts':
        path='scripts/generate.mjs';text=current(path).decode()
        if text.count('project_license: null')!=1: raise ValueError('Generator metadata anchor drift')
        put(path,text.replace('project_license: null','project_license: packageManifest.license ?? null',1))
        path='scripts/package-content.mjs';text=current(path).decode()
        anchor="path.endsWith('.mjs') || path.endsWith('.md') || path.endsWith('.json')"
        if text.count(anchor)!=1: raise ValueError('Package content anchor drift')
        put(path,text.replace(anchor,"path === 'LICENSE' || "+anchor,1))
        obj=json.loads(current('generated/dependency-provenance.json'));obj['project_license']='MIT';put('generated/dependency-provenance.json',dump(obj))
        manifest=json.loads(current('generated/package-content-manifest.json'))
        for path in list(manifest['files']):
            if path in changes: manifest['files'][path]='sha256:'+digest(changes[path])
        for path in ['LICENSE','COPYRIGHT.md','THIRD_PARTY_NOTICES.md']:manifest['files'][path]='sha256:'+digest(current(path))
        manifest['files']=dict(sorted(manifest['files'].items()))
        canonical=json.dumps(manifest['files'],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
        manifest['digest']='sha256:'+digest(canonical)
        put('generated/package-content-manifest.json',dump(manifest))
    for path,data in changes.items():
        if '\x00' in data.decode():raise ValueError('Binary content forbidden in licensing changes')
        if path in cfg.get('new_paths',[]) and (root/path).exists():raise ValueError('New path already exists')
    return changes

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--config',type=Path,required=True);ap.add_argument('--repo',required=True)
    ap.add_argument('--root',type=Path,required=True);ap.add_argument('--license-cache',type=Path)
    ap.add_argument('--output',type=Path,required=True);ap.add_argument('--write',action='store_true')
    args=ap.parse_args();cfg=json.loads(args.config.read_text())['repositories'][args.repo]
    changes=prepare(args.root.resolve(),args.repo,cfg,args.license_cache)
    result={'repository':ORG+'/'+args.repo,'base_sha':cfg['base_sha'],'base_tree':cfg['base_tree'],'files':[]}
    for path,data in sorted(changes.items()):
        result['files'].append({'path':path,'git_blob_sha':blob(data),'sha256':digest(data),'bytes':len(data)})
        if args.write:
            p=args.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    args.output.write_text(dump(result))
    print(json.dumps({'repository':result['repository'],'changed_files':len(changes),'write':args.write}))
if __name__=='__main__':main()
