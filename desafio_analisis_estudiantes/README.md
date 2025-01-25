# Desafío 049H

**Objetivo:** Analizar y procesar los datos de estudiantes para descubrir patrones, realizar transformaciones, y crear visualizaciones utilizando NumPy, Pandas, Sckit-Learn y Matplotlib.

1. **Cargue el archivo datos_estudiantes_desafio.csv**
* El archivo datos_estudiantes_desafio.csv contiene 20 mil registros:
 * Estudiante_ID: Identificador único del estudiante.
 * Edad: Edad del estudiante.
 * Horas_de_estudio: Número promedio de horas de estudio por semana.
 * Nota_Matemáticas, Nota_Lenguaje, Nota_Ciencias: Calificaciones en cada asignatura.
 * Genero: Género del estudiante.
 * Comuna: Comuna donde reside el estudiante.


2. **Exploración de datos:**
* Verificar las primeras y últimas filas del conjunto de datos (head y tail).
* Mostrar la forma del conjunto de datos (shape).
* Mostrar estadísticas descriptivas de las columnas numéricas (describe).
* Pregunta: ¿Cuál es el rango de edad más común entre los estudiantes?


3. **Limpieza de Datos:**
* Verificar y manejar valores nulos o faltantes en el conjunto de datos.
 * Identificar si hay valores nulos (isnull).
 * Si hay valores nulos, reemplazarlos por la mediana en las columnas numéricas.
* Pregunta: ¿Cuál es el porcentaje de datos faltantes en cada columna?


4. **Análisis Exploratorio:**
* Calcular las siguientes métricas para las columnas de calificaciones:
 * Promedio general por asignatura.
 * Promedio por estudiante.
* Determinar el porcentaje de estudiantes que tienen una calificación mayor o igual a 60 en las tres asignaturas.
* Pregunta: ¿Qué comuna tiene el promedio más alto en matemáticas?


5. **Filtros y Agrupaciones:**
* Filtrar estudiantes con calificaciones promedio mayores a 80 y mostrarlos en un nuevo DataFrame.
* Agrupar los datos por género y calcular el promedio de calificaciones por género.


6. **Preprocesamiento de Datos:**
* Normalizar las columnas de calificaciones y horas de estudio usando NumPy o Scikit-learn.
* Convertir las categorías de la columna Genero en variables numéricas (One-Hot Encoding).
* Pregunta: ¿Cuál es el rango de las calificaciones después de la normalización.


7. **Visualizaciones:**
* Crear gráficos utilizando Matplotlib (https://matplotlib.org/stable/gallery/index.html).
  * Distribución de calificaciones por asignatura.
  * Promedio de calificaciones por comuna (gráfico de barras).
* Crear un gráfico de dispersión que relacione Horas_de_estudio y Nota_Matemáticas.
* Pregunta: ¿Qué patrón observas entre horas de estudio y desempeño en matemáticas?