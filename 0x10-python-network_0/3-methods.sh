#!/bin/bash
# bash script to  display all methods available to given URL
curl -sI "$1" | grep "Allow"  | cut -d " " -f 2-
