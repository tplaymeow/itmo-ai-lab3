#!/bin/sh

OUTPUT=$(python3 main.py monopoly.pl < test_requests.txt)
EXPECTED_OUTPUT=$(cat test_responses.txt)
if [ "$OUTPUT" == "$EXPECTED_OUTPUT" ]
then
  echo "Tests OK"
else
  echo "Tests failed"
  exit 1
fi