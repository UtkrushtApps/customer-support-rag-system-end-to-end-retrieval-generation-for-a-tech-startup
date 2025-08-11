#!/usr/bin/env bash

set -euo pipefail

if ! command -v docker > /dev/null || ! command -v docker-compose > /dev/null; then
    echo "Error: Docker and docker-compose must be installed and available in PATH." >&2
    exit 1
fi

docker-compose down

if [ "${1:-}" == "--fresh" ]; then
    docker volume rm chroma_data || true
fi

docker-compose up -d chroma-db

for i in {1..30}; do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/api/v1 || echo 000)
    if [ "$STATUS" = "200" ]; then
        echo "Chroma DB is up and running at http://localhost:8000"
        exit 0
    fi
    sleep 2
done

echo "Chroma DB failed to start or is not healthy." >&2
exit 2
