# 02 — Schedules, catchup, and backfills

> **Design-only, gate 1 target** — drafted from fleet evidence, not runtime-validated. Run it against your own Airflow before adopting it.

A daily DAG that shows the three schedule decisions every pipeline needs: the schedule itself, what happens to missed intervals (catchup), and how to fill history (backfill).

## Files

- `schedule_dag.py` — a daily DAG with `catchup=False` and one backfill-safe task.

## Run

```bash
# A daily run appears each morning; nothing backfills for missed days.
airflow dags list | grep daily_geo_summary

# Fill a missed window explicitly (dates are examples, not fleet dates):
airflow dags backfill daily_geo_summary \
  --start-date 2026-01-05 --end-date 2026-01-07
```

## Expected output (stated, not yet run against the fleet)

- With `catchup=False`, enabling the DAG creates only the next scheduled run, not one per missed interval since `start_date`.
- The backfill command creates exactly one run per day in the requested window, each marked with its logical date.
- The task logs its logical date, so a backfilled run's output is distinguishable from a live run's.

## Versions note

- Fleet evidence: Airflow 2.10.5 via Docker Compose on :18084 (Node-1 and Node-3).
- The DAG uses the Airflow 2.x `schedule="@daily"` spelling; the legacy `schedule_interval` spelling is a validation item, not asserted here.

## Failure behavior

- `catchup=True` (the default if you omit it) on a DAG with an old `start_date` creates a run per missed interval — the classic surprise. Set it explicitly, every time.
- A backfill against a destination without idempotent writes double-loads data. The example task is read-only (it logs); a real backfill task must write idempotently (keyed upserts, not blind appends).

## To confirm at validation

- Exact 2.10.5 `airflow dags backfill` flags (the command's options moved across 2.x releases).
- Cron vs preset (`@daily`) timetable behavior on the fleet's timezone setting.
- Whether the fleet's scheduler honors the DAG's `catchup=False` without a config override.
