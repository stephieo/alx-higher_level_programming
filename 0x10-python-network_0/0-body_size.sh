#!/bin/bash
# bash script to send request to URL and displays body size
curl -s -o/dev/null -w "%{size_download}\n"  "$1"
