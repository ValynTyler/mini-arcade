#!bin/bash

DIR=$(dirname "$0")

python -m venv $DIR/.venv
source $DIR/.venv/bin/activate

pip install -r $DIR/requirements.txt

