#!/bin/bash
# script takes URL and displays HTTP methods the server accepts
curl -sI "$1" | grep -i "Allow:" | cut -d ' ' -f2-
