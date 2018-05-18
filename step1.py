import sqlite3

conn = sqlite3.connect('/home/crutch/workspace/mtmba/procurements.sqlite3')

for row in conn.execute('SELECT * FROM procurements LIMIT 10'):
    # print(row)
    print('-------------')
    print(row[14])

conn.close()