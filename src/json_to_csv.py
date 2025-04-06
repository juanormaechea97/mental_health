import json
import csv
import os

INPUT_PATH = "data/eurostat_raw.json"
OUTPUT_PATH = "data/processed/eurostat_clean.csv"

# Crear carpeta si no existe
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Cargar el JSON
with open(INPUT_PATH, encoding="utf-8") as f:
    data = json.load(f)

# Extraer dimensiones y etiquetas
dimensions = data["dimension"]
category_labels = {}
dim_order = []

for dim_name, dim_data in dimensions.items():
    if "category" in dim_data:
        labels = dim_data["category"]["label"]
        category_labels[dim_name] = labels
        dim_order.append(dim_name)

# Valores
values = data["value"]

# Guardar CSV
with open(OUTPUT_PATH, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(dim_order + ["value"])

    for key, val in values.items():
        indices = list(map(int, key.split(":")))
        row = []
        error_detected = False

        for i, dim_name in enumerate(dim_order):
            label_dict = category_labels[dim_name]
            label = label_dict.get(str(indices[i]))

            if label is None:
                print(f"No se encontró etiqueta para índice {indices[i]} en '{dim_name}'")
                error_detected = True
                break

            row.append(label)

        if not error_detected:
            row.append(val)
            writer.writerow(row)

print(f"CSV generado correctamente en {OUTPUT_PATH}")
