import json
import csv
import os
from itertools import product

def json_to_csv():
    INPUT_PATH = "data/eurostat_raw.json"
    OUTPUT_PATH = "data/processed/eurostat_clean.csv"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(INPUT_PATH, encoding="utf-8") as f:
        data = json.load(f)

    dimensions = data["dimension"]
    size = data["size"]
    dimension_names = data["id"]

    # Crear diccionarios de etiquetas
    labels = {
        dim: dimensions[dim]["category"]["label"]
        for dim in dimension_names
    }

    # Crear lista ordenada de claves por dimensión
    keys = {
        dim: list(labels[dim].keys())
        for dim in dimension_names
    }

    # Crear combinaciones posibles de índices por dimensión (como un grid)
    combinations = list(product(*[range(len(keys[dim])) for dim in dimension_names]))

    # Abrir CSV
    with open(OUTPUT_PATH, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dimension_names + ["value"])

        for idx, combo in enumerate(combinations):
            value = data["value"].get(str(idx))
            if value is not None:
                row = []
                for dim_index, dim in enumerate(dimension_names):
                    key = keys[dim][combo[dim_index]]
                    label = labels[dim][key]
                    row.append(label)
                row.append(value)
                writer.writerow(row)

    print(f"✅ CSV generado correctamente con {len(data['value'])} filas.")

# Esto permite ejecutarlo de forma independiente también
if __name__ == "__main__":
    json_to_csv()
