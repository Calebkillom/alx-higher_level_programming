#!/usr/bin/python3
"""
Python script that takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""

    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response["id"], json_response["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
