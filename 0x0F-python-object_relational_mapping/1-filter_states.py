#!/usr/bin/python3
'''Lists all states start with letter N'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY'N%'\
                ORDER BY states.id ASC")
    state = cur.fetchall()
    for row in state:
        print(row)
    cur.close()
    db.close()
