# Airflow Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **Airflow cookbook** — DAGs, schedules, and geospatial pipelines. Airflow is verified live on Node-1 and Node-3 from the Docker sets (both via Docker Compose on port 18084). Patterns are drawn from those deployments. It is intended for Data engineers who schedule geospatial pipelines as DAGs. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — first pattern pass written (design-only, gate 1 target; runtime validation pending).

**What this repository is:** Airflow patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Data engineers who schedule geospatial pipelines as DAGs.

## Prerequisites

- Airflow via Docker Compose
- Python 3.11+
- Postgres or DuckDB as a pipeline destination

## Patterns

| # | Example | Status | What it demonstrates |
|---|---------|--------|----------------------|
| 01 | [01-first-dag](examples/01-first-dag/README.md) | Written | A first DAG: tasks, dependencies, and retries |
| 02 | [02-schedules](examples/02-schedules/README.md) | Written | Schedules, catchup, and backfills |
| 03 | [03-geo-pipeline](examples/03-geo-pipeline/README.md) | Written | A geospatial DAG: ingest → transform → publish |
| 04 | [04-deploy-notes](examples/04-deploy-notes/README.md) | Written | Deployment notes from the fleet's Compose deployments (Node-1/Node-3 :18084) |

## Repository layout

```text
airflow-cookbook/
├── examples/01-first-dag/
├── examples/02-schedules/
├── examples/03-geo-pipeline/
├── examples/04-deploy-notes/
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: the first two table rows
- Second pass: the remaining rows, from fleet-verified setups

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [prefect-cookbook](https://github.com/ZQM-Computing/prefect-cookbook) — Workflow orchestration, schedules, and deployments
- [dlt-cookbook](https://github.com/ZQM-Computing/dlt-cookbook) — ELT pipelines from Python into Postgres and DuckDB
- [nifi-cookbook](https://github.com/ZQM-Computing/nifi-cookbook) — Visual dataflow, ingestion, and feed-to-PostGIS pipelines

