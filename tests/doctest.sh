#!/bin/bash

m=None,
name=None,
globs=None,
verbose=None,
report=True,
optionflags=0,
extraglobs=None,
raise_on_error=False,
exclude_empty=False

function test_file {
  echo "## Test $1 class"
  python3 $1
  echo ''
}

cd dazzl_aws_lambda_tools

test_file bucket.py
test_file environment.py
test_file headers.py
test_file logger.py
test_file parameters.py
