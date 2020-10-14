#!/bin/bash

# This script is for CI updates

BRANCH=gh-pages

# setup
git config user.email mnot@mnot.net
git config user.name mnot-bot
git remote set-url --push origin https://mnot:$GITHUB_TOKEN@github.com/httpwg/wg-materials
git checkout -B $BRANCH origin/$BRANCH

# Push the changes
git add .
git commit -m "update indices"
git push origin $BRANCH
