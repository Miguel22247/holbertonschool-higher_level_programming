#!/usr/bin/python3
"""script that fetches"""


import requests
if __name__ == "__main__":
    request = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(request.text), request.text))
