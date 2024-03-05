#!/bin/bash
# bash script to send POST request to URL and display body
curl -s -H "Content_Type: application/json" -d "$(cat "$2")" "$1"
