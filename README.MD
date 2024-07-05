# Proyecto YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS

![1718594640848](image/README/1718594640848.png)

## Índice del Proyecto

1. [Objetivo y Alcance del Proyecto](#objetivo-y-alcance-del-proyecto)
2. [Descripción del Conjunto de Datos](#descripción-del-conjunto-de-datos)
3. [Plan de Trabajo](#plan-de-trabajo)
4. [Stack Tecnológico](#stack-tecnológico)
5. [Sprints](#sprints)
   - [Sprint 1: Puesta en marcha del proyecto y Trabajo con Datos](#sprint-1-puesta-en-marcha-del-proyecto-y-trabajo-con-datos)
   - [Sprint 2: Data Engineering](#sprint-2-data-engineering)
   - [Sprint 3: Data Analytics + ML](#sprint-3-data-analytics--ml)
6. [Pipeline del Proceso ETL](#pipeline-del-proceso-etl)
7. [Análisis de los Datos](#análisis-de-los-datos)
8. [Tecnologías Utilizadas](#tecnologías-utilizadas)
9. [Índice de Archivos del Repositorio](#índice-de-archivos-del-repositorio)
10. [Equipo Involucrado](#equipo-involucrado)

## Objetivo y Alcance del Proyecto

![1720196076920](image/README/1720196076920.png)

El objetivo de este proyecto es analizar y recomendar establecimientos basados en las reseñas y datos obtenidos de Yelp y Google Maps. Este análisis incluye:

1. Análisis de Sentimientos :

- 😊 Analizar las reseñas de Yelp y Google Maps para determinar el sentimiento general (positivo, negativo, neutral).
- 🔍 Identificar tendencias y patrones en las opiniones de los usuarios.

2. Predicción de Crecimiento :

- 📈 Predecir cuáles rubros de negocios crecerán o decaerán.
- 📉 Identificar áreas de oportunidad o riesgo.

3. Emplazamiento de Nuevos Locales :

- 🗺️ Determinar las mejores ubicaciones para abrir nuevos locales. basados en análisis de mercado y datos de reseñas.

4. Sistema de Recomendación :

- 🤖 Desarrollar un sistema que ofrezca recomendaciones personalizadas de restaurantes y otros negocios.
- 🌟 Permitir a los usuarios descubrir nuevos sabores y experiencias basadas en sus reseñas previas.

## Descripción del Conjunto de Datos

- **Diccionario_Datos.ipynb**: Contiene la descripción detallada de los datos utilizados.
- **Conjunto de Datos**: Incluye reseñas de usuarios en Google Maps y Yelp sobre los establecimientos que visitan.
  - [**Dataset Google Maps**](https://drive.google.com/drive/folders/1Wf7YkxA0aHI3GpoHc9Nh8_scf5BbD4DA): Incluye la metadata de sitios y reviews de estados de los usuarios.
  - [**Dataset Yelp**](https://drive.google.com/drive/folders/1TI-SsMnZsNP6t930olEEWbBQdo_yuIZF?usp=sharing): Conjunto de datos que contiene:
    - business.pkl
    - checkin.json
    - review.json
    - tip.json
    - user.parquet

Para ver mas informacion, ingresar al [diccionario de datos](https://github.com/bautiarmanicode/HENRY-PROYECTO-FINAL/blob/master/0%20Diccionario_Datos.ipynb)

## Key Performance Indicators (KPis)

**KPI 1:**
Promedio Anual de Calificación de las Reseñas
Descripción: Medir el promedio de las calificaciones otorgadas por los clientes cada año
Objetivo: Incrementar el promedio anual de calificaciones en un 10% durante el próximo año.
Periodo de Tiempo: Anual, revisado al final de cada año.
Meta: Si el promedio actual de calificaciones es 4.0, la meta sería alcanzar un promedio de 4.4 en el proximo año.

**KPI 2:**
Número de Reseñas Recibidas por Mes
Descripción: Contar el número de reseñas recibidas cada mes.
Objetivo: Aumentar el número de reseñas mensuales en un 15% durante el próximo trimestre.
Periodo de Tiempo: Mensual, revisado al final de cada mes.
Meta: Si actualmente se reciben 100 reseñas por mes, la meta sería alcanzar 115 reseñas mensuales al final del trimestre.

**KPI 3:**

Comparativa de Popularidad con Competencia (Taco Bell)

Descripción: Medir y comparar la popularidad de Pizza Hut frente a Taco Bell en Florida utilizando el número de reseñas y la calificación promedio.

Objetivo: Superar a Taco Bell en número de reseñas y calificación promedio en un 15% durante el próximo año.

Periodo de Tiempo: Anual, revisado al final de cada año.

Meta: Número de reseñas: Si Taco Bell recibe 1,000 reseñas anuales, Pizza Hut debe recibir al menos 1,150 reseñas. Calificación promedio: Si la calificación promedio de Taco Bell es 4.0, Pizza Hut debe alcanzar al menos 4.6.

## Plan de Trabajo

El trabajo se ha organizado utilizando la metodología Gantt para asegurar una distribución efectiva de las tareas.

- **Diagrama de Gantt**: Muestra la asignación de tareas a cada miembro del equipo y el período de tiempo dedicado a cada una.

### 🏁Sprint 1: Puesta en marcha del proyecto y Trabajo con Datos🏁

En este sprint se enfoca en iniciar el proyecto y realizar un análisis preliminar de los datos y las tecnologías a emplear, con lo que teniendo un entendimiento de lo que se va a lograr encarar la solución.

### 🏁Sprint 2: Data Engineering🏁

Este sprint se centra en finalizar la infraestructura y pipelines del proyecto, al realizar el proceso ETL apuntando a estructuras de tipo Data Warehouse, Datalake, aprovechando las herramientas de Big Data para su próxima representación en la utilización de los datos.

![1720199390691](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/El%20Bauto/Desktop/HENRY%20PROYECTO%20FINAL/image/README/1720199390691.png)

### 🏁Sprint 3: Data Analytics + ML🏁

En este último sprint, el objetivo es tener listos los modelos de machine learning y el dashboard interactivo en donde el cliente pueda comprender, visualizar e interactuar con los datos provistos y KPI's para su consumo, y preparar una presentación integral del proyecto.

![1720199444411](image/README/1720199444411.png)

# Stack Tecnologico

Nuestro proyecto utiliza una combinación de tecnologías y herramientas para garantizar un análisis de datos eficiente y un desarrollo de modelos de machine learning robusto. A continuación, se detalla el stack tecnológico empleado:

### Lenguajes de Programación

- **Python**: Utilizado para el análisis de datos, desarrollo de modelos de machine learning y scripting en general.
- **SQL**: Empleado para la gestión y consulta de bases de datos.

### Bibliotecas y Frameworks

- **Pandas**: Para la manipulación y análisis de datos.
- **NumPy**: Para operaciones matemáticas y manejo de matrices.
- **Scikit-learn**: Para el desarrollo y evaluación de modelos de machine learning.

### Bases de Datos BigQuery

- **BigQuery:**

### Herramientas de ETL

- Google Cloud Funcitions:

### Plataformas de Despliegue

- **Google cloud services**: Utilizado para almacenamiento en la nube, cómputo y servicios de machine

### Herramientas de Colaboración y Control de Versiones

- **Git**: Para el control de versiones del código.
- **GitHub**: Para la colaboración en el código fuente y la gestión de repositorios.
- **Trello**: Para la gestión de proyectos y seguimiento de tareas.
- **Team Gantt**: Para la designación de tareas en un tiempo específico.

### Otros Servicios y Herramientas

- **Drive**: Para la importación de los datos y donde estuvieron los datos alojados inicialmente
- **Discord**: Para la comunicación interna del equipo, reuniones y videoconferencias.

### Visualización e Interacción

- **Power BI**: Para la visualización e interacción del usuario con los KPI's encontrados.

## Pipeline del Proceso ETL

![1720199482652](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/El%20Bauto/Desktop/HENRY%20PROYECTO%20FINAL/image/README/1720199482652.png)

## Índice de Archivos del Repositorio

**0_Dataset**

* Carpeta que contiene los archivos de datos originales antes de cualquier procesamiento y las muestras extraidas por Data Engineer.

**1_Jupyter_Notebooks**

* Aquí se almacenan los Jupyter Notebooks utilizados para la limpieza, análisis preliminar de los datos, y machine Learning.

**3_MachineLearning**

* Contiene los notebooks de Jupyter desarrollados para el análisis exploratorio de datos (EDA) y modelos de Machine Learning. Se incluyen detalles de las técnicas utilizadas y los resultados obtenidos.
* **0 Diccionario_Datos.ipynb** : Notebook de Jupyter con el diccionario de datos.

## Equipo Involucrado

![1720195634242](image/README/1720195634242.png)

### Información sobre los miembros del equipo:

- Nombres y roles:
  - **Bautista Armani**
    - Rol: Data Engineer
    - [LinkedIn](https://www.linkedin.com/in/bautiarmani/)
  - **Adrian Panduro**
    - Rol: Data Engineer
    - [LinkedIn](https://www.linkedin.com/in/adrian-panduro-valdivia-7a1ab5290/)
  - **Lorenzo Locava**
    - Rol: Data Scientist
    - [LinkedIn](https://www.linkedin.com/in/lacavalorenzo/)
  - **Juan Celada**
    - Rol: Data Analyst
    - [LinkedIn](https://www.linkedin.com/in/juan-cruz-celada/)
  - **Jay Peralta**
    - Rol: Data Analyst
    - [LinkedIn](https://www.linkedin.com/in/jayperaltaborjas/)

---
