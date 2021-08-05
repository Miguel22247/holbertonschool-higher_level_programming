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
        database = MySQLdb.\
            connect(host=MY_HOST, user=MY_USER, password=MY_PSWD, db=MY_DBNAME)
        cur = database.cursor()
        query = 'SELECT * FROM states ORDER BY id ASC'
        cur.execute(query)
        row_query = cur.fetchall()
        for row_query in rows:
            print(row_query)
        cur.close()
        database.close()
    except Exception as excep:
        print("ERROR {}".format(excep))
