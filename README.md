# Hajar Mrifag

Final-year **Software Engineering student at Sichuan University**, graduating in **June 2027** and planning to relocate to London. My interests are backend systems, algorithms and performance engineering.

[Portfolio and case studies](https://hajarmrifag.github.io/) · [LinkedIn](https://www.linkedin.com/in/hajar-mrifag-a7903334b/)

My degree includes Java/OOP, data structures, operating systems, architecture, networking and distributed systems. My projects also use C++/CUDA, Python, SQL, C# and TypeScript. I focus on clear constraints, tested behaviour and measurements with explicit limits.

## Selected engineering work

### CUDA Transformer Kernels — profiling and memory locality

[Source and recorded results](https://github.com/hajarmrifag/cuda-transformer-kernels)

FP32 GEMM and row-wise Softmax implementations with shared-memory/register tiling and alternative reductions. A historical Tesla T4 run recorded **1.28 TFLOPS at 1024 × 1024**, 3.31× a naive kernel and 24% of cuBLAS. Register caching recorded 1.71× baseline Softmax throughput at width 2048; the slower warp-shuffle experiment remains documented.

Finite-output comparisons, explicit width contracts and CPU regressions improve validation. GPU-specific regression tests are provided separately; the latest validation changes have not been rerun on a GPU. Kernel measurements exclude application/network overhead.

### Java Order Book — algorithms and JVM measurement

[Source, tests and benchmarks](https://github.com/hajarmrifag/java-order-book)

A compact Java 21 single-writer limit-order matching engine: integer ticks, price-time priority, cancellation and deterministic full/partial fills. Tests compare 60,000 generated commands against an independent list-based reference model. JMH records throughput, sampled batch durations and allocation with explicit warm-up/forks. This is an educational simulation, not production exchange infrastructure.

### GridFlex — numerical correctness and optimization

[Application](https://gridflex.onrender.com/) · [Case study](https://hajarmrifag.github.io/work/gridflex.html) · [Source](https://github.com/hajarmrifag/gridflex-ai)

A React/FastAPI workspace around an energy-simulation engine, with **91 Python tests**, numerical invariants, bounded computation and browser/container CI. Removing repeated pandas indexing produced a historical **31.9×** improvement in a 60-day shift-and-battery workload, with identical outputs in the compared case. That is an engine measurement, not whole-app latency. Benchmark records now retain raw samples, randomized paired order and source/environment metadata.

### Neobank Transaction API — concurrency and reliability

[Source and transaction design](https://github.com/hajarmrifag/neobank-growth-analytics)

Simulated PostgreSQL transfers with integer money, atomic debit/credit, consistent account-lock order and idempotency-key serialization. **37 local tests** cover analytics plus real-database API behaviour, including concurrent spending, retry conflicts and injected-failure rollback. Query-plan measurements remain explicitly database-only. The separate analytics dataset contains 891,772 synthetic transactions.

### Aegis Claims — layered backend and authorization

[Application](https://claims-management-ync9.onrender.com) · [Source](https://github.com/hajarmrifag/claims-management-api)

React/ASP.NET Core application with JWT authentication, API-enforced roles, status-history records and validated uploads. **22 local backend tests** cover domain/application rules, HTTP flows and real PostgreSQL constraints/rollback. Defined-status validation is distinct from a lifecycle state machine. Deployment and authorization limitations remain documented.

## Team experience

[SkyQuery internship project](https://github.com/maryamibaaichou/Flight-Ticket-Meta-Search-and-Analysis/tree/master): backend/data engineering in a two-person project documented around 15 million Expedia records. The PySpark/HDFS/Hive batch workflow is separate from the FastAPI/SQLite conversational prototype. My teammate owned the frontend and contributed analysis.

[Churn & Reactivation Engine](https://github.com/hajarmrifag/churn-reactivation-engine) and [FinSight](https://github.com/hajarmrifag/finsight-streamlit) contain additional work on temporal banking research and its evidence-review interface.

Based in Chengdu, China · Seeking graduate software engineering roles for 2027.

*Free-hosted demonstrations may take time to wake. Source, tests and benchmark conditions are the primary engineering evidence.*
