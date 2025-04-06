import csv
import sqlite3
import os

def csv_to_sqlite():
    CSV_PATH = "data/processed/eurostat_clean.csv"
    DB_PATH = "db/eurostat.db"

    if not os.path.exists(CSV_PATH):
        print("Error: El archivo CSV no existe.")
        return

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

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

    cursor.execute("DELETE FROM eurostat")

    inserted_rows = 0
    skipped_rows = 0

    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        expected_columns = {"freq", "unit", "wstatus", "age", "sex", "reason", "geo", "time", "value"}

        if not expected_columns.issubset(reader.fieldnames):
            print("❌ Error: El archivo CSV no contiene todas las columnas necesarias.")
            return

        rows_to_insert = []

        for row in reader:
            try:
                value = float(row["value"])
                rows_to_insert.append((
                    row["freq"], row["unit"], row["wstatus"], row["age"], row["sex"],
                    row["reason"], row["geo"], row["time"], value
                ))
                inserted_rows += 1
            except (ValueError, KeyError):
                print(f"⚠️ Fila inválida: {row}")
                skipped_rows += 1

    cursor.executemany("INSERT INTO eurostat VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", rows_to_insert)

    conn.commit()
    conn.close()

    print(f"- Datos cargados correctamente en {DB_PATH}")
    print(f"- Filas insertadas: {inserted_rows}")
    if skipped_rows:
        print(f"Filas saltadas por error: {skipped_rows}")

if __name__ == "__main__":
    csv_to_sqlite()
