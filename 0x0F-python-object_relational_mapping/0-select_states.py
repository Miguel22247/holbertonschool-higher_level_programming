#!/usr/bin/python3
""" Script that lists all states"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    HOST = 'localhost'
    MY_USER = argv[1]
    MY_PSWD = argv[2]
    MY_DB = argv[3]
    db = MySQLdb.connect(host=HOST, user=MY_USER, passwd=MY_PSWD, db=MY_DB)
    cur = db.cursor()
    query = 'SELECT * FROM states ORDER BY id ASC'
    cur.execute(query)
    row_query = cur.fetchall()
    for rq_print in row_query:
        print(rq_print)
