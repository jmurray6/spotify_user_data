#!/usr/bin/env bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source .venv/bin/activate
python3 ${SCRIPT_DIR}/../src/main.py