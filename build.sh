#!/bin/bash

echo "Installing libraries"
pip3 install -r requirements.txt

echo "Running tests"
#Run tests
python3 -m pytest unit_test_movie_catalog.py

echo "Tests passed"