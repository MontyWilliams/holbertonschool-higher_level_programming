#!/usr/bin/python3
""" Script lists all states with names starting with 'N' from db hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=int(3306), user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
