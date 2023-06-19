#!/bin/bash
echo "start test case on"

browserstack-sdk pytest -s --html=reports/report.html --end_point=$1 testCase/test_Cpl.py
#"--end_point=${endpoint}"