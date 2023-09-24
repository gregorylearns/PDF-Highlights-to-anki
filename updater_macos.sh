#!/bin/bash

# Check if the current directory is a Git repository
if [ ! -d .git ]; then
  echo "This directory is not a Git repository. Please run this script in a Git repository."
  exit 1
fi

# Update the local repository with the latest changes
git pull origin master --rebase

# Check if the pull was successful
if [ $? -eq 0 ]; then
    echo "Git pull successful."
else
    echo "Failed to update the Git repository."
    exit 1
fi
