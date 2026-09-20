#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if [[ "${1:-cli}" == "gui" ]]; then
  exec mvn javafx:run
fi
exec mvn compile exec:java -Dexec.mainClass=GridManagerCore.main.GridSystem
