#!/usr/bin/env bash

# activate virtual environment

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
REQUIREMENTS_FILE=${SCRIPT_DIR}/../requirements.txt

python3 -m venv .venv
source .venv/bin/activate

pip3 install -r ${REQUIREMENTS_FILE}