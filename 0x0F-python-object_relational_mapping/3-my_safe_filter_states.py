#!/usr/bin/python3
""" this module executes an SQL command with python script,
    safe from SQL injections"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    MY_HOST = 'localhost'
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    STATE_NAME = argv[4]

    conn = MySQLdb.connect(host=MY_HOST, user=MY_USER,
                           passwd=MY_PASS,  port=3306,db=MY_DB)
    cur = conn.cursor()

    cur.execute(f""" SELECT * FROM states WHERE name = %s
                ORDER BY states.id ASC; """, (STATE_NAME,))

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    conn.close()
