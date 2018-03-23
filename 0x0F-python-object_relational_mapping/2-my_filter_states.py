#!/usr/bin/python3
'''List state based on user input'''
import MySQLdb
import sys


db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()

if __name__ == "__main__":
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))
    state = cur.fetchall()
    for row in state:
        print(row)
    cur.close()
    db.close()
