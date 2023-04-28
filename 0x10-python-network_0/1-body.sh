#!bin/bash
# script takes URL, sends a GET request , and displays the body

url="$1"

curl -s -o /dev/null -w "%{http_code}\n" "$url" | {
    read status_code
    if [ "$status_code" -eq 200 ]; then
        curl -s "$url" | tr -d '\r'
    fi
}
