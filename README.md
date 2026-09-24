# Hi, I'm Hajar 👋

I'm a final-year **Software Engineering student at Sichuan University**, expecting to graduate in **2027**, building backend, distributed, data-intensive, and performance-oriented software systems.

I enjoy working on problems that go beyond basic CRUD: API design, authentication and authorization, database performance, distributed data processing, containerization, CI/CD, testing, and low-level performance optimization.

My recent work spans **Python/FastAPI, React/TypeScript, C#/.NET, PostgreSQL, Docker, AWS EC2, Hadoop/Spark, and CUDA C++**.

I am particularly interested in data-intensive decision systems across financial technology, infrastructure, and energy, especially where reliability, optimisation, and trustworthy software matter.

## Engineering Evidence at a Glance

| Capability | Evidence |
|---|---|
| Production delivery | Live full-stack Claims deployment, multi-stage Docker build, health checks, structured logging, CI/CD, SAST and DAST |
| Backend engineering | ASP.NET Core claims platform and FastAPI transaction service with authentication, authorization, pagination and atomic transfers |
| Data engineering | 15M-record Hadoop/Hive/PySpark team project and a reproducible PostgreSQL analytics pipeline over 891K synthetic transactions |
| Data and AI | Leakage-aware temporal ML validation, explainable risk segmentation, evidence retrieval and scenario analysis |
| Reliability and integrity | Integration and browser tests, idempotency, rollback/concurrency tests, audit histories, threat modelling and explicit model limitations |
| Performance engineering | CUDA kernels benchmarked against CPU references and cuBLAS, with Nsight-guided optimization |

---

## Featured Engineering Projects

### 🛡️ Claims Management Platform
**React · TypeScript · C# · ASP.NET Core · PostgreSQL · Docker · GitHub Actions**

[View repository](https://github.com/hajarmrifag/claims-management-api) · [Live application](https://claims-management-ync9.onrender.com)

A deployed full-stack insurance claims platform with a responsive React client, layered ASP.NET Core API, role-based workflows, persistent data, automated tests, and security controls.

**Engineering highlights:**
- Built a React and TypeScript interface with protected routes, typed form validation, server-state caching, filtering, pagination, and responsive layouts
- Built a multi-layer .NET architecture across Domain, Application, Infrastructure, and API projects
- Implemented JWT authentication with secure password hashing
- Added role-based authorization for Adjuster, Manager, and Admin workflows
- Designed auditable claim status transitions and claim history
- Added authenticated document upload and download with size, type, filename, and magic-byte validation
- Abstracted file storage to support both local storage and Azure Blob Storage
- Deployed a multi-stage Docker image with PostgreSQL and health checks on Render
- Added unit, integration, component, and Playwright browser tests
- Automated frontend and backend validation plus CodeQL, Trivy, Dependabot, and OWASP ZAP security checks

This project demonstrates complete product delivery across frontend state and forms, API design, security, persistence, testing, observability, containerization, and CI/CD.

---

### ⚡ GridFlex AI: Renewable Power Systems
**Python · Optimisation (LP) · Energy Storage · Demand Flexibility · Streamlit · pytest · GitHub Actions**

[View repository](https://github.com/hajarmrifag/gridflex-ai) · [Live application](https://gridflex-energy-sim.streamlit.app/)

A battery-dispatch and demand-flexibility simulator for high-renewables grids, with a Morocco (Tétouan) and Germany case study built on public data. The README reports results from a systematic experiment matrix rather than only describing the tool.

**Highlights:**
- Physically constrained battery model (state of charge, power limits, round-trip losses) and energy-conserving daily demand shifting
- Perfect-foresight LP benchmark showing a simple threshold rule captures 0.6% peak reduction where 6.7% is achievable (Tétouan, 4 h battery)
- In Tétouan, 5% demand flexibility avoided about as much curtailment as a 4 h battery and cut peak demand 5.0% vs 0.6%
- Found that greedy load shifting above ~10% flexibility creates a rebound peak in the Germany profile
- Clear separation of measured vs estimated data, with limitations stated

---

### 🏦 Neobank Growth Analytics + Banking API
**Python · FastAPI · PostgreSQL · Docker · Docker Compose · GitHub Actions · SQL**

[View repository](https://github.com/hajarmrifag/neobank-growth-analytics)<br>
[Live analytics dashboard](https://neobank-growth-analytics-hajar.streamlit.app/)

An end-to-end neobank analytics platform with a separate transaction API for simulated banking workflows.

**Backend engineering highlights:**
- Built a FastAPI + PostgreSQL transaction API
- Implemented balances, transaction history, atomic transfers, and idempotent retries
- Containerized the API using Docker
- Orchestrated API and PostgreSQL services using Docker Compose
- Added PostgreSQL health checks, persistent volumes, and service dependencies
- Added automated API and database testing
- Built Docker images inside GitHub Actions
- Verified running containers over HTTP during CI
- Added database query-index benchmarking and concurrency/rollback testing

**Analytics scale:**
- **50,000 customers**
- **891,772 transactions**
- **£49.8M simulated completed transaction volume**
- **35,536 transacting customers**

The analytics layer also covers acquisition, cohort retention, experimentation, segmentation, and unit economics.

---

### ✈️ SkyQuery
**Hadoop HDFS · Apache Hive · PySpark · FastAPI · Python · SQL**

[View team repository](https://github.com/maryamibaaichou/Flight-Ticket-Meta-Search-and-Analysis)

A university team project built on **15 million Expedia flight records**.

**My role: Backend & Data Engineering**

My work included:
- Distributed processing with Hadoop HDFS, Hive, and PySpark
- Backend API development using FastAPI
- Data enrichment and large-scale analysis pipelines
- Natural-language-to-HiveQL backend integration
- Query execution and schema-aware backend services
- Automated setup and service orchestration scripts

The text-to-SQL system translated natural-language requests into HiveQL with a measured response of approximately **244 ms** in the project environment and included a three-retry self-correction loop.

This project gave me hands-on experience working with distributed data infrastructure rather than only single-machine analytics.

---

### ⚡ CUDA Transformer Kernels
**CUDA C++ · C++ · CMake · NVIDIA Nsight Compute · GPU Performance Engineering**

[View repository](https://github.com/hajarmrifag/cuda-transformer-kernels)

CUDA implementations and performance analysis of two core transformer operations: matrix multiplication and row-wise Softmax.

#### GEMM

I iteratively optimized matrix multiplication through:

`naive global memory → shared-memory tiling → register tiling → profiling → shared-memory padding`

At `1024 × 1024`, the final custom kernel achieved:

- **1.28 TFLOPS FP32**
- **3.31×** the throughput of the naive CUDA implementation
- **24.0% of cuBLAS SGEMM throughput**

Nsight Compute profiling helped identify scheduler pressure and shared-memory bank conflicts. Padding reduced excessive shared-memory wavefronts from approximately **32% to 3%** in the profiled kernel.

#### Softmax

The best register-cached implementation achieved:

- **27.0 billion elements/second**
- approximately **1.71×** the throughput of the naive implementation

I also implemented a warp-shuffle version that turned out to be slower. I kept it in the repository because it demonstrates an important engineering principle: a theoretically more sophisticated optimization still needs to be validated empirically.

---

## Machine Learning & Applied Data Systems

### 🔄 Churn & Reactivation Engine
**Python · SQL · scikit-learn · Feature Engineering · Temporal Validation**

[View repository](https://github.com/hajarmrifag/churn-reactivation-engine)

A banking disengagement prediction pipeline built from **1M+ historical transaction records**.

The project includes:

- temporal feature engineering
- leakage-aware evaluation
- purged temporal validation
- customer risk segmentation
- intervention targeting
- economic evaluation

The stricter purged evaluation achieved a **6.63× top-decile lift**.

---

### 🔎 FinSight
**Python · Streamlit · MiniLM Embeddings · Search · Applied ML**

[View repository](https://github.com/hajarmrifag/finsight-streamlit)<br>
[Live demo](https://finsight-ai-hajar.streamlit.app/)

An interactive application built around my banking disengagement research.

It combines:
- reproduced model results
- cohort analytics
- semantic evidence search using MiniLM embeddings
- campaign scenario analysis
- responsible-AI documentation
- automated testing with GitHub Actions

FinSight turns the underlying research pipeline into an application that non-technical users can explore.

---

## Technologies

### Languages
`Python` · `TypeScript` · `C#` · `C++` · `SQL` · `JavaScript` · `Bash`

### Frontend
`React` · `TanStack Query` · `React Hook Form` · `Zod` · `Playwright`

### Backend & APIs
`FastAPI` · `ASP.NET Core` · `Entity Framework Core` · `REST APIs`

### Databases & Data Systems
`PostgreSQL` · `SQL Server` · `SQLite` · `Hadoop HDFS` · `Apache Hive` · `PySpark`

### Infrastructure & Engineering
`AWS EC2` · `Docker` · `Docker Compose` · `GitHub Actions` · `CI/CD` · `Git` · `Linux/macOS`

### Data & Machine Learning
`pandas` · `NumPy` · `scikit-learn` · `Streamlit`

### Performance Engineering
`CUDA C++` · `CMake` · `NVIDIA Nsight Compute`

---

## What I'm interested in

I'm particularly interested in:

- backend and full-stack software engineering
- cloud-native application development
- distributed systems
- developer infrastructure and DevOps
- data-intensive applications
- performance engineering
- applied AI systems that solve real product problems

I enjoy understanding not only **how to make something work**, but also why a particular architecture or implementation is appropriate, what its trade-offs are, and how it behaves under real engineering constraints.

---

## Currently

- Completing my Software Engineering degree at Sichuan University
- Building production-style backend and full-stack projects
- Expanding my cloud and infrastructure-as-code experience
- Looking for international software engineering opportunities for 2027

---

## Connect

[LinkedIn](https://www.linkedin.com/in/hajar-mrifag-a7903334b)
