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

An Airflow cookbook for DAGs, schedules, retries, and geospatial pipeline patterns. It is intended for data engineers who orchestrate geospatial or scientific workflows. Examples use synthetic data and avoid writing to external services by default.

## Repository role and maturity

**Status:** Examples Present — design patterns documented; full Airflow runtime validation remains pending.

This repository is part of the ZQM Computing geospatial portfolio. The series index is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

Automated checks only cover the paths and environments configured in this repository. Written examples and successful static checks do not establish production readiness, deployment compatibility, or operational certification.

## Intended audience

Data engineers who schedule geospatial pipelines as Airflow DAGs, especially readers who need examples of task dependencies, retries, schedules, backfills, and safe synthetic-data workflows.

## Prerequisites

- Apache Airflow **2.10.5** is the documented reference version for the fleet examples; validate compatibility before using a different version.
- Python **3.11+** for local tooling. The Python version inside the referenced Airflow container has not yet been independently confirmed.
- Docker Compose if running Airflow in containers.
- Postgres or DuckDB only if adapting a pattern to a real destination; the examples do not require either service to demonstrate their core logic.
- A disposable local Airflow environment for DAG-import and task-run validation. Do not validate experimental DAG changes directly against production.

## Examples

| # | Example | Maturity | What it demonstrates |
|---|---------|---------|----------------------|
| 01 | [First DAG](examples/01-first-dag/README.md) | Written; runtime validation pending | Task dependencies, retries, and XCom |
| 02 | [Schedules](examples/02-schedules/README.md) | Written; runtime validation pending | Schedule decisions, catchup, and backfills |
| 03 | [Geospatial pipeline](examples/03-geo-pipeline/README.md) | Written; runtime validation pending | Synthetic GeoJSON ingest, transform, and local summary output |
| 04 | [Deployment notes](examples/04-deploy-notes/README.md) | Documentation; runtime validation pending | Deployment observations and validation caveats |

## Repository layout

```text
airflow-cookbook/
├── examples/01-first-dag/
├── examples/02-schedules/
├── examples/03-geo-pipeline/
├── examples/04-deploy-notes/
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

## Validate locally

The documented fleet reference is Airflow 2.10.5 via Docker Compose; the repository does not currently claim that these commands have been run successfully against that fleet.

1. Review the example README for its assumptions and expected behavior.
2. In a disposable environment using your target Airflow version, place the DAG in the configured DAGs folder.
3. Check DAG discovery and import errors:

   ```bash
   airflow dags list
   airflow dags list-import-errors
   ```

4. Run the individual example's documented trigger/task commands and inspect task logs.
5. Confirm that output paths are writable and that no placeholder destination is mistaken for a real integration.

For a local syntax-only check, compile the DAG Python files with the Python interpreter used by your target Airflow environment. Syntax checks do not prove that Airflow can import or execute the DAG.

## What this does not claim

- The examples are not certified for production deployment.
- The documented Node-1/Node-3 fleet configuration is not a substitute for independently reproducing the environment.
- A placeholder publish destination does not upload data to GeoServer, PostGIS, or another service.
- A successful DAG parse does not prove data correctness, idempotence, access control, alerting, recovery, or production performance.
- No real geospatial or participant data is included; synthetic examples must be adapted and reviewed before use with real datasets.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for scope, validation expectations, and safe contribution practices. Report security issues privately to zqmcomputing@gmail.com; do not publish exploitable details in a public issue.

## Related patterns

- [Prefect Cookbook](https://github.com/ZQM-Computing/prefect-cookbook) — workflow orchestration, schedules, and deployments.
- [dlt Cookbook](https://github.com/ZQM-Computing/dlt-cookbook) — ELT pipelines from Python into Postgres and DuckDB.
- [NiFi Cookbook](https://github.com/ZQM-Computing/nifi-cookbook) — visual dataflow, ingestion, and feed-to-PostGIS pipelines.

---

Part of the [ZQM Computing geospatial cookbook portfolio](https://github.com/ZQM-Computing/geospatial-cookbooks).
