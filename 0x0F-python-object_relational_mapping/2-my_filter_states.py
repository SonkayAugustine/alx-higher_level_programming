#!/usr/bin/python3
'''
2-my_filter_states.py:  a script that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
'''

import MySQLdb
import sys

if __name__ == '__main__':
    state_search = sys.argv.argv[4]
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "{}"
                 ORDER BY id ASC;'.format(state_search))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
