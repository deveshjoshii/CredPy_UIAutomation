#!/bin/bash
echo "start test case"
browserstack-sdk pytest -s --endpoint=$1 testCase/test_Cpl.py
#"--end_point=${endpoint}"