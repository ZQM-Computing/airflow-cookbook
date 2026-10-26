# 01 — First DAG: tasks, dependencies, and retries

> **Design-only, gate 1 target** — drafted from fleet evidence, not runtime-validated. Run it against your own Airflow before adopting it.

A minimal DAG with three tasks in a chain: extract synthetic points → transform (bbox + count) → load (print a summary). It demonstrates task dependencies, retries, and XCom return values without any external service.

## Files

- `first_dag.py` — the DAG definition (drop into your DAGs folder).

## Run

```bash
airflow dags list | grep hello_geo
airflow dags trigger hello_geo
airflow tasks list hello_geo
```

## Expected output (stated, not yet run against the fleet)

- All three tasks end `success`; the transform task logs a bbox and a count of 5 points.
- The load task logs a one-line summary naming the point count and bbox.
- If a task fails transiently, Airflow retries it up to 2 times with a 5-minute delay before marking it failed.

## Versions note

- Fleet evidence: Airflow 2.10.5 via Docker Compose (images `apache/airflow:2.10.5`, `postgres:13`, `redis:7.2-bookworm`), web UI on :18084 (Node-1 and Node-3).
- DAG code uses the Airflow 2.x `schedule` spelling.

## Failure behavior

- A task that exhausts its retries marks the DAG run failed; downstream tasks do not run (default `trigger_rule=all_success`).
- A missing DAGs-folder mount shows the DAG as absent from `airflow dags list` — check the compose volume mapping, not the DAG code, first.

## To confirm at validation

- Exact 2.10.5 behavior of `schedule=None` vs the legacy `schedule_interval` spelling.
- The container's Python version (host Node-1 Python is 3.12.10; the image's Python is unconfirmed).
- Whether the fleet's Flower profile stays gated off (it was profile-gated, not started, in the Node-1 Compose stack).
