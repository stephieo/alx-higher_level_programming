#!/usr/bin/python3
"""module uses python script to query database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    MY_HOST = 'localhost'
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]

    #create connection and cursor
    conn = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = conn.cursor()

    #execute query and display results
    cur.execute(f"""SELECT * FROM cities
                    ORDER BY cities.id ASC""")
    
    conn.commit()
    results = cur.fetchall()
    for row in results:
        print(row)

    #close cursor and connection
    cur.close()
    conn.close()
