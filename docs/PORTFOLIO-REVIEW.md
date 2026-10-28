# Engineering portfolio review

Prepared 28 October 2026. Proposal implemented only on `design/engineering-portfolio-2026`, based on live profile commit `7ab6752666d82bdaa102142d3941cd161a9f1562`. Nothing in this proposal changes the live profile, pins, repository descriptions, visibility or portfolio website.

## Audit scope and standard of evidence

Inventoried all 16 publicly listed repositories, inspected the available root READMEs, and examined selected implementation, test, benchmark and report files in 11 substantive repositories plus the portfolio. The internship repository was examined separately. This is a presentation and evidence audit, not a complete code review or a new benchmark run. Recorded results remain recorded results; source inspection is not proof that the current code passes every test.

The companion [source register](SOURCES.md) records immutable revisions and the exact implementation and evidence files reviewed. Local files were reused only when their Git blob hashes matched the current public tree. Public screenshots were copied unchanged. No private repositories, datasets, credentials or thesis implementation details are included. The thesis sentence uses only the project description supplied in the brief; it does not imply a finished robot, deployment or evaluation.

### The existing first impression

The live README has valuable strengths: specific measurements, direct evidence links, a mobile header and unusually candid performance caveats. Its problem is positioning and hierarchy, not a shortage of work.

In 5–10 seconds a reader sees “Backend systems. Measured performance.” followed by Java and CUDA. They can find the CV, but they could reasonably miss the AI evaluation, modelling, constraint solving, product design and research direction. The light paper/green header has little relationship to Night Floor's charcoal/brass identity; prose dominates the rest of the page. There is no visual evidence overview or product preview. PolicyLens is relegated to a closing sentence; PowerCut, the forensic lab and thesis are absent.

The current pins emphasize GridFlex, Aegis, CUDA, Neobank, SkyQuery and banking research. These are defensible choices, but leave the original PowerCut implementation and the Java reference-model work out of the six. A recruiter must reconstruct your range from several repositories.

### Portfolio and assets

The public homepage and GridFlex/SkyQuery case studies supply working routes, contact details and a CV. The public repository's homepage is the warm-paper engineering notebook. Night Floor exists in the local `studio` source of the separate portfolio checkout; its CSS establishes charcoal `#12141a`, ivory `#f4f0e6` and brass `#e0c089`. The attempted public `/studio/` URL returned a custom 404. This proposal uses the local visual reference and retains the working homepage link. It does not modify, build or deploy Night Floor.

GridFlex's real workspace image shows the interface and explicit modelling assumptions. PowerCut has extensive Vega Virtual Device screenshot evidence; the selected overview makes both the energy shortfall and model limitations visible. CUDA and PolicyLens already have evidence graphics in their repositories. Aegis and Sourced have useful architecture documentation but no comparable committed product screenshot in the inspected public trees. The forensic lab is strongest as a traceable evidence report, not as a conventional app screenshot.

## Design decisions

**Direction: an engineering folio.** Large serif name, restrained monospaced labels, fine rules and a computational tile illustration. The illustration is explicitly abstract; it does not pretend to encode experimental results. Light and dark artwork are independently authored from the same palette tokens. The charcoal treatment echoes Night Floor without copying its 3D objects or interaction model.

**Opening:** name, AI/systems/product identity, university, June 2027 graduation, location, and portfolio/CV/email/LinkedIn. These remain understandable when images are unavailable because the introduction and alt text repeat essential context.

**Evidence before a technology list:** a common-scale CUDA comparison that includes cuBLAS; 31 PolicyLens marks that retain seven failures; and the finite Java reference-model workload. The point is the quality of the experiment, not the largest possible number. Mobile artwork replaces the dense three-column strip with readable stacked summaries.

**Six concise entries:** each connects a real engineering decision to code and evidence. Product screenshots use native `details` disclosure so they can be inspected without stretching the initial page. Native text, links and headings remain selectable and reflow naturally. Other credible work stays in a compact further-investigations list.

**GitHub constraints:** no custom page CSS, scripts, external fonts, widgets or animations in the README. All visuals are repository-local; SVGs have no external dependencies, embedded scripts or foreignObject. Native `picture`, `source`, `img`, `details` and Markdown provide the layout. GitHub's Markdown API retained these elements. Light/dark art remains self-contained and legible even if a client falls back to the light image.

## Exactly six proposed pins, in order

| Position | Repository | Why it earns the slot |
| --- | --- | --- |
| 1 | [gridflex-ai](https://github.com/hajarmrifag/gridflex-ai) | Best opening demonstration of breadth: a usable full-stack product around numerical modelling, optimization, constraints and measurement. |
| 2 | [cuda-transformer-kernels](https://github.com/hajarmrifag/cuda-transformer-kernels) | Low-level implementation, GPU memory reasoning and comparison with a serious library baseline. Retains unsuccessful experiments and validation limits. |
| 3 | [policylens-ai](https://github.com/hajarmrifag/policylens-ai) | The clearest public AI evaluation story: retrieval, generation, answerability, adversarial cases and failure analysis. |
| 4 | [powercut](https://github.com/hajarmrifag/powercut) | Original algorithm-to-product work: DP scheduling, independent verification, cross-language checks and a remote-operated device interface. |
| 5 | [java-order-book](https://github.com/hajarmrifag/java-order-book) | Inspectable data structures, invariants, a genuinely different reference model and bounded JVM measurements. |
| 6 | [opportunity-compass](https://github.com/hajarmrifag/opportunity-compass) | Collaboration and product judgment: evidence-aware discovery through application planning, with individual ownership made explicit. |

This is an overall engineering/research selection, not a universal ranking. Neobank has strong database correctness evidence but overlaps the systems signal supplied by Java and GridFlex. Aegis adds security/workflow depth, retained in the README. The forensic lab is unusually rigorous and deserves a direct report link; its specialized domain is less central to this six-slot introduction. Banking research supplies tabular ML and temporal-validation depth, while PolicyLens makes the AI experimental loop faster to inspect. SkyQuery retains a dedicated internship paragraph; the shared work is not presented as a solo project.

## Targeted repository improvements

These are recommendations only. No source code, README or settings in these repositories were changed.

| Repository | Presentation/documentation changes | Engineering or evidence work, separately scoped |
| --- | --- | --- |
| **GridFlex** | Keep the screenshot, engine boundary and case study. Add one small input → simulation → API → interface diagram and put historical/current benchmark protocols side by side. Give a shortest no-key reproduction path. | Run several independent paired benchmark repetitions before asserting stable performance. Distinguish perfect-foresight optimization from an online controller; forecasts and physical model assumptions need their own evaluation. |
| **CUDA** | Keep cuBLAS on the same chart scale. Link each plotted value to a dated run and identify source revision/toolchain. Reconcile 3.31× in the old results prose with the arithmetic rounding of 1278.508 / 385.648 ≈ 3.315× → 3.32×. | Compile and run the current optional GPU tests, including odd shapes and width guards, then preserve raw timings and profiler exports. Historical results cannot validate later changes; absent Nsight exports cannot be recreated editorially. |
| **PolicyLens** | Add one real question → retrieved passage → answer/refusal screenshot, with a visible failed example. Put the 24/31 evaluation and 0/3 partial-evidence result beside corpus size and calibration caveat. Reconcile the live app's older totals. | Separate calibration from held-out evaluation, compare a stronger or extractive reader, and improve conflict/partial-evidence handling. Keyword scoring is limited; retrieval Recall@3 is not answer accuracy. |
| **PowerCut** | Lead with the actual overview and a 60-second demo path. Replace the long historical narrative with shipped TypeScript path → independent verifier → Python oracle. Reconcile old 163/164 counts with the current 231 fixture cases and 232 differential test cases; move phase history into docs. | Worst-case repair work blocks the JS thread for around two seconds in the recorded virtual-device tests. Deferring one macrotask does not make the calculation asynchronous. Consider chunked/cooperative work or a supported worker architecture. Repeat wall-clock measurements with controlled load; 770 → 629 solver calls does not establish a latency speedup. Avoid calling noisy timings “statistically indistinguishable” without a statistical analysis. |
| **Java Order Book** | Preserve the small matching diagram and put “single writer / in memory / one instrument” near the title. Add a short trace mapping one partial fill to queue and ID-index changes. Keep JMH batch sizes and allocation denominators next to numbers. | No concurrent-writer, persistence, recovery or network guarantees are implemented. These are scope limits, not cosmetic omissions. A finite 60,000-command comparison is not a formal proof; any extension needs its own correctness and workload design. |
| **Sourced** | Add a real discovery → compare → Journey screenshot sequence, a team ownership panel, and an explicit local-data/account-data diagram. Use Sourced as the display name while retaining the stable repository URL. | Browser-local Journey does not migrate automatically to Supabase. Validate recovery/export and live integration failure paths in separate work. Keep unknown eligibility and funding visible; do not imply autonomous applications or available Gmail scanning. |
| **Neobank** | Separate API and analytics into two clear paths from the opening. Keep the lock/transaction diagram; identify synthetic data beside every business result. Label the dashboard as an analytics demo, not a transaction UI. | The local service lacks production authentication/account ownership. Real concurrency and rollback tests are stronger evidence than HTTP mocks, but do not establish production ledger guarantees. Query-plan timings are not HTTP latency. |
| **Aegis Claims** | Add screenshots of claim detail/history and a compact role/action matrix linked to controller tests. The current README already distinguishes EF InMemory HTTP tests from real PostgreSQL checks; retain that distinction. | Tenant ownership, optimistic concurrency and a strict lifecycle state machine are absent. Valid file signatures do not establish malware safety. Ephemeral demo uploads and the limits of unauthenticated ZAP coverage must remain visible. |
| **Forensic Evidence Lab** | Start with the two cases and a concise “claim → artefact → verification” example. Show the independent NTFS reconstruction and report links before the long commands. Separate lightweight CI from dataset tests. | The parser covers the chosen volume, not all NTFS. It does not independently decompress LZNT1 or decrypt EFS. Publisher XML based on historical TSK is not independent tool validation. Do not imply malicious intent, recovered encryption keys or certified evidence. |
| **Churn / FinSight** | Use a temporal split/90-day outcome diagram. Lead with the purged result and show the original result as a separately labelled comparison. Link the FinSight interface to the research repo so two repos do not look like two independent studies. | Source CSVs and fitted model are absent from the public repository; CI does not rebuild the full experiment. Publish permitted acquisition instructions, checksums and dated aggregate run evidence. Historical account-month observations are not unique customers; campaign economics are assumptions, not observed intervention impact. |
| **SkyQuery internship** | Put the two-person contribution table and architecture split first. Describe PySpark/HDFS/Hive analysis separately from the FastAPI/SQLite conversational prototype. Link individual code and saved output. | The execution service uses SQLite despite its Hive-oriented naming and has hardcoded local paths. A SELECT/WITH prefix check is not a complete query safety boundary. The splicing script limits daily results before collection, so saved “opportunities” are bounded output, not an exhaustive market count. Avoid unverified “production-grade” and end-to-end latency claims. |
| **AI Study Companion thesis** | Use only the brief's high-level description and “work in progress” until public material is intentionally released. Later, a research question, architecture sketch and short robot demo would be useful. | No public implementation/evaluation was verified. Do not claim completed hardware, measured learning gains, deployment, publication or participant studies. |

The course fork (`fullstack-course4`), course exercise (`coursera-test`) and currently sparse public learning portfolio are learning context, not flagship pins. The portfolio and profile repositories provide navigation rather than separate engineering evidence.

## Manual GitHub settings, only after approval

1. Open your GitHub profile and choose **Edit profile**. Suggested bio: `Software Engineering @ Sichuan University · June 2027 · AI, GPU computing & product engineering`. Keep the working portfolio URL. Save only when the wording is approved.
2. On your profile, choose **Customize your pins**. Select the six repositories above; remove the other selections to stay within six. Choose **Save pins**. Drag the pins using their upper-right handles into the proposed order. See [GitHub's pinning instructions](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile).
3. If desired, update only the profile repository's About description to `Selected engineering work: AI evaluation, GPU computing, algorithms and full-stack products.` Repository descriptions/topics elsewhere require separate authorization.
4. To publish the README later, push this design branch, review its complete diff and open a PR into the profile repository's `main`. Approve the rendered branch preview before merging. The special profile repository renders its default-branch README; a local branch does not change the profile.

The current delivery stops at a local branch and preview. No push or PR has been made. Existing README and assets remain recoverable from the base commit; the two original SVG files are also retained unchanged. A future rollback should revert the redesign commit, not rewrite history.
