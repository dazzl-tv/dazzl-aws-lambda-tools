#!/bin/bash

files=("bucket.py" "environment.py" "headers.py" "logger.py" "parameters.py")
codes=()

function run_test {
  echo "Number of file tested : ${#files[*]}\r\n"
  for ix in ${!files[*]}
  do
    test_file ${files[$ix]} $ix
  done
}

function test_file {
  echo "## Test $1 class"
  python3 $1
  codes[$2]=$?
  echo
}

function exit_with_status {
  for ix in ${!files[*]}
  do
    if [ ${codes[$ix]} == 1 ]; then
      echo "Error in test for file ${files[$ix]}"
      exit ${codes[$ix]}
    fi
  done
}

echo 'Get lib folder ...'
cd dazzl_aws_lambda_tools
run_test
exit_with_status
