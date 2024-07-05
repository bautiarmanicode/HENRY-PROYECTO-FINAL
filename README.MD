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

1. KPI 1:
2. KPI 2:
3. KPI 3:

## Plan de Trabajo

El trabajo se ha organizado utilizando la metodología Gantt para asegurar una distribución efectiva de las tareas.

- **Diagrama de Gantt**: Muestra la asignación de tareas a cada miembro del equipo y el período de tiempo dedicado a cada una.

  tack Tecnológico

Nuestro proyecto utiliza una combinación de tecnologías y herramientas para garantizar un análisis de datos eficiente y un desarrollo de modelos de machine learning robusto. A continuación, se detalla el stack tecnológico empleado:

### Lenguajes de Programación

- **Python**: Utilizado para el análisis de datos, desarrollo de modelos de machine learning y scripting en general.
- **SQL**: Empleado para la gestión y consulta de bases de datos.

### Bibliotecas y Frameworks

- **Pandas**: Para la manipulación y análisis de datos.
- **NumPy**: Para operaciones matemáticas y manejo de matrices.
- **Scikit-learn**: Para el desarrollo y evaluación de modelos de machine learning.

### Bases de Datos (Aún por definir)

- **PostgreSQL**: Utilizado para almacenar y gestionar grandes volúmenes de datos estructurados.
- **SQLite**: Empleado para el almacenamiento local durante el desarrollo y pruebas.

### Herramientas de ETL (Aún por definir)

- **Apache Airflow**: Para la orquestación de flujos de trabajo de datos.
- **Talend**: Utilizado para la integración de datos y la ejecución de procesos ETL.

### Plataformas de Despliegue

- **Google cloud services**: Utilizado para almacenamiento en la nube, cómputo y servicios de machine
- **Docker**: Para la creación de contenedores y la gestión de entornos de desarrollo consistentes.

### Herramientas de Colaboración y Control de Versiones

- **Git**: Para el control de versiones del código.
- **GitHub**: Para la colaboración en el código fuente y la gestión de repositorios.
- **Trello**: Para la gestión de proyectos y seguimiento de tareas.
- **Team Gantt**: Para la designación de tareas en un tiempo específico.

### Otros Servicios y Herramientas

- **Drive**: Para la importación de los datos y donde estuvieron los datos alojados inicialmente.
- **Google Maps API**: Para la obtención de datos de localización y reseñas.
- **Yelp API**: Para la obtención de datos de reseñas y metadata de establecimientos.
- **Discord**: Para la comunicación interna del equipo, reuniones y videoconferencias.

### Visualización e Interacción

- **Power BI**: Para la visualización e interacción del usuario con los KPI's encontrados.

## Sprints

### 🏁Sprint 1: Puesta en marcha del proyecto y Trabajo con Datos🏁

En este sprint se enfoca en iniciar el proyecto y realizar un análisis preliminar de los datos y las tecnologías a emplear, con lo que teniendo un entendimiento de lo que se va a lograr encarar la solución.

### 🏁Sprint 2: Data Engineering🏁

Este sprint se centra en finalizar la infraestructura y pipelines del proyecto, al realizar el proceso ETL apuntando a estructuras de tipo Data Warehouse, Datalake, aprovechando las herramientas de Big Data para su próxima representación en la utilización de los datos.

### 🏁Sprint 3: Data Analytics + ML🏁

En este último sprint, el objetivo es tener listos los modelos de machine learning y el dashboard interactivo en donde el cliente pueda comprender, visualizar e interactuar con los datos provistos y KPI's para su consumo, y preparar una presentación integral del proyecto.

## Pipeline del Proceso ETL

- **Carga Incremental**:
  - Descripción de los pasos del pipeline ETL.
  - Herramientas y técnicas utilizadas para la carga incremental de datos.

## Análisis de los Datos

- Descripción del análisis realizado:
  - Exploración inicial de los datos.
  - Limpieza y preprocesamiento.
  - Análisis descriptivo y de tendencias.

## Índice de Archivos del Repositorio

- Lista de archivos y carpetas importantes del repositorio con una breve descripción de cada uno.
- .
- .
- .
- .

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
