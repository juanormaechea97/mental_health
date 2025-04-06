import csv
import sqlite3
import os

CSV_PATH = "data/processed/eurostat_clean.csv"
DB_PATH = "db/eurostat.db"

# Crear carpeta db si no existe
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Conexión a SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Crear tabla con TODAS las columnas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS eurostat (
        freq TEXT,
        unit TEXT,
        wstatus TEXT,
        age TEXT,
        sex TEXT,
        reason TEXT,
        geo TEXT,
        time TEXT,
        value REAL
    )
""")

# Limpiar la tabla antes de cargar
cursor.execute("DELETE FROM eurostat")

# Leer CSV e insertar en la tabla
with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = [
        (
            r["freq"], r["unit"], r["wstatus"], r["age"], r["sex"],
            r["reason"], r["geo"], r["time"], float(r["value"])
        )
        for r in reader if r["value"]
    ]

cursor.executemany("INSERT INTO eurostat VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)

conn.commit()
conn.close()

print(f"✅ Datos cargados correctamente en {DB_PATH}")
