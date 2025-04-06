import requests
import json

URL = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hlth_silc_13?geo=ES&format=JSON"

def download_data():
    print("Descargando datos desde Eurostat...")

    try:
        response = requests.get(URL, timeout=10)  # Espera máximo 10 segundos
        response.raise_for_status()  # Lanza excepción si el status no es 200

        data = response.json()
        with open("data/eurostat_raw.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("✅ Datos guardados correctamente en data/eurostat_raw.json")

    except requests.exceptions.Timeout:
        print("⏱️ La solicitud ha tardado demasiado y fue cancelada (timeout).")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error al descargar datos: {e}")

if __name__ == "__main__":
    download_data()
