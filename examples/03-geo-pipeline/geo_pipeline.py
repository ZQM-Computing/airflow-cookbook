"""geo_ingest_publish: ingest -> transform -> publish (gated).

Design-only example. Synthetic data only. The publish stage writes a local
summary file and logs a placeholder destination — it performs no real push.
"""
import json
from datetime import datetime, timedelta
from pathlib import Path

from airflow.decorators import dag, task

DATA = Path(__file__).with_name("points.geojson")
# Synthetic bbox filter (lon/lat). Only points inside are kept.
BBOX = (-80.905, 28.945, -80.885, 28.965)
# Placeholder destination: replace with a real, credentialed target only
# after an admin decision. This pattern never pushes anywhere.
PUBLISH_DESTINATION = "https://example.invalid/geoserver/rest/workspaces/demo"


@dag(
    dag_id="geo_ingest_publish",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=10),
    },
    tags=["example", "geospatial"],
)
def geo_ingest_publish():
    @task
    def ingest():
        """Read the synthetic GeoJSON file and return its features."""
        with DATA.open(encoding="utf-8") as f:
            doc = json.load(f)
        return doc["features"]

    @task
    def transform(features):
        """Keep features inside BBOX; summarize count, bbox, and CRS note."""
        kept = []
        for feat in features:
            lon, lat = feat["geometry"]["coordinates"]
            if BBOX[0] <= lon <= BBOX[2] and BBOX[1] <= lat <= BBOX[3]:
                kept.append(feat)
        lons = [f["geometry"]["coordinates"][0] for f in kept]
        lats = [f["geometry"]["coordinates"][1] for f in kept]
        return {
            "ingested": len(features),
            "kept": len(kept),
            "bbox": [min(lons), min(lats), max(lons), max(lats)] if kept else None,
            "crs_note": "Input assumed EPSG:4326; reprojection is a validation exercise.",
        }

    @task
    def publish(summary):
        """Write the summary locally; log (do not push to) the destination."""
        out = Path("/tmp/geo_summary.json")
        out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print(f"Wrote summary to {out}")
        print(f"Would-be destination (NOT pushed): {PUBLISH_DESTINATION}")
        print(f"Summary: {summary}")

    publish(transform(ingest()))


geo_ingest_publish()
