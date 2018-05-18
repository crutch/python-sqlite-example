import sqlite3

conn = sqlite3.connect('/home/crutch/workspace/mtmba/procurements.sqlite3')
conn.row_factory = sqlite3.Row

for row in conn.execute('SELECT * FROM procurements LIMIT 10'):
    print('-------------')
    print(row['customer_company_name'])

conn.close()