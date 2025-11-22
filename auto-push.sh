#!/bin/bash

# Go to your repo directory
cd /Users/jeremycabrera/Desktop/dsa-practice

# Load environment so cron can use Git + SSH correctly
source ~/.bashrc 2>/dev/null
source ~/.zshrc 2>/dev/null

# Check for changes
if [[ $(git status --porcelain) ]]; then
    git add .
    git commit -m "Auto-update on $(date)"
    git push
fi

