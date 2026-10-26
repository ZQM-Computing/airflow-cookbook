"""daily_geo_summary: schedule, catchup, and backfill behavior.

Design-only example. The task is read-only (it logs its logical date) so
that backfills are safe to demonstrate; a real pipeline task must write
idempotently before it is ever backfilled.
"""
from datetime import datetime, timedelta

from airflow.decorators import dag, task


@dag(
    dag_id="daily_geo_summary",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=10),
    },
    tags=["example", "schedule"],
)
def daily_geo_summary():
    @task
    def summarize(ds=None):
        """Log the run's logical date (ds) so backfills are distinguishable."""
        print(f"Daily geo summary for logical date {ds}")

    summarize()


daily_geo_summary()
