#!/bin/bash
echo "start test case on"

browserstack-sdk pytest -s -m smoke --html=reports/report.html --end_point=$1 testCase
#"--end_point=${endpoint}"