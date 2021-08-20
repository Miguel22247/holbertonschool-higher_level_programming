#!/usr/bin/python3
"""script that takes a URL, send a request and returns"""


import requests
import sys

if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print("{}".format(request.text))
