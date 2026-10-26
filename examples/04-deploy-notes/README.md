# 04 — Deployment notes from the fleet's Compose deployments

> **Design-only, gate 1 target** — drafted from fleet evidence, not runtime-validated. Verify against your own stack before adopting it.

How Airflow runs on the fleet, and what to check when it doesn't. This pattern corrects the seed's stale wording: Node-1 and Node-3 Airflow are Docker Compose deployments, not kind-cluster deployments (kind is the Airbyte route).

## Fleet deployment map (verified evidence)

| Item | Node-1 | Node-3 |
|---|---|---|
| Route | Docker Compose | Docker Compose |
| Compose file dir | `C:\docker-stacks\airflow` | (path to confirm at validation) |
| Images | `apache/airflow:2.10.5`, `postgres:13`, `redis:7.2-bookworm` | (to confirm at validation) |
| Web UI port | 18084 | 18084 |
| Services | 6: webserver, scheduler, triggerer, worker, postgres, redis | (to confirm at validation) |
| Flower | Profile-gated, NOT started | (to confirm at validation) |
| Firewall rule | "ZQM Airflow 18084" (tailnet+LAN) | (to confirm at validation) |

## Health checks (run these, in order)

```bash
# 1. The service answers (fleet-verified 200 on Node-1 after the Docker restart):
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:18084/health

# 2. Container states (all six expected Up; see the discrepancy note below):
docker compose -f C:\docker-stacks\airflow\docker-compose.yml ps
```

## Known fleet behaviors (do not "fix" these without evidence)

- **Triggerer + worker show `(unhealthy)` flags while `/health` answers 200.** This is a healthcheck-level discrepancy observed on Node-1, not a service outage. Treat the HTTP answer as the service signal and the flags as a healthcheck investigation item.
- **Admin credentials are Alex's to change.** This pattern uses placeholders only (`<ADMIN_USER>` / `<ADMIN_PASSWORD>`); it never states, uses, or endorses any default pair, and no pattern in this repo logs in as admin.
- **Flower is off by design** (profile-gated). Starting it changes the port and process footprint; that is a separate decision, not part of this pattern.

## Failure behavior

- If `/health` fails but containers are Up, suspect the Docker engine, not Airflow: Node-1's engine wedged in October 2026 and took all published-port traffic down with it. Check `docker ps` health before debugging Airflow.
- If the webserver answers but DAGs are missing, check the DAGs-folder volume mapping in the Compose file before touching DAG code.

## To confirm at validation

- Node-3's Compose directory, image tags, service list, and firewall rule (all unconfirmed in the record used here).
- The exact healthcheck commands behind the triggerer/worker `(unhealthy)` flags.
- Whether the fleet's scheduler honors per-DAG `catchup=False` without a config override.
