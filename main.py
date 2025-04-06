from src.etl import download_data
from src.json_to_csv import json_to_csv
from src.csv_to_sqlite import csv_to_sqlite

def main():
    print("1).Iniciando pipeline ETL")
    download_data()
    json_to_csv()
    csv_to_sqlite()
    print("x)Pipeline completado")

if __name__ == "__main__":
    main()
