#!/usr/bin/python3
"""Python code that check intranet status"""


import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    status = response.read()
    decode_response = status.decode('utf-8')
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: \
{}".format(type(status), status, decode_response))
