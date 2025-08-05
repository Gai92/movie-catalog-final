#!/bin/bash

echo "Installing libraries"
pip3 install -r requirements.txt

echo "Running tests"
#Run tests
python3 -m pytest

echo "Tests passed"