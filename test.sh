#!/bin/sh

OUTPUT=$(python3 main.py monopoly.pl < test_requests.txt)
EXPECTED_OUTPUT=$(cat test_responses.txt)
if [ "$OUTPUT" == "$EXPECTED_OUTPUT" ]
then
  echo 'Tests OK'
else
  >&2 echo 'Tests failed'
fi