#!/bin/bash
# bash script to send POST request to URL and display body
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
