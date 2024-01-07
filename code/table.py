import sqlite3

# create a database connection
conn = sqlite3.connect('bank_database.db')

# create a table
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE customers (
        Account_number INTEGER,
        Name TEXT,
        Gender TEXT,
        Address TEXT,
        Phone_number TEXT,
        Email TEXT,
        Balance REAL,
        Date TEXT,
        Time TEXT
    )
''')

# commit the changes
conn.commit()

# close the connection
conn.close()
