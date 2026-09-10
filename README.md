# Hi, I'm Hajar 👋

I'm a final-year **Software Engineering student at Sichuan University** building backend, distributed, data-intensive, and performance-oriented software systems.

I enjoy working on problems that go beyond basic CRUD: API design, authentication and authorization, database performance, distributed data processing, containerization, CI/CD, testing, and low-level performance optimization.

My recent work spans **Python/FastAPI, C#/.NET, PostgreSQL, SQL Server, Docker, Hadoop/Spark, and CUDA C++**.

---

## Featured Engineering Projects

### 🛡️ Claims Management API
**C# · ASP.NET Core · Entity Framework Core · SQL Server · JWT · GitHub Actions · Azure Blob Storage**

[View repository](https://github.com/hajarmrifag/claims-management-api)

A production-style insurance claims backend designed around layered architecture and clear separation of concerns.

**Engineering highlights:**
- Built a multi-layer .NET architecture across Domain, Application, Infrastructure, and API projects
- Implemented JWT authentication with secure password hashing
- Added role-based authorization for Adjuster, Manager, and Admin workflows
- Designed auditable claim status transitions and claim history
- Added authenticated document upload and download
- Abstracted file storage to support both local storage and Azure Blob Storage
- Added centralized exception handling and structured request logging
- Implemented EF Core migrations, relationships, unique constraints, and query-oriented indexes
- Added unit and end-to-end HTTP integration tests
- Automated restore, build, and test validation with GitHub Actions

This project focuses on backend architecture, security, persistence, testing, observability, and maintainable service boundaries.

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
`Python` · `C#` · `C++` · `SQL` · `JavaScript` · `Bash`

### Backend & APIs
`FastAPI` · `ASP.NET Core` · `Entity Framework Core` · `REST APIs`

### Databases & Data Systems
`PostgreSQL` · `SQL Server` · `SQLite` · `Hadoop HDFS` · `Apache Hive` · `PySpark`

### Infrastructure & Engineering
`Docker` · `Docker Compose` · `GitHub Actions` · `CI/CD` · `Git` · `Linux/macOS`

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
