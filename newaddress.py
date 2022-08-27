import sqlite3

conn= sqlite3.connect('addressdetails.db')

c = conn.cursor()




c.execute('''CREATE TABLE IF NOT EXISTS Address
              (id int PRIMARY KEY,
              name text,
               longitude real,
                latitude real,
                 streetname text)''')

c.execute('''INSERT OR IGNORE INTO Address VALUES
              ( '6','JOY','23.54', '56.23', 'PARKSTREET')''')


conn.commit







































