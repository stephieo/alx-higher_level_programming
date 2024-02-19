#!/usr/bin/python3
""" This module displays the results of a basic SQL query"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    MY_HOST = 'localhost'
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]

    # creating a connection and cursor
    conn = MySQLdb.connect(host=MY_HOST, user=MY_USER,
                           passwd=MY_PASS, port=3306, db=argv[3])
    cur = conn.cursor()

    # executing query
    cur.execute(f"""SELECT *
                    FROM states
                    ORDER BY states.id ASC;
                """)

    # display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # cloding cursor and connection
    cur.close()
    conn.close()
