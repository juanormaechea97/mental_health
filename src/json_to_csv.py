import json
import csv
import os
from itertools import product

def json_to_csv():
    INPUT_PATH = "data/eurostat_raw.json"
    OUTPUT_PATH = "data/processed/eurostat_clean.csv"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    if not os.path.exists(INPUT_PATH):
        print("Error: El archivo JSON no existe.")
        return

    with open(INPUT_PATH, encoding="utf-8") as f:
        data = json.load(f)

    if "value" not in data or not data["value"]:
        print("El JSON no contiene valores (campo 'value' vacío o ausente).")
        return

    dimensions = data.get("dimension", {})
    size = data.get("size", [])
    dimension_names = data.get("id", [])

    if not dimension_names or not dimensions:
        print("Error: Falta información de dimensiones en el JSON.")
        return

    # Crear diccionarios de etiquetas
    labels = {
        dim: dimensions[dim]["category"]["label"]
        for dim in dimension_names if "category" in dimensions[dim]
    }

    keys = {
        dim: list(labels[dim].keys())
        for dim in dimension_names
    }

    combinations = list(product(*[range(len(keys[dim])) for dim in dimension_names]))

    registros_escritos = 0

    with open(OUTPUT_PATH, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dimension_names + ["value"])

        for idx, combo in enumerate(combinations):
            value = data["value"].get(str(idx))
            if value is not None:
                row = []
                try:
                    for dim_index, dim in enumerate(dimension_names):
                        key = keys[dim][combo[dim_index]]
                        label = labels[dim].get(key, f"UNKNOWN-{key}")
                        row.append(label)
                    row.append(value)
                    writer.writerow(row)
                    registros_escritos += 1
                except IndexError:
                    print(f"Índice fuera de rango para combinación {combo}, saltado.")

    if registros_escritos > 0:
        print(f"CSV generado correctamente con {registros_escritos} filas.")
    else:
        print("No se escribió ninguna fila en el CSV.")

if __name__ == "__main__":
    json_to_csv()
