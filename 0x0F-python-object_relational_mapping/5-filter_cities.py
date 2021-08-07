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
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
        cities.state_id = states.id WHERE states.name LIKE %s \
        ORDER BY cities.id", (NAME,))
    rows = cur.fetchall()
    list = []
    for r in rows:
        list.append(r[0])
    print(", ".join(list))
    cur.close()
    db.close()
