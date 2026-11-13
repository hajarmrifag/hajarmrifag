"""Validate the portable README and static SVG contract; no network required."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
s=(ROOT/'README.md').read_text()
projects=['gridflex-ai','webatlas','cuda-transformer-kernels','viewshift-lab','opportunity-compass','powercut','policylens-ai','java-order-book']
assert s.startswith('I’m **Hajar Mrifag**'), 'broad introduction must precede project artwork'
for repo in projects:
 assert re.search(r'<a href="https://github.com/hajarmrifag/'+repo+r'">\n<picture>',s),repo
assert '<script' not in s.lower() and '<style' not in s.lower()
refs=re.findall(r'(?:src|srcset)="([^"]+)"',s)+re.findall(r'\]\(([^)]+)\)',s)
for link in refs:
 if not re.match(r'^(https?://|mailto:|#)',link):assert (ROOT/link).is_file(),link
for f in (ROOT/'assets').glob('*.svg'):
 root=ET.parse(f).getroot()
 assert root.attrib.get('viewBox'),f
 assert root.find('{http://www.w3.org/2000/svg}title') is not None,f
 for node in root.iter():
  assert node.tag.split('}')[-1] not in ['script','foreignObject'],f
  for k,v in node.attrib.items():
   assert not k.lower().startswith('on'),(f,k)
   if k.split('}')[-1] in ['href','src']:assert not v.startswith(('http:','https:')) and (not v.startswith('data:') or v.startswith('data:image/jpeg;base64,')),f
assert s.count('<details>') == s.count('</details>') == 1
assert s.count('<picture>')==s.count('</picture>')==8
assert s.count('expected graduation in June 2027')==1
assert 'perfect foresight' in s and 'not held-out results' in s and 'await a GPU rerun' in s
assert 'optimality is limited to that scope' in s and 'finite regression set' in s
assert 'projects.html' not in s and 'engineering-identity-review' not in s and '127.0.0.1' not in s
assert '[Project index](#more-engineering-work)' in s
assert 'Independent research' in s and 'Team hackathon' in s and 'University thesis' in s
visible, extra = s.split('<details>', 1)
for repo in ['gridflex-ai','webatlas','cuda-transformer-kernels','viewshift-lab','java-order-book','opportunity-compass']:
 assert f'<a href="https://github.com/hajarmrifag/{repo}">\n<picture>' in visible,repo
for repo in ['powercut','policylens-ai']:
 assert f'<a href="https://github.com/hajarmrifag/{repo}">\n<picture>' in extra,repo
portfolio_refs = re.findall(r'https://hajarmrifag\.github\.io/[^\s)"<]*',s)
assert set(portfolio_refs) <= {'https://hajarmrifag.github.io/', 'https://hajarmrifag.github.io/assets/Hajar-Mrifag-CV.pdf', 'https://hajarmrifag.github.io/work/skyquery.html'}
print(f'PASS: broad introduction and eight directly linked project panels; {len(refs)} link/image references; valid self-contained SVGs; broad identity, contribution boundaries and measurement limits retained.')
