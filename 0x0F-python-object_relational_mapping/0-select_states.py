#!/usr/bin/python3
""" Script that lists all states"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    MY_HOST = 'localhost'
    MY_USER = argv[1]
    MY_PSWD = argv[2]
    MY_DBNAME = argv[3]
    try:
        databases = MySQLdb.\
            connect(myhost=MY_HOST, user=MY_USER, password=MY_PSWD, db=MY_DBNAME)
        cur = databases.cursor()
        cur.execute("SELECT * FROM states ")
    except Exception as e:
        print("ERROR")
