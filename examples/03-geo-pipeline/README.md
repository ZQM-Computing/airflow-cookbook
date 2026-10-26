# 03 — Geospatial DAG: ingest → transform → publish

> **Design-only, gate 1 target** — drafted from fleet evidence, not runtime-validated. Run it against your own Airflow before adopting it.

A three-stage geospatial pipeline DAG: ingest a synthetic GeoJSON file, transform it (filter + reproject-note + summary), and publish a summary document. The publish stage is gated: it writes a local summary file and prints the destination it *would* push to, so the pattern is safe to run anywhere.

## Files

- `geo_pipeline.py` — the DAG definition.
- `points.geojson` — 5 synthetic points (no real place, no real data).

## Run

```bash
airflow dags trigger geo_ingest_publish
```

## Expected output (stated, not yet run against the fleet)

- Ingest reads 5 features from `points.geojson`.
- Transform keeps the 2 features inside the synthetic bbox (points 1 and 2; point 3 falls east of the bbox, points 4 and 5 fall outside it) and writes a summary: kept count 2, bbox [-80.90, 28.95, -80.89, 28.96], and the output CRS note.
- Publish writes `summary.json` next to the DAG run's working directory and logs the would-be destination URL (a placeholder — no real push happens).

## Versions note

- Fleet evidence: Airflow 2.10.5 via Docker Compose on :18084 (Node-1 and Node-3).
- The transform uses only the standard library (no geopandas dependency) so the DAG runs on a bare Airflow image; swapping in geopandas is a validation exercise, not assumed here.

## Failure behavior

- A malformed GeoJSON file fails ingest fast with a JSON error — the DAG does not produce a partial summary.
- The publish stage never runs if transform fails (default `all_success` trigger rule), so no stale summary is published.
- The publish destination is a placeholder by design: wiring a real GeoServer/PostGIS push requires credentials and an admin decision, neither of which this pattern assumes.

## To confirm at validation

- The fleet's preferred destination for published summaries (PostGIS table vs object storage vs GeoServer layer) — the pattern deliberately does not choose.
- Whether the fleet's Airflow image carries geopandas/shapely (unconfirmed; the pattern avoids the dependency).
- DAG-file placement in the fleet's Compose volume mapping (DAGs folder path on Node-1/Node-3).
