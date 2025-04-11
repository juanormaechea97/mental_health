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
│   └── powerbi.pbix  
├── notebooks/
│   └── exploration.ipynb        # Dashboard interactivo en Power BI
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
   git clone https://github.com/juanormaechea97/mental_health.git
   cd mental_health

2. Crear entorno virtual y activar:
    python3 -m venv venv
    source venv/bin/activate

3. Instalar dependencias:
    pip3 install -r requirements.txt

4. python main.py


5. Abrir eurostat.db con DB Browser o cargar en Power BI


# 📈 Análisis en Power BI

# 📊 Página 1: Evolución económica de las barreras

1. Título: Evolución del acceso limitado a atención médica por razones económicas

2. Visualización: Gráfico de línea con el promedio de "Too expensive" a lo largo del tiempo.

3. Indicador adicional: Máximo histórico (%).

# Conclusión:

Se observa un descenso progresivo de esta barrera económica desde 2013.

El pico fue del 7.1% en años anteriores.

Esto podría reflejar mejoras en accesibilidad o cambios en la percepción de coste.

# 🌎 Página 2: Análisis geográfico y por género

1. Título: ¿Dónde y para quién es más difícil acceder a atención médica?

2. Mapa: Distribución geográfica de barreras económicas.

3. Gráfico de barras: Comparativa de barreras por sexo y año.

# Conclusión:

Las diferencias por sexo existen, siendo las mujeres ligeramente más afectadas en años clave.

Las barreras aparecen agrupadas en regiones concretas.

Esto sugiere que el acceso desigual podría estar relacionado con el territorio y el género.

# 👥 Página 3: Edad, motivo y sexo

1. Título: Barreras médicas en la población española: edad, sexo y motivo

2. Gráfico de dispersión: Relación entre motivo, edad y suma de casos.

3. Gráfico de columnas agrupadas: Comparativa de motivos por sexo.

# Conclusión:

Los jóvenes tienden a declarar "esperar a ver si mejora" como barrera.

Las barreras económicas afectan más a personas de entre 25 y 44 años.

Los datos muestran una distribución bastante homogénea entre hombres y mujeres según motivos.

## 🔍 Conclusiones generales

Las barreras económicas siguen presentes, pero han disminuido con el tiempo.

El género y la edad influyen en el tipo de barrera declarada.

Existen diferencias regionales que deberían estudiarse más a fondo.


## 💡 Notas finales

Este proyecto ha sido realizado como parte del Máster en Data Science con IA
Se ha optado por evitar librerías como pandas o numpy para profundizar en el manejo manual de datos
Los datos proceden del portal Eurostat



