#!/usr/bin/python3
"""Script that takes our Github credentials"""


import requests
import sys
from request.auth import HTTPBasicAuth

if __name__ == '__main__':
    response = requests.get('https://api.github.com/users',
                            auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    if response.status_code == 200:
        dictionary = response.json()
        print(dictionary['id'])
    else:
        print(None)
