import sqlite3

class Procurement:
    def __init__(self, customer, supplier, price, year, subject):
        self.customer = customer
        self.supplier = supplier
        self.price = price
        self.year = year
        self.subject = subject

    def __str__(self):
        return f"V {self.year} si {self.customer} objednal od {self.supplier} toto: {self.subject} za {self.price}"

###########################################

conn = sqlite3.connect('/home/crutch/workspace/mtmba/procurements.sqlite3')
conn.row_factory = sqlite3.Row
##########################################
procurements = []
with conn:
    for row in conn.execute('SELECT * FROM procurements LIMIT 30'):
        procurements.append(Procurement(row['customer_company_name'], row['supplier_company_name'], row['price'], row['year'], row['procurement_subject']))

print()
print(f"Mame tu {len(procurements)} obstaravani:")
for procurement in procurements:
    print(procurement)
