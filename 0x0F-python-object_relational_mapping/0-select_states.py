#!/usr/bin/python3
""" Script that lists all states"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    MY_HOST = 'localhost'
    MY_USER = argv[[1]]
    MY_PSWD = argv[2]
    MY_DBNAME = argv[3]
    