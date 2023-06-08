#!/bin/bash
echo "start test case"
browserstack-sdk pytest -s --end_point="${endpoint}" testCase/test_Cpl.py