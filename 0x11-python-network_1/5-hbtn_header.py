#!/usr/bin/python3
""" takes a URL, sends a request and returns"""


import requests
import sys

if __name__ == '__main__':
    req_get = requests.get(sys.argv[1])
    print("{}".format(req_get.headers.get('X-Request-Id')))
