#!/usr/bin/python3
"""
Python script that takes in a URL,
and sends a request to the URL and displays the value of the X-Request-Id
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req_st = urllib.request.Request(url)

    with urllib.request.urlopen(req_st) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
