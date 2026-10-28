# Preview and validation record

28 October 2026. Documentation/artwork change only. Project benchmark and test suites were not rerun; the README attributes historical results to their public evidence.

## Completed

- Created `design/engineering-portfolio-2026` from public profile revision `7ab6752666d82bdaa102142d3941cd161a9f1562` in a separate local Git worktree.
- Parsed all ten SVG files as XML. The eight new SVGs and two retained originals have viewBox/title metadata and no scripts, foreignObject or external resources.
- Confirmed six showcase entries, two picture elements, two native disclosures, and all 39 README link/image references have valid local syntax and existing local targets where applicable.
- Verified all 21 distinct GitHub repository/file/directory targets in the README against current public tree inventories.
- Submitted the proposed README to GitHub's Markdown API without publishing it. The sanitized response retained the picture/source order, responsive/theme queries, native details/summary elements and image alt text.
- Inspected browser renders at 1100px in light and dark mode, 390px in light and dark mode, and 320px in dark mode. The preview uses the actual GitHub-rendered HTML with approximate GitHub page styling. Fixed-width local preview frames select the real responsive SVG variants; the light/dark iframe color scheme selects the corresponding artwork.
- Replaced the dense mobile evidence strip with independently composed stacked summaries. All substantive copy remains native, reflowing text beneath the art. No clipped headline or horizontal overflow was observed in the inspected views.
- Verified both the GridFlex and PowerCut native screenshot disclosures expand, and inspected the rendered PowerCut screenshot at 320px. Local preview image-link paths were corrected separately from the already-valid README paths.
- Calculated foreground/background contrast ratios for the new SVG text palette: dark primary 15.51:1, brass 9.82:1, secondary 8.59:1; light primary 13.31:1, brass 5.21:1, secondary 5.45:1. All exceed 4.5:1. Decorative rules/tiles are not used to convey essential information.
- Checked screenshot provenance byte-for-byte against the public blobs. No new product screenshots or measurements were fabricated.
- Confirmed homepage, CV and both linked case studies returned HTTP 200; the CV response has a valid PDF signature.
- Confirmed the 231-case PowerCut fixture count directly, the PolicyLens aggregate results from JSON, Java's 40 × 1,500 loop bounds, and the CUDA comparison arithmetic and GridFlex measurement conditions.
- Ran `python3 scripts/check_profile.py` and Git whitespace checks.

## Limits and checks before publication

- These are local screenshots of GitHub-rendered content, not screenshots of a published branch on github.com. Repository chrome, GitHub's own theme selector, image proxy/cache behavior and browser-specific font substitutions should receive one final inspection on the remote design branch before merging.
- The first HTTP probe to GridFlex timed out. A subsequent browser visit loaded the application and reached “Simulation ready,” with populated metrics and charts. Free-host wake time is not evidence of a broken repository link.
- LinkedIn returned HTTP 999 to the automated probe. Its URL matches the existing public profile/portfolio, but automated reachability is unverified.
- The Night Floor `/studio/` URL returned 404. The redesign links to the verified portfolio homepage and makes no deployment change.
- No private thesis implementation, robot readiness or study results were verified. Only the user-provided work-in-progress description appears.
- A published branch and GitHub settings changes require the user's next approval. Nothing was pushed, merged or deployed during this delivery.

## Reproduce local asset checks

From this profile checkout:

```sh
python3 scripts/build_artwork.py
python3 scripts/check_profile.py
git diff --check
```

The artwork generator uses only Python's standard library. The README itself has no build/runtime dependency. Updating a measurement requires updating its public evidence, README context and artwork together.

## Exact change inventory

- Rewrote `README.md`: broader positioning; six selected projects; evidence and limitation links; expandable product screenshots; further investigations; internship ownership; brief thesis status; contact paths.
- Added eight SVGs: header/evidence × desktop/mobile × light/dark.
- Added two unchanged public product screenshots.
- Added `scripts/build_artwork.py` and `scripts/check_profile.py`.
- Added this validation record, `PORTFOLIO-REVIEW.md` and `SOURCES.md`.
- Retained the original `assets/header.svg` and `assets/header-mobile.svg` unchanged. Git history preserves the old README.
