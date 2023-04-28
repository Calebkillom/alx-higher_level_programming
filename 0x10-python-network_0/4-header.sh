#!/bin/bash
# script that takes URL,  sends GET request, displays the body
curl -s -H "X-School-User-Id: 98" "$1"
