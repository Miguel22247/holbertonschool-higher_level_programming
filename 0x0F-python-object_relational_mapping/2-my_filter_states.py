#!/usr/bin/python3
""" Script that lists all states starting with N"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    HOST = 'localhost'
    PORT = 3306
    MY_USER = argv[1]
    MY_PSWD = argv[2]
    MY_DB = argv[3]
    NAME = argv[4]
    db = MySQLdb.connect(host=HOST, user=MY_USER, password=MY_PSWD,
                         db=MY_DB, port=PORT)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(NAME)
    cur.execute(query)
    row_query = cur.fetchall()
    for rq_print in row_query:
        if rq_print[1] == NAME:
            print(rq_print)
    cur.close()
    db.close()
