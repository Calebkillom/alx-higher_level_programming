#!/bin/bash
# script takes URL, sends a POST request and displays the body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
