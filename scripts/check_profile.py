"""Validate the portable README and static SVG contract; no network required."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
s=(ROOT/'README.md').read_text()
projects=['gridflex-ai','powercut','cuda-transformer-kernels','policylens-ai','java-order-book','opportunity-compass']
assert s.startswith('<a href="https://github.com/hajarmrifag/gridflex-ai">\n<picture>'),'first featured project must open the README'
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
assert '<details>' not in s
assert s.count('<picture>')==s.count('</picture>')==6
assert s.count('graduating June 2027')==1
assert 'perfect foresight' in s and 'not held-out results' in s and 'await a GPU rerun' in s
assert 'optimality is limited to that scope' in s and 'finite regression set' in s
print(f'PASS: six directly linked selected projects (screenshots embedded in SVG); {len(refs)} link/image references; valid self-contained SVGs; visible product evidence and retained measurement limits.')
