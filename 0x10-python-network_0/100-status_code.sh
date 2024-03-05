#!/bin/bash
# bash script to send request to URL and display response code
curl -s -o /dev/null -w "%{response_code}\n"  "$1"
