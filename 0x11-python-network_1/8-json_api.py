#!/usr/bin/python3
""" Script that takes in a letter and send it """


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    values = {'q': q}
    request = requests.post('http://0.0.0.0:5000/search_user', data=values)
    try:
        response = request.json()
        if response:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
