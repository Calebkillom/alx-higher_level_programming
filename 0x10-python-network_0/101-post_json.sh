#!/bin/bash
Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d '{"key":"value"}' "$1" -D - | awk '/Content-Length/ {print $2}'
