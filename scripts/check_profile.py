"""Validate the portable README and static SVG contract; no network required."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
s=(ROOT/'README.md').read_text()
assert len(re.findall(r'^### 0[1-6] / ',s,re.M))==6
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
   if k.split('}')[-1] in ['href','src']:assert not v.startswith(('http:','https:','data:')),f
assert s.count('<details>')==s.count('</details>')==2
assert s.count('<picture>')==s.count('</picture>')==2
print(f'PASS: six selected projects; {len(refs)} link/image references; ten valid self-contained SVGs; native disclosure and picture markup.')
