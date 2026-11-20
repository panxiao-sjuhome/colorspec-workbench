#!/bin/zsh
set -e
cd "$(dirname "$0")"
PORT=8876
while lsof -nP -iTCP:$PORT -sTCP:LISTEN >/dev/null 2>&1; do PORT=$((PORT+1)); done
printf '色准工作台已启动： http://127.0.0.1:%s/\n' "$PORT"
python3 -m http.server "$PORT"
