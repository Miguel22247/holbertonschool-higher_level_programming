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
    db = MySQLdb.connect(host=HOST, user=MY_USER, password=MY_PSWD,
                         db=MY_DB, port=PORT)
    cur = db.cursor()
    query = 'SELECT * FROM states ORDER BY id'
    cur.execute(query)
    rowquery = cur.fetchall()
    for rqprint in rowquery:
        if rqprint[1][0] == 'N':
            print(rqprint)
    cur.close()
    db.close()
