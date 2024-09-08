#!/bin/bash

set -e

echo "----------------------------------------------------------------------"
# Add comma separated errors to ignore by Flake8
# Example: E501,E502 or empty
ERRORS_TO_IGNORE=E501

echo "Running flake8 for code linting..."
flake8 --ignore="${ERRORS_TO_IGNORE}" totara/
STATUS=$?
if [ $STATUS -eq 0 ]; then
  echo "No linting errors found..."
fi
echo "----------------------------------------------------------------------"
printf "\n"

echo "Running mock & unit tests..."
python -m unittest discover -s tests

echo "----------------------------------------------------------------------"
