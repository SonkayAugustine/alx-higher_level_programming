#!/usr/bin/python3
'''
5-filter_cities.py:a script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
'''
import MySQLdb
import sys

if __name__ == '__main__':
    state_search = sys.argv[4]
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute('SELECT c.name FROM cities c INNER JOIN states s ' +
                'ON s.id = c.state_id WHERE ' +
                'BINARY s.name = %s ' +
                'ORDER BY c.id ASC;', [state_search])
    query_rows = cur.fetchall()
    print(', '.join(map(lambda x: x[0], query_rows)))

    cur.close()
    conn.close()
