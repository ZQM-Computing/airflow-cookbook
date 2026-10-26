"""hello_geo: a first Airflow DAG (extract -> transform -> load).

Design-only example. Synthetic points only; no external service is called.
Uses the Airflow 2.x TaskFlow API so task return values pass as objects
(plain op_args templating would pass rendered strings, not values).
"""
from datetime import datetime, timedelta

from airflow.decorators import dag, task


@dag(
    dag_id="hello_geo",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
    },
    tags=["example", "geospatial"],
)
def hello_geo():
    @task
    def extract():
        """Return 5 synthetic points (lon, lat) around a small synthetic area."""
        return [
            (-80.90, 28.95),
            (-80.89, 28.96),
            (-80.88, 28.95),
            (-80.90, 28.94),
            (-80.89, 28.94),
        ]

    @task
    def transform(points):
        """Compute a bbox and a count from the extracted points."""
        lons = [p[0] for p in points]
        lats = [p[1] for p in points]
        return {
            "count": len(points),
            "bbox": [min(lons), min(lats), max(lons), max(lats)],
        }

    @task
    def load(summary):
        """Print the summary (a real pipeline would write it to a destination)."""
        print(f"Loaded {summary['count']} points, bbox={summary['bbox']}")

    load(transform(extract()))


hello_geo()
