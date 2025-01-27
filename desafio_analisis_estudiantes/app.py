import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="Datos estudiantes desafio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """
    Main function to set up the Streamlit app layout.
    """
    cs_sidebar()
    cs_body()
    return None

# Función para el sidebar
def cs_sidebar():
    """
    Sidebar con un resumen de los datos de los estudiantes.
    """
    st.sidebar.title("Análisis de Datos de Estudiantes")

    # Mostrar logo
    logo_url = "images/student.svg"  # Ajusta la ruta de la imagen si es necesario
    st.sidebar.image(logo_url, width=200)

    # Objetivos del análisis
    with st.sidebar:
        with st.expander("🎯 Objetivos del Análisis"):
            st.markdown(
                """
                - **Explorar el rendimiento académico de los estudiantes**: Analizar las notas de Matemáticas, Lenguaje y Ciencias.
                - **Identificar patrones**: Relacionar las horas de estudio con el rendimiento académico.
                - **Analizar la influencia del género y la comuna**: Evaluar cómo estos factores afectan las calificaciones de los estudiantes.
                """
            )

        # Descripción de la Aplicación
        with st.expander("📌 Descripción de la Aplicación"):
            st.markdown(
                """
                La aplicación permite explorar y analizar los datos de estudiantes en diversas áreas:
                - Carga y exploración de datos.
                - Visualización de la distribución de notas y horas de estudio.
                - Análisis de la relación entre variables como género, comuna y rendimiento académico.
                """
            )
    

def cs_body():
    """
    Create content sections for the main body of the Streamlit cheat sheet with Python examples.
    """

    # Cargar el archivo CSV
    file_path = 'data/datos_estudiantes_desafio.csv'  # Ajusta la ruta si es necesario
    df = pd.read_csv(file_path)

    # Título de la aplicación
    st.title('Análisis de Datos de Estudiantes')

    # Subtítulo
    st.subheader("Exploración de datos")

    # Expander para mostrar las primeras filas
    with st.expander('Primeras filas del conjunto de datos'):
        st.write(df.head())

    # Expander para mostrar las últimas filas
    with st.expander('Últimas filas del conjunto de datos'):
        st.write(df.tail())

    # Expander para mostrar el shape del DataFrame
    with st.expander('Dimensiones del conjunto de datos'):
        st.write(df.shape)

    # Expander para estadísticas descriptivas
    with st.expander('Estadísticas descriptivas'):
        st.write(df.describe())

    # Expander para información adicional
    with st.expander('Información adicional'):
        # Crear un DataFrame con la información de df.info()
        info_data = {
            "Columna": df.columns,
            "Tipo de datos": df.dtypes,
            "No Nulos": df.notnull().sum(),
            "Total": df.shape[0]
        }

        info_df = pd.DataFrame(info_data)

        # Mostrar la tabla con la información del DataFrame
        st.dataframe(info_df)

    # Subtítulo
    st.subheader("Limpieza de Datos")

    # Expander para verificar valores nulos
    with st.expander("Verificar valores nulos"):
        valores_nulos = df.isnull().sum()
        st.write("Valores nulos por columna:")
        st.write(valores_nulos)
    
    # Subtítulo
    st.subheader("Análisis Exploratorio")

    # Calcular el rango de edad más común
    edad_counts = df['Edad'].value_counts().sort_index()

    # Expander para mostrar el rango de edad más común
    with st.expander('Rango de edad más común entre los estudiantes'):
        st.write("Las edades más comunes entre los estudiantes son:")
        st.write(edad_counts.head())

    # Expander para el promedio por asignatura
    with st.expander('Promedio por asignatura'):
        promedio_asignaturas = df[['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']].mean()
        st.write("Promedio por asignatura:")
        st.write(promedio_asignaturas)

    # Expander para el promedio por estudiante
    with st.expander('Promedio por estudiante'):
        df['Promedio'] = df[['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']].mean(axis=1)
        st.write("Promedio por estudiante (primeros 5):")
        st.write(df[['Estudiante_ID', 'Promedio']].head())

    # Expander para el porcentaje de estudiantes con calificación >= 60
    with st.expander('Porcentaje de estudiantes con calificación >= 60'):
        porcentaje_60_matematicas = (df['Nota_Matemáticas'] >= 60).mean() * 100
        porcentaje_60_lenguaje = (df['Nota_Lenguaje'] >= 60).mean() * 100
        porcentaje_60_ciencias = (df['Nota_Ciencias'] >= 60).mean() * 100

        st.write("Porcentaje de estudiantes con calificación >= 60 en cada asignatura:")
        st.write(f"Matemáticas: {porcentaje_60_matematicas:.2f}%")
        st.write(f"Lenguaje: {porcentaje_60_lenguaje:.2f}%")
        st.write(f"Ciencias: {porcentaje_60_ciencias:.2f}%")

    # Expander para la comuna con el promedio más alto en matemáticas
    with st.expander('Comuna con el promedio más alto en matemáticas'):
        promedio_comuna = df.groupby('Comuna')['Nota_Matemáticas'].mean()
        st.write("Promedio de matemáticas por comuna:")
        st.write(promedio_comuna)
        st.write("Comuna con el promedio más alto en matemáticas:")
        st.write(promedio_comuna.nlargest(1))

    # Subtítulo de la sección
    st.subheader("Filtros y Agrupaciones")
    
    # Filtro: Estudiantes con calificaciones promedio mayores a 80
    with st.expander("Filtrar estudiantes con calificaciones promedio > 80"):
        estudiantes_altas_notas = df[df['Promedio'] > 80]
        st.write("Estudiantes con calificación promedio mayor a 80 (primeros 5):")
        st.write(estudiantes_altas_notas[['Estudiante_ID', 'Promedio']].head())
    
    # Agrupación: Promedio de calificaciones por género
    with st.expander("Promedio de calificaciones por género"):
        promedio_genero = df.groupby('Genero')[['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']].mean()
        st.write("Promedio de calificaciones por género:")
        st.write(promedio_genero)

    # Subtítulo de la sección
    st.subheader("Preprocesamiento de Datos")

    # Normalización de columnas de calificaciones y horas de estudio
    with st.expander("Normalizar columnas de calificaciones y horas de estudio"):
        scaler = StandardScaler()
        cols = ['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias', 'Horas_de_estudio']
        new_cols = ['Nota_Matemáticas_norm', 'Nota_Lenguaje_norm', 'Nota_Ciencias_norm', 'Horas_de_estudio_norm']
        
        # Normalizar las columnas y agregarlas al DataFrame
        df[new_cols] = scaler.fit_transform(df[cols])
        
        # Mostrar el rango después de la normalización
        st.write("Rango de las calificaciones después de la normalización:")
        st.write(df[new_cols].describe())
    
    # Codificación de la columna 'Genero' mediante One-Hot Encoding
    with st.expander("Convertir categorías de la columna 'Genero' en variables numéricas (One-Hot Encoding)"):
        # Realizar One-Hot Encoding
        df_genero_encoded = pd.get_dummies(df['Genero'], prefix='Genero')
        
        # Concatenar el DataFrame original con las nuevas columnas
        df_with_encoded_genero = pd.concat([df, df_genero_encoded], axis=1)
    
        # Mostrar las primeras filas del nuevo DataFrame
        st.write("Primeras filas con la columna 'Genero' codificada:")
        st.write(df_with_encoded_genero.head())

    # Subtítulo de la sección
    st.subheader("Visualizaciones")

    # Expander para mostrar los gráficos
    with st.expander("Ver distribuciones de calificaciones"):
        # Crear figura y ejes
        fig, axes = plt.subplots(1, 3, figsize=(15, 6))

        # Histograma para Matemáticas
        df['Nota_Matemáticas'].plot(kind='hist', bins=50, alpha=0.7, ax=axes[0], color='blue')
        axes[0].set_title('Distribución de Calificaciones - Matemáticas')
        axes[0].set_xlabel('Calificación')
        axes[0].set_ylabel('Frecuencia')

        # Histograma para Lenguaje
        df['Nota_Lenguaje'].plot(kind='hist', bins=50, alpha=0.7, ax=axes[1], color='red')
        axes[1].set_title('Distribución de Calificaciones - Lenguaje')
        axes[1].set_xlabel('Calificación')
        axes[1].set_ylabel('Frecuencia')

        # Histograma para Ciencias
        df['Nota_Ciencias'].plot(kind='hist', bins=50, alpha=0.7, ax=axes[2], color='green')
        axes[2].set_title('Distribución de Calificaciones - Ciencias')
        axes[2].set_xlabel('Calificación')
        axes[2].set_ylabel('Frecuencia')

        # Ajuste del espaciado
        plt.tight_layout()

        # Mostrar gráfico en Streamlit
        st.pyplot(fig)

    # Expander para mostrar el gráfico de barras
    with st.expander("Ver gráfico de barras del promedio de calificaciones por comuna"):
        # Calcular el promedio de calificaciones por comuna
        comuna_promedio = df.groupby('Comuna')[['Nota_Matemáticas', 'Nota_Lenguaje', 'Nota_Ciencias']].mean()

        # Crear el gráfico de barras
        fig, ax = plt.subplots(figsize=(12, 6))
        comuna_promedio.plot(kind='bar', ax=ax, color=['blue', 'red', 'green'])

        # Personalizar el gráfico
        ax.set_title('Promedio de Calificaciones por Comuna')
        ax.set_xlabel('Comuna')
        ax.set_ylabel('Promedio de Calificación')
        ax.set_xticks(range(len(comuna_promedio.index)))
        ax.set_xticklabels(comuna_promedio.index, rotation=45)
        ax.legend(['Matemáticas', 'Lenguaje', 'Ciencias'])

        # Mostrar gráfico en Streamlit
        st.pyplot(fig)

    # Expander para el gráfico de dispersión
    with st.expander("Ver gráfico de dispersión"):
        # Crear el gráfico de dispersión
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df['Promedio'], df['Nota_Matemáticas'], alpha=0.5, color='blue')

        # Personalizar el gráfico
        ax.set_title('Relación entre Horas de Estudio y el Promedio')
        ax.set_xlabel('Horas de Estudio')
        ax.set_ylabel('Promedio')

        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)

    # Subtítulo
    st.subheader("Conclusiones")

    # Diccionario de conclusiones intermedias
    conclusiones = {
        "Exploración de datos": """
            1. **Carga de Datos y Exploración Inicial:**
                - Los datos de los estudiantes fueron cargados exitosamente, y al mostrar las primeras y últimas filas del DataFrame, se confirmó que la estructura general de los datos está completa y organizada.
                - La revisión inicial permitió entender cómo están estructurados los datos, como columnas y tipos de variables.

            2. **Dimensionalidad del DataFrame:**
                - El uso de `.shape` confirmó la cantidad de filas y columnas, lo que ofrece una visión general del tamaño del conjunto de datos y su nivel de complejidad.

            3. **Resumen Estadístico:**
                - La utilización de `.describe()` permitió identificar medidas clave como promedio, desviación estándar, valores mínimos y máximos para las columnas numéricas. Esto ayuda a tener una visión clara de la distribución de los datos y detectar posibles valores atípicos.

            4. **Verificación de Calidad de los Datos:**
                - Mediante `.info()`, se comprobó la ausencia de valores nulos y se validó el tipo de datos en cada columna, asegurando que no será necesario realizar imputaciones de valores faltantes.
        """,
        "Limpieza de Datos": """
            Durante la etapa de **verificación y manejo de valores nulos**, se evaluaron los datos en busca de valores faltantes en cada columna. Al calcular el porcentaje de datos nulos, se determinó que **todas las columnas tienen un 0% de datos faltantes**.  

            Como resultado, no fue necesario realizar imputaciones o reemplazos, ya que el conjunto de datos está completamente limpio en este aspecto. Esta verificación garantiza que el análisis posterior no estará afectado por valores ausentes.
        """,
        "Análisis Exploratorio": """
        - **Promedio por Asignatura**:  
            - Matemáticas: **50.84%**  
            - Lenguaje: **50.47%**  
            - Ciencias: **50.59%**  
        Las calificaciones están balanceadas alrededor de 50% en promedio, lo que sugiere una distribución relativamente uniforme en las tres asignaturas.  
        - **Porcentaje de Estudiantes con Calificaciones ≥ 60**:  
            - Matemáticas: **41.30%**  
            - Lenguaje: **41.09%**  
            - Ciencias: **41.22%**  
            Aproximadamente el 41% de los estudiantes lograron calificaciones destacadas (≥ 60) en cada asignatura.  

        - **Comuna con Mejor Promedio en Matemáticas**:  
            - La comuna de **Tomé** obtuvo el promedio más alto en Matemáticas con **51.60%**, ligeramente superior al promedio general. 
        """,
        "Filtros y Agrupaciones": """
        - **Estudiantes con Calificaciones Promedio Mayores a 80**:  
            - Se identificaron **708 estudiantes** con un promedio de calificaciones superior a 80.  
            - Ejemplo de los primeros 5 estudiantes:
                - Estudiante 36: **84.33**  
                - Estudiante 81: **84.00**  
                - Estudiante 84: **83.33**  
                - Estudiante 86: **83.00**  
                - Estudiante 105: **84.67**  

        - **Promedio de Calificaciones por Género**:  
            - **Femenino**:  
                - Matemáticas: **51.05**  
                - Lenguaje: **50.58**  
                - Ciencias: **50.30**  
            - **Masculino**:  
                - Matemáticas: **50.71**  
                - Lenguaje: **50.36**  
                - Ciencias: **50.32**  
            - **Prefiero no decirlo**:  
                - Matemáticas: **50.76**  
                - Lenguaje: **50.46**  
                - Ciencias: **51.15**  

        Las diferencias en promedios por género son mínimas, pero destacan ligeramente las calificaciones de estudiantes que prefirieron no declarar su género en Ciencias (**51.15**).
        """,
        "Preprocesamiento de Datos":"""
        ##### 1. **Normalización de las Calificaciones y Horas de Estudio**  
            - Se aplicó **StandardScaler** para normalizar las columnas de calificaciones y horas de estudio.  
            - Después de la normalización:  
            - **Promedio (mean):** Cercano a 0 para todas las columnas normalizadas.  
            - **Desviación estándar (std):** Igual a 1, lo que confirma que los datos fueron escalados correctamente.  
            - **Rango de los datos:**  
                - Mínimo: Aproximadamente **-1.73**.  
                - Máximo: Aproximadamente **1.71**.  
        
            Esta normalización asegura que todas las variables tengan el mismo peso en análisis y modelos posteriores.  
        
        ##### 2. **Codificación de la Columna "Genero"**  
            - Se utilizó **One-Hot Encoding** para convertir la columna categórica `"Genero"` en variables binarias.  
            - Nuevas columnas generadas:  
            - `Genero_femenino`  
            - `Genero_masculino`  
            - `Genero_prefiero no decirlo`  
            - Ejemplo de datos procesados:  
            - El género de cada estudiante ahora está representado con valores booleanos (`True` o `False`) en las columnas correspondientes.  
        
        #### Resumen  
            - Las variables normalizadas están listas para su uso en modelos de machine learning o análisis estadísticos.  
            - La codificación de `"Genero"` asegura que los datos categóricos sean compatibles con modelos que requieren valores numéricos.
        """,
        "Visualizaciones": """
        ##### 1. **Distribución de Calificaciones por Asignatura (Primer Gráfico)**
        - Los histogramas de las calificaciones en **Matemáticas**, **Lenguaje** y **Ciencias** muestran una **distribución uniforme**.
            - Esto sugiere que las calificaciones están equilibradas y no hay asignaturas con tendencias de calificaciones más altas o más bajas.
            - La distribución uniforme indica que no hay asignaturas que se perciban significativamente más fáciles o más difíciles entre los estudiantes.

        ##### 2. **Promedio de Calificaciones por Comuna (Segundo Gráfico)**
        - El gráfico de barras proporciona un análisis de los **promedios de calificaciones por comuna**.
            - Permite identificar si alguna comuna tiene un desempeño sobresaliente o deficiente en alguna asignatura.
            - Esto podría reflejar posibles diferencias en **calidad educativa** o **acceso a recursos** en distintas comunas, lo que sugiere áreas para mejorar o investigar.

        ##### 3. **Relación entre Horas de Estudio y Promedio (Tercer Gráfico)**
        - El gráfico de dispersión muestra una clara **relación positiva** entre las **horas de estudio** y el **promedio de calificaciones**.
            - A medida que aumentan las horas dedicadas al estudio, los estudiantes tienden a tener un **mejor desempeño académico**.
            - Esta evidencia respalda la importancia del tiempo invertido en el estudio para mejorar los resultados.

        #### **Relación entre los Gráficos**
        - **Distribución de Calificaciones y Promedio por Comuna**:  
            - La distribución uniforme de calificaciones ayuda a interpretar los promedios de calificaciones por comuna de manera objetiva, sin sesgos evidentes en las calificaciones.

        - **Promedios de Calificaciones y Horas de Estudio**:  
            - Si algunas comunas presentan promedios bajos en el gráfico de barras, podría ser útil investigar si en esas comunas los estudiantes dedican menos tiempo al estudio, como sugiere la tendencia positiva del gráfico de dispersión.

        #### **Resumen**
        - Los tres gráficos proporcionan una visión integral de cómo la distribución de las calificaciones, la ubicación geográfica (comunas) y las horas de estudio influyen en el desempeño académico de los estudiantes.
        - A través de este análisis, se pueden identificar áreas de mejora tanto en términos de distribución de recursos como en la optimización del tiempo de estudio. 
        """,
        "Conclusión General": """
        El análisis del desempeño académico de los estudiantes ha proporcionado valiosas perspectivas sobre diversos factores que afectan los resultados educativos:

        1. **Calificaciones y Distribución**:  
           Las calificaciones en Matemáticas, Lenguaje y Ciencias presentan una distribución **uniforme**, lo que sugiere que no existen asignaturas significativamente más fáciles ni más difíciles. Esto refleja una estabilidad general en el desempeño de los estudiantes en estas áreas.

        2. **Impacto de las Comunas**:  
           El análisis de los promedios por comuna revela diferencias significativas en el desempeño académico, lo que podría estar relacionado con factores como la **calidad educativa** y el **acceso a recursos**. La comuna de **Tomé** se destacó con el promedio más alto en Matemáticas, lo que invita a explorar qué condiciones en esa comuna podrían estar favoreciendo el rendimiento.

        3. **Relación con las Horas de Estudio**:  
           Se encontró una **relación positiva** entre las horas de estudio y el promedio de calificaciones. Esto confirma que un mayor tiempo dedicado al estudio tiene un impacto directo en el desempeño académico, lo que resalta la importancia de la dedicación personal para mejorar los resultados.

        4. **Filtrado y Análisis por Género**:  
           Aunque las diferencias en los promedios por género son mínimas, se observó un ligero **mejor desempeño en Ciencias** entre aquellos estudiantes que prefirieron no declarar su género. Estos resultados subrayan la importancia de considerar diversas variables en el análisis de desempeño académico.

        5. **Preprocesamiento de Datos y Transformaciones**:  
           La **normalización** de las calificaciones y las **horas de estudio**, junto con la **codificación de la columna de género**, permitió preparar los datos para análisis posteriores, garantizando que las variables estén escaladas adecuadamente y que la información categórica sea manejada de manera efectiva en modelos predictivos.

        6. **Conclusiones Gráficas**:  
           Los gráficos proporcionaron una visión clara sobre cómo las distribuciones de calificaciones, los promedios por comuna y las horas de estudio se relacionan con el desempeño académico. Los resultados sugieren que, al analizar estos factores en conjunto, es posible identificar áreas para **mejorar la distribución de recursos** y optimizar **estrategias de estudio** a nivel individual y regional.

        En conjunto, estos análisis ofrecen una visión integral sobre cómo **el esfuerzo individual**, **los factores geográficos** y **el acceso a recursos educativos** pueden influir significativamente en el desempeño académico. Este enfoque puede ser útil para diseñar **políticas educativas** más equitativas y enfocadas en las necesidades específicas de los estudiantes.
        """
    }

    # Selector para elegir la sección con un placeholder
    seleccion = st.selectbox("Selecciona la sección para ver la conclusión:", 
                             ["Seleccione conclusión..."] + list(conclusiones.keys()))

    # Verificar si el usuario ha seleccionado una sección
    if seleccion != "Seleccione conclusión...":
        # Mostrar la conclusión correspondiente
        st.subheader(f"Conclusión de {seleccion}")
        st.markdown(conclusiones[seleccion])

    # Subtítulo
    st.subheader("Notas")

    # Diccionario de notas

    notas = {
        "Nota 1": """
        **Se cambió la pregunta inicial: "¿Qué patrón observas entre horas de estudio y desempeño en matemáticas?"** por **"¿Qué patrón observas entre horas de estudio y el promedio de calificaciones?"**. 
        Esto se hizo porque la relación entre horas de estudio y el desempeño específicamente en matemáticas no proporcionaba un patrón claro o no permitía hacer inferencias significativas. Al ampliar el análisis al promedio general de calificaciones, se pudo observar una relación más evidente y relevante entre las horas de estudio y el rendimiento académico.
        """,
        "Nota 2": """
        Aunque este ejemplo fue práctico y sencillo, faltaron algunos elementos que podrían haber añadido más complejidad al análisis. Por ejemplo, no se incluyeron datos nulos ni duplicados, lo que hubiera permitido realizar un manejo más exhaustivo de los datos. Además, la normalización fue bastante directa, pero para futuras iteraciones, sería beneficioso contar con un conjunto de datos más diverso y desordenado. La inclusión de valores nulos, variables categóricas adicionales o incluso datos más desbalanceados podría generar un análisis más desafiante, permitiendo aplicar técnicas más complejas de limpieza y preprocesamiento. De igual manera, la exploración de nuevas transformaciones y la manipulación de datos adicionales podría enriquecer el análisis y aportar más información relevante para los modelos posteriores.
        """
    }

    # Selector para elegir la sección con un placeholder
    seleccion = st.selectbox("Selecciona la sección para ver la nota:", 
                             ["Seleccione nota..."] + list(notas.keys()))

    # Verificar si el usuario ha seleccionado una sección
    if seleccion != "Seleccione nota...":
        # Mostrar la nota correspondiente
        st.subheader(f"Nota de {seleccion}")
        st.markdown(notas[seleccion])

    css = '''
    <style>
        /* Ajusta el tamaño del texto en las pestañas (Tabs) */
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.5rem; /* Tamaño del texto en las pestañas */
        }

        /* Opción adicional: Ajusta el tamaño de los encabezados dentro de los expanders */
        .st-expander h1, .st-expander h2, .st-expander h3 {
            font-size: 4rem; /* Tamaño de los encabezados dentro de los expanders */
        }

        /* Ajustar el tamaño del texto del selectbox en el sidebar */
        .sidebar .stSelectbox label {
            font-size: 1.5rem; /* Ajusta este valor para cambiar el tamaño del texto */
        }

    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)

    return None

if __name__ == "__main__":
    main()
