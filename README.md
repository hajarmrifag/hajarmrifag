I’m **Hajar Mrifag**, a Software Engineering student at Sichuan University, with expected graduation in June 2027. I build software and data systems, investigate AI/ML questions, and work on algorithms, performance and collaborative products.

**[Portfolio](https://hajarmrifag.github.io/)** · **[CV](https://hajarmrifag.github.io/assets/Hajar-Mrifag-CV.pdf)** · **[Project index](#more-engineering-work)** · **[Contact](mailto:hajarmrifag2@gmail.com)**

## Selected work

[GridFlex](https://github.com/hajarmrifag/gridflex-ai) · [WebAtlas](https://github.com/hajarmrifag/webatlas) · [CUDA kernels](https://github.com/hajarmrifag/cuda-transformer-kernels) · [ViewShift Lab](https://github.com/hajarmrifag/viewshift-lab) · [Java Order Book](https://github.com/hajarmrifag/java-order-book) · [Sourced](https://github.com/hajarmrifag/opportunity-compass)

<a href="https://github.com/hajarmrifag/gridflex-ai">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/hero-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/hero-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" width="960" alt="Hajar Mrifag, final-year Software Engineering student at Sichuan University working across AI, systems and product engineering. Featured project GridFlex AI: real workspace screenshot; recorded 60-day shift plus battery engine workload 71.731 to 2.246 ms, about 32 times faster.">
</picture>
</a>

**Personal project · full-stack and numerical computing.** I built the React workspace, FastAPI API and simulation engine. The historical 60-day shift + battery workload fell from 71.731 to 2.246 ms; this is engine timing, not application latency. Retrospective optimization assumes perfect foresight. [Benchmark evidence](https://github.com/hajarmrifag/gridflex-ai/tree/main/benchmarks).

<a href="https://github.com/hajarmrifag/webatlas">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/webatlas-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/webatlas-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/webatlas-dark.svg">
  <img src="assets/webatlas-light.svg" width="960" alt="WebAtlas architecture: PostgreSQL leases, bounded workers, transactional history and acknowledgement. Recorded synthetic crash test recovered 64 leases and completed 300 of 300 jobs. At-least-once execution with idempotent committed effects.">
</picture>
</a>

**Personal project · backend and data systems.** PostgreSQL leases coordinate bounded ingestion; observation history and job acknowledgement commit together. A recorded synthetic crash test reclaimed 64 leases and completed 300/300 jobs. At-least-once execution with idempotent committed effects, not exactly once. [Recovery evidence](https://github.com/hajarmrifag/webatlas/blob/main/docs/reliability.md).

<a href="https://github.com/hajarmrifag/cuda-transformer-kernels">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/cuda-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/cuda-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/cuda-dark.svg">
  <img src="assets/cuda-light.svg" width="960" alt="CUDA Transformer Kernels: on a T4, FP32 GEMM at 1024 by 1024, naive 385.648, custom 1278.508 and cuBLAS 5322.721 GFLOP/s; custom reaches 1.28 TFLOPS, 3.32 times naive and 24 percent of cuBLAS, kernel time only.">
</picture>
</a>

**Personal project · systems and optimization.** CUDA C++ GEMM and Softmax experiments keep cuBLAS visible as the stronger reference. [Historical T4 results](https://github.com/hajarmrifag/cuda-transformer-kernels/tree/main/results) measure kernel time only. Current GPU validation changes **await a GPU rerun**; raw historical profiler exports were not retained.

<a href="https://github.com/hajarmrifag/viewshift-lab">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/viewshift-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/viewshift-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/viewshift-dark.svg">
  <img src="assets/viewshift-light.svg" width="960" alt="ViewShift Lab independent research. Mean synthetic OOD accuracy across four training seeds: 48.1 percent single-view CNN and 57.8 percent two-view CNN. Same scenes, matched parameters, extra two-view compute. Real-photo evaluation pending.">
</picture>
</a>

**Independent research · AI/ML and experimental design.** Matched CNN parameters, disjoint scene splits, four training seeds and paired predictions. Mean two-view advantage: +9.7 percentage points on fixed synthetic OOD scenes, with extra input and compute. Projected disks limit interpretation; real-photo validation is pending. [Repeatability and uncertainty](https://github.com/hajarmrifag/viewshift-lab/blob/main/reports/repeatability.md).

<a href="https://github.com/hajarmrifag/java-order-book">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/orderbook-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/orderbook-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/orderbook-dark.svg">
  <img src="assets/orderbook-light.svg" width="960" alt="Java Order Book: 40 seeds of 1,500 generated commands, 60,000 in total, checked against an independent list-based model.">
</picture>
</a>

**Personal project · algorithms and JVM engineering.** One writer owns price-time matching, FIFO queues and cancellation. Twenty tests include 60,000 generated commands checked against an independent model: a finite regression set, not a proof. Educational in-memory system; JMH measures bounded batches, not end-to-end order latency. [Design and results](https://github.com/hajarmrifag/java-order-book#readme).

<a href="https://github.com/hajarmrifag/opportunity-compass">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/sourced-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/sourced-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/sourced-dark.svg">
  <img src="assets/sourced-light.svg" width="960" alt="Sourced, a team product from the BUILD ACROSS Hackathon. Its own flow: source-linked search and a user-confirmed Passport feed a review where unknown stays unknown, then compare and plan, My Journey and a Tracker. I built search, comparison, My Journey and affordability-scenario UI; teammates owned CV extraction, retrieval and eligibility verification.">
</picture>
</a>

**Team hackathon · product development.** Sourced, BUILD ACROSS, Hong Kong, 3–4 October 2026. I built search, persistent comparison, My Journey, Opportunity Brief and affordability-scenario UI. Teammates owned extraction, retrieval and eligibility verification; the finance teammate owned the pure calculator integration. [Contributions and prototype limits](https://github.com/hajarmrifag/opportunity-compass#readme).

## More engineering work

| Project / context | Decision and evidence |
| --- | --- |
| [Aegis Claims](https://github.com/hajarmrifag/claims-management-api) · personal | API role checks, file-signature validation and layered .NET persistence. [22-test record](https://github.com/hajarmrifag/claims-management-api/blob/main/docs/verification-results.md), including real PostgreSQL constraints; no tenant ownership or optimistic concurrency. |
| [Neobank](https://github.com/hajarmrifag/neobank-growth-analytics) · personal | Ordered account locks and idempotent retries. [37-test verification](https://github.com/hajarmrifag/neobank-growth-analytics/blob/main/docs/engineering-verification.md); synthetic funds. Analytics is a separate pipeline. |
| [PowerCut](https://github.com/hajarmrifag/powercut) · Amazon hackathon entry | On-device TypeScript solver, independent verifier and Python reference. Repairs change one or two appliances; optimality is limited to that scope. |
| [PolicyLens](https://github.com/hajarmrifag/policylens-ai) · personal | 15/15 evidence-bearing retrieval cases found the passage; full evaluation passed 24/31, including 0/3 partial-evidence cases. Four synthetic documents; calibration reused questions: not held-out results. |
| [Churn research](https://github.com/hajarmrifag/churn-reactivation-engine) / [FinSight](https://github.com/hajarmrifag/finsight-streamlit) | Purged temporal evaluation and a separate research interface. Historical banking activity is not account closure; campaign effects were not measured. |
| [Quantum Confinement Lab](https://github.com/hajarmrifag/quantum-confinement-lab) · independent research | Numerical eigenproblems checked against matching equations and convergence studies. Idealized 1D physics, not experimental device validation. |
| [Forensic Evidence Lab](https://github.com/hajarmrifag/forensic-evidence-lab) · personal | Binary parsing, integrity hashes and reproducible FAT/NTFS evidence. Artefacts do not establish an actor or authorization. |
| [DevInsight](https://github.com/hajarmrifag/DevInsight) · independent research | Source-linked pipeline over 18 public Vite reports. Exploratory sample, no interviews or prevalence estimates. |

<details>
<summary>Visual notes: PowerCut and PolicyLens</summary>

<a href="https://github.com/hajarmrifag/powercut">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/powercut-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/powercut-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/powercut-dark.svg">
  <img src="assets/powercut-light.svg" width="960" alt="PowerCut: real Vega Virtual Device screenshot showing a 1,908 Wh outage plan against a 1,800 Wh battery, 108 Wh over, with the TypeScript solver, schedule verifier and Python reference pipeline and 231 differential scenarios.">
</picture>
</a>

<a href="https://github.com/hajarmrifag/policylens-ai">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/policylens-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/policylens-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/policylens-dark.svg">
  <img src="assets/policylens-light.svg" width="960" alt="PolicyLens AI: expected evidence in the top three 15 of 15, evaluation cases passed 24 of 31, partial-evidence cases 0 of 3. Synthetic documents, not held-out results.">
</picture>
</a>

</details>

## Experience & university work

**Internship — Data & AI Engineering, Chengdu Suncaper Data, March–April 2026.** On the two-person [SkyQuery project](https://hajarmrifag.github.io/work/skyquery.html), I owned backend/data engineering: PySpark/HDFS/Hive analysis over a documented 15M flight records and a separate FastAPI/SQLite query prototype. My teammate owned frontend and contributed analysis. The large dataset count does not describe the prototype database.

**University thesis — AI Study Companion.** Explores adaptive tutoring and a physical robot. This is separate from the independent studies above; implementation and results are not presented as public evidence here. [University learning notes and publication scope](https://github.com/hajarmrifag/university-learning-portfolio).

Based in Chengdu, China. Interested in software engineering, AI/ML, data engineering, research and graduate opportunities. **[Explore my portfolio](https://hajarmrifag.github.io/)**.

<sub>Free-hosted demonstrations may need time to wake. Measurement records belong to their documented workloads and environments.</sub>
