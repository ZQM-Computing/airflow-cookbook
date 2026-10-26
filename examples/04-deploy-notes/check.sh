#!/bin/bash
# Fleet Airflow health check (Node-1/Node-3 Compose deployments, port 18084).
# Usage: check.sh [host]  (default host: localhost)
# Exits 0 only when /health answers 200. Placeholders only; no credentials.
set -u
HOST="${1:-localhost}"
CODE=$(curl -s -o /dev/null -w "%{http_code}" "http://${HOST}:18084/health" || echo "000")
echo "Airflow /health on ${HOST}:18084 -> HTTP ${CODE}"
if [ "$CODE" = "200" ]; then
  echo "OK: service answers"
  exit 0
else
  echo "NOT-OK: check 'docker compose ps' in the Airflow stack dir, then the Docker engine itself"
  exit 1
fi
