#!/usr/bin/env bash
set -euo pipefail

BASE="$HOME/python-neo4j"
NEO_PASSWORD="${ORG_GRAPH_NEO_PASSWORD}"

mkdir -p "${BASE}/neo4j/"{data,logs,import,plugins}


docker run \
    --name neo4j-backend \
    -p7474:7474 -p7687:7687 \
    -d \
    -v "$BASE/neo4j/data:/data" \
    -v "$BASE/neo4j/logs:/logs" \
    -v "$BASE/neo4j/import:/var/lib/neo4j/import" \
    -v "$BASE/neo4j/plugins:/plugins" \
    --env NEO4J_AUTH=neo4j/test \
    --user="$(id -u)":"$(id -g)" \
    --env NEO4J_AUTH=neo4j/"${NEO_PASSWORD}" \
    neo4j:3.5
