import sqlite3
con = sqlite3.connect("crud.db")

cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS peliculas(id INTEGER PRIMARY KEY AUTOINCREMENT,titulo TEXT,
            anio INTEGER, puntuacion INTEGER )""")