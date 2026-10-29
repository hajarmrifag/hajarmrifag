# Validation record

Documentation and artwork change only. Project benchmark and test suites were not rerun: every number in the README is attributed to its recorded public evidence ([source register](SOURCES.md)).

## Checked

- **Static checks.** `python3 scripts/check_profile.py` passes: GridFlex opens the README; all six projects are linked panels; 24 referenced SVGs exist; every SVG has a viewBox and title and contains no scripts, `foreignObject`, event handlers or external references (only `data:image/jpeg` is allowed); required limit statements are present.
- **Real GitHub rendering.** The branch was pushed to a temporary branch and loaded on github.com at desktop and phone width. All panels, including the two with embedded JPEGs, were served as `image/svg+xml` and displayed. The temporary branch was then deleted. GitHub's Markdown API also retained the `picture`/`source` structure and alt text.
- **Responsive rendering.** Light and dark at 1100 px and 390 px in headless Chrome; no clipping or horizontal overflow observed. A local browser follows the OS colour scheme, so light previews were made by dropping the dark `source` elements. GitHub's own theme setting can disagree with the OS in the same way.
- **Contrast.** Text colours measured against each panel's base colour (ignoring the faint accent glow): dark theme at least 7.05:1; light theme at least 4.60:1 (GridFlex accent), body text 5.2:1 and above.
- **Links.** All 15 distinct external URLs resolved, except the GridFlex free-hosted demo, which timed out at 25 s in the automated probe. Free hosting needs time to wake; a prior browser visit reached "Simulation ready".
- **Provenance.** `assets/gridflex-workspace.png` and `assets/powercut-workspace.png` are the unchanged public screenshots. The JPEGs in `scripts/src/` are crops/resizes of them. Plotted values come only from recorded results; `≈32×` is 71.731 ÷ 2.246; `3.32×` and `24%` are the arithmetic of 1278.508 / 385.648 and 1278.508 / 5322.721.
- **Attribution.** Redesign commits are authored by the repository owner. No history was rewritten.

## Limits

- Sourced has no product screenshot: its repository contains none and has no live deployment. The panel uses the README's own architecture diagram instead.
- Panels use system font stacks, so letterforms differ by operating system.
- Thesis implementation, robot readiness and study results were not verified; only the supplied description appears.
- LinkedIn is not linked from the README. Its URL could not be verified by automated probe.

## Rebuild

```sh
python3 scripts/build_artwork.py   # regenerates assets/*.svg from scripts/src/*.jpg
python3 scripts/check_profile.py
git diff --check
```

Standard library only. Changing a measurement means changing its public evidence, the README text and the artwork together.
