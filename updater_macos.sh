#!/bin/bash

# Check if the current directory is a Git repository
if [ ! -d .git ]; then
  osascript -e 'display dialog "This directory is not a Git repository. Please run this script in a Git repository." buttons {"OK"} default button "OK"'
  exit 1
fi

# Update the local repository with the latest changes
git pull origin main --rebase

# Check if the pull was successful
if [ $? -eq 0 ]; then
    osascript -e 'display dialog "Git pull successful." buttons {"OK"} default button "OK"'
else
    osascript -e 'display dialog "Failed to update the Git repository." buttons {"OK"} default button "OK"'
    exit 1
fi
