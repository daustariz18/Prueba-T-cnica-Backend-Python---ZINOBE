import sqlite3 as sql
from prueba import tabla


conn = sql.connect('paises.db')
tabla.to_sql('paises', conn)
