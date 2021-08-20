#!/usr/bin/python3
"""Python script that post an email"""


import requests
import sys

if __name__ == '__main__':
    email_value = {'email': sys.argv[2]}
    email_r = requests.post(sys.argv[1], data=email_value)
    print("{}".format(email_r.text))
