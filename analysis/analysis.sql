from pathlib import Path

# Crear el archivo analysis.sql con algunas consultas útiles
sql_queries = """
-- Porcentaje medio de personas con problemas de salud laboral por grupo de edad
SELECT age, AVG(value) AS promedio
FROM eurostat
GROUP BY age
ORDER BY promedio DESC;

-- Evolución temporal de problemas de salud por razones económicas
SELECT time, AVG(value) AS media
FROM eurostat
WHERE reason = 'Too expensive'
GROUP BY time
ORDER BY time;

-- Comparativa por sexo en razón 'Too expensive'
SELECT sex, AVG(value) AS promedio
FROM eurostat
WHERE reason = 'Too expensive'
GROUP BY sex;

-- Comparativa por estado laboral (wstatus)
SELECT wstatus, AVG(value) AS promedio
FROM eurostat
GROUP BY wstatus
ORDER BY promedio DESC;

-- Razones más frecuentes con mayor impacto medio
SELECT reason, AVG(value) AS promedio
FROM eurostat
GROUP BY reason
ORDER BY promedio DESC;
"""

# Crear carpeta si no existe
Path("analysis").mkdir(parents=True, exist_ok=True)

# Guardar archivo
file_path = Path("analysis/analysis.sql")
file_path.write_text(sql_queries)

file_path.name
