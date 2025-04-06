# 🧠 Análisis de la Salud Laboral en España (Eurostat + Power BI)

Este proyecto analiza la relación entre factores laborales y problemas de salud en la población española, utilizando datos abiertos de Eurostat. Se explora cómo influyen variables como el sexo, la edad, el estado laboral o la causa reportada sobre la prevalencia de limitaciones de salud asociadas al trabajo.

---

## 🎯 Objetivos

- Aplicar un flujo ETL completo desde una fuente oficial (API de Eurostat)
- Almacenar los datos estructurados en una base SQL local
- Realizar análisis exploratorio (EDA) y estadísticas descriptivas
- Visualizar los resultados en un dashboard interactivo con Power BI
- Formular preguntas de investigación relevantes sobre salud laboral
- Documentar y organizar el proyecto de forma modular y reproducible

---

## 🔍 Preguntas de investigación

1. ¿Qué porcentaje de personas en España sufre problemas de salud relacionados con el trabajo?
2. ¿Qué factores (edad, sexo, situación laboral) están más asociados a estos problemas?
3. ¿Existen diferencias significativas entre grupos de edad o entre hombres y mujeres?
4. ¿Qué razones son más frecuentes al reportar limitaciones de salud relacionadas con el trabajo?
5. ¿Cómo ha evolucionado este problema en los últimos años?
6. ¿Qué perfil de trabajador/a presenta más riesgo de sufrir problemas de salud laboral?

---

## 🧱 Estructura del proyecto

mental_health_api/
├── analysis/
│   └── analysis.sql 
├── data/
│   ├── raw/                # JSON original descargado desde Eurostat
│   └── processed/          # CSV limpio y listo para cargar
├── db/
│   └── eurostat.db         # Base de datos SQLite local
├── dashboards/
│   └── powerbi.pbix        # Dashboard interactivo en Power BI
├── src/
│   ├── etl.py              # Descarga de datos desde la API de Eurostat
│   ├── json_to_csv.py      # Transformación de JSON a CSV estructurado
│   └── csv_to_sqlite.py    # Carga de datos en base SQLite
├── main.py                 # Script principal que ejecuta todo el pipeline ETL
├── requirements.txt        # Dependencias del entorno virtual
└── README.md               # Documentación general del proyecto


---

## ⚙️ Reproducibilidad

1. Clonar el proyecto:
   ```bash
   git clone https://github.com/tuusuario/mental_health.git
   cd mental_health

2. Crear entorno virtual y activar:
    python3 -m venv venv
    source venv/bin/activate

3. Instalar dependencias:
    pip3 install -r requirements.txt

4. python main.py


5. Abrir eurostat.db con DB Browser o cargar en Power BI

## 📊 Dashboard

En esta sección se insertará una captura del dashboard final + breve explicación de las visualizaciones.

Ejemplo de visualizaciones:

- Gráfico de barras por grupo de edad

- Segmentación por sexo

- Evolución por año

- Tabla comparativa por causa (reason)

- Filtros interactivos en Power BI

## 🧪 Análisis y resultados

Se comentarán los principales hallazgos a partir de las consultas SQL y del dashboard en Power BI.

Ejemplos:

- Mayor prevalencia de problemas de salud laboral en el grupo de 45–64 años

- Las mujeres reportan más limitaciones de salud relacionadas con el trabajo que los hombres

- El estado laboral (desempleado vs ocupado) influye notablemente en los resultados

- Las razones más comunes son problemas físicos o estrés

## 💡 Notas finales

Este proyecto ha sido realizado como parte del Máster en Data Science con IA
Se ha optado por evitar librerías como pandas o numpy para profundizar en el manejo manual de datos
Los datos proceden del portal Eurostat



