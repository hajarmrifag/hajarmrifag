# Hajar Mrifag

Final-year **Software Engineering student at Sichuan University**, graduating in **2027**. I build backend and full-stack applications, with an interest in data systems and performance engineering.

**[Portfolio & case studies](https://hajarmrifag.github.io/)** · [LinkedIn](https://www.linkedin.com/in/hajar-mrifag-a7903334b)

I'm looking for software engineering opportunities after graduation. My main tools are **Python/FastAPI, React/TypeScript, C#/.NET, PostgreSQL and Docker**.

## Selected engineering work

### GridFlex — energy systems workspace

[Live application](https://gridflex.onrender.com/) · [Engineering case study](https://hajarmrifag.github.io/work/gridflex.html) · [Repository](https://github.com/hajarmrifag/gridflex-ai)

A React/TypeScript and FastAPI application for exploring renewable generation, battery dispatch and flexible demand.

- Six views covering system impact, hourly replay, scenario comparison, forecasting, stress testing and optimization.
- **31.9× faster shift + battery pipeline** in the recorded 60-day local benchmark, with identical numeric outputs in the compared case. This is an engine measurement, not a whole-app speedup.
- **91 Python tests and five browser journeys** at release 0.2.0, plus container smoke tests and deployment after CI checks pass.
- Explicit physical constraints, data-quality disclosures and chronological forecast evaluation.

[Benchmark conditions](https://github.com/hajarmrifag/gridflex-ai/tree/main/benchmarks) · [Architecture](https://github.com/hajarmrifag/gridflex-ai/blob/main/docs/architecture.md)

### Aegis Claims — full-stack workflow and application security

[Live application](https://claims-management-ync9.onrender.com) · [Repository](https://github.com/hajarmrifag/claims-management-api)

A React client and layered ASP.NET Core API with PostgreSQL persistence, role-based claim transitions and auditable history.

- API-enforced authorization, password hashing and validated document uploads.
- Unit, integration and browser tests; containerized delivery with health checks.
- A documented threat model and assessment, with CodeQL, Trivy and ZAP workflows.
- Explicit deployment limits: uploaded files in the public demo use ephemeral storage; an Azure Blob provider is available for durable storage.

[Security assessment](https://github.com/hajarmrifag/claims-management-api/blob/main/docs/security/assessment-report.md)

### CUDA Transformer Kernels — measured performance engineering

[Repository & results](https://github.com/hajarmrifag/cuda-transformer-kernels)

CUDA C++ matrix multiplication and Softmax implementations, profiled with NVIDIA Nsight Compute on a Tesla T4.

- **1.28 TFLOPS FP32 GEMM** at 1024 × 1024: 3.31× the naive kernel and 24% of cuBLAS throughput in the recorded workload.
- **1.71× Softmax throughput** from register caching at width 2048.
- Correctness checks against CPU references, warm-up runs and median timing. A slower warp-shuffle experiment remains documented alongside the measured winner.

### Neobank Analytics & Transaction API — data and backend systems

[Repository](https://github.com/hajarmrifag/neobank-growth-analytics) · [Analytics dashboard](https://neobank-growth-analytics-hajar.streamlit.app/)

A FastAPI/PostgreSQL transaction service with atomic transfers, idempotent retries, concurrency tests and container smoke checks. The separate analytics pipeline covers **891,772 synthetic transactions**, cohort retention and experiment economics.

## Team and research work

| Project | Focus |
| --- | --- |
| [SkyQuery](https://github.com/maryamibaaichou/Flight-Ticket-Meta-Search-and-Analysis) | University team project over 15M Expedia flight records. My role: backend and data engineering with FastAPI, HDFS, Hive and PySpark. |
| [Churn & Reactivation Engine](https://github.com/hajarmrifag/churn-reactivation-engine) | Historical banking transaction research with temporal features, purged evaluation and customer-risk segmentation. |
| [FinSight](https://github.com/hajarmrifag/finsight-streamlit) | An interface for exploring the banking research, evidence search and campaign scenarios. |

## What I want to work on

Backend and full-stack software, data-intensive applications, and systems where reliability and performance matter. I like projects with clear constraints, measurable outcomes and technical decisions I can explain.

Based in **Chengdu, China** · Expected graduation **2027** · [Let's connect](https://www.linkedin.com/in/hajar-mrifag-a7903334b)

*Public demonstrations on free hosting may need time to wake after inactivity.*
