#!/usr/bin/python3
'''Lists all cities of a state'''
import MySQLdb
import sys


db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()

if __name__ == "__main__":
    cur.execute("SELECT cities.name FROM cities\
                 JOIN states ON cities.state_id = states.id\
                 WHERE states.name = %s\
                 ORDER BY cities.id ASC", (sys.argv[4],))
    city = cur.fetchall()
    result = []
    for row in city:
        result.append(row[0])
    print(', '.join(result))
    cur.close()
    db.close()
