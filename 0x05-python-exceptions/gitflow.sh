#!/bin/bash

#this script is for my git flow - add, commit , push


git add .
git status
read -p "enter commit message:
" message
git commit -m "$message" 
git push
