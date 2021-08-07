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
    cur.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') \
                FROM cities \
                INNER JOIN states \
                ON states.name = %s \
                WHERE cities.state_id = states.id \
                ORDER BY cities.id ASC;", (NAME,))
    row_query = cur.fetchone()
    print(row_query[0] if row_query is not None else "")
db.close()
