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

    @staticmethod
    def from_row(row):
        return Procurement(row['customer_company_name'], row['supplier_company_name'], row['price'], row['year'],
                    row['procurement_subject'])

class ProcurementService:
    def __init__(self, sqlite_filename):
        self.conn = sqlite3.connect(sqlite_filename)
        self.conn.row_factory = sqlite3.Row

    def fetch_first(self, limit):
        procurements = []
        with self.conn:
            for row in self.conn.execute(f"SELECT * FROM procurements LIMIT {limit}"):
                procurements.append(Procurement.from_row(row))
        return procurements

########################################
ps = ProcurementService('/home/crutch/workspace/mtmba/procurements.sqlite3')
########################################
procurements = ps.fetch_first(30)

print()
print(f"Mame tu {len(procurements)} obstaravani:")
for procurement in procurements:
    print(procurement)

print()

procurements = ps.fetch_first(20)

print()
print(f"Mame tu {len(procurements)} obstaravani:")
for idx, procurement in enumerate(procurements, start=1):
    print(idx, procurement)
