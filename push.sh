#!/bin/bash
date=$(date +%Y-%m-%d)
FILE=./test
if [ -f "$FILE" ];then
    rm "$FILE"
fi
git add .
git commit -m ${date}
git push