#!/bin/bash

echo "Installing libraries"
pip install -r requirements.txt

echo "Running tests"
#Run tests
pytest unit_test_movie_catalog.py > test_result.txt

#Check tests result
if grep -q "FAILED" test_result.txt; then
    echo "Build failed: Some tests did not pass."
    exit 1
else
    echo "Build successful: All tests passed."
    exit 0
fi