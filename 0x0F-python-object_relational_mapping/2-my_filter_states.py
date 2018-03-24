#!/usr/bin/python3
'''List state based on user input'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'"\
                .format(sys.argv[4]))
    state = cur.fetchall()
    for row in state:
        print(row)
    cur.close()
    db.close()
