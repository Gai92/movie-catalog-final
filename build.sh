#!/bin/bash

echo "Installing libraries"
pip3 install -r requirements.txt

echo "Running tests"
#Run tests
python3 -m pytest
RESULT=$?

if [ $RESULT -ne 0 ]; then
  echo "Build failed: Some tests did not pass."
  exit 1
else
  echo "Build successful: All tests passed."
  exit 0
fi