![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

# **PROYECTO GRUPAL Nº1**

---

# `<h1 align="center">`**`YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS`**`</h1>`

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yelp_Logo.svg/2560px-Yelp_Logo.svg.png"  height="200">
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Google_Maps_Logo_2020.svg/512px-Google_Maps_Logo_2020.svg.png"  height="200">

## **Contexto**

🍽️ **Yelp**

* Plataforma de reseñas de negocios como restaurantes, hoteles y servicios.
* Los usuarios suben reseñas basadas en sus experiencias.

🗺️ **Google Maps**

* Plataforma de reseñas integrada en el servicio de localización y mapas de Google.
* Reseñas de todo tipo de negocios, restaurantes, hoteles, servicios, entre otros.
* Los usuarios suben reseñas tras utilizar servicios.

##### 🔍 Información valiosa para empresas:

* ⭐ Los usuarios utilizan estos servicio y luego suben su reseña según la experiencia vivida.
* 🗺️ Conocer distintos locales de la empresa
* 🏆 Conocer la imagen que tienen los usuarios
* 📈 Medir desempeño y utilidad.
* 🔍 Identificar aspectos a mejorar.

⭐⭐⭐⭐⭐ Muchos usuarios leen las reseñas de los lugares a los que planean ir para tomar decisiones sobre dónde comprar, comer, dormir, reunirse, etc.

## **Rol a desarrollar - Consultora de Data**

### 😎 Nos ha contratado un conglomerado de empresas de restaurantes y afines para poder realizar un análisis detallado del mercado estadounidense:

**Análisis de Sentimientos** :

* 😊 **Análisis de Sentimientos** de las reseñas en Yelp y Google Maps.
* 📊 Determinar el sentimiento general (positivo, negativo, neutral) hacia los negocios del sector(hoteles, restaurantes y otros negocios afines al turismo y ocio).
* 🔍 Identificar tendencias en las opiniones de los usuarios sobre distintos aspectos del servicio.

 **Predicción de Crecimiento** :

* 📈 Utilizar los datos recopilados para predecir cuáles serán los rubros de los negocios que más crecerán o decaerán.
* 📉 Analizar patrones y comportamientos en las reseñas para identificar áreas de oportunidad o riesgo.

 **Emplazamiento de Nuevos Locales** :

* 🗺️ Determinar las ubicaciones óptimas para abrir nuevos locales de restaurantes y negocios afines.
* 📍 Usar datos de reseñas y análisis de mercado para identificar zonas con alta demanda y menos competencia.

 🤖 **Sistema de Recomendación** :

* 🤖 Desarrollar un sistema de recomendación de restaurantes y otros negocios para usuarios de Yelp y Google Maps.
* Poder cambiar el tipo de comercio (no es necesario que sean restaurantes)
* ⭐ Ofrecer recomendaciones personalizadas basadas en las experiencias previas de los usuarios. (x ejemplo: nuevos sabores)
* 🌟 Incluir la posibilidad de descubrir nuevos sabores y experiencias.

## **Propuesta de trabajo**

### **1. Recopilar, Depurar y Disponibilizar la Información**

📊  **Creación de una Base de Datos (DataWarehouse)** :

* Integrar datos de diferentes fuentes, tanto provistas por Henry como incorporadas por nuestro equipo.
* La base de datos puede correr en local o estar alojada en proveedores en la nube.

🔄  **Depuración de Datos** :

* Asegurar que los datos sean precisos, completos y consistentes.
* Remover duplicados, datos erróneos o inconsistentes.

🛠️  **Métodos de Extracción de Datos** (POR LO MENOS 2):

* **Datos Estáticos** : Importar datos de archivos planos, como CSV o Excel.
* **APIs** : Realizar llamadas a APIs para obtener datos en tiempo real.
* **Scrapping** : Extraer datos de páginas web relevantes usando técnicas de web scraping

### **2. Reporte y Análisis Significativos de la(s) Línea(s) de Investigación Escogidas**

📊  **Análisis de Datos** :

* Analizar las relaciones entre variables para identificar patrones y correlaciones.
* Determinar si existe una relación significativa entre las variables y los posibles factores que la causan.

📈  **Informe de Resultados** :

* Presentar los hallazgos de manera clara y concisa, utilizando visualizaciones efectivas como gráficos y tablas.
* Incluir conclusiones sobre las relaciones encontradas y sus posibles causas en la realidad.

### **3. Entrenamiento y Puesta en Producción de un Modelo de Machine Learning**

**El modelo debe:**

- Resolver un problema
- Conectar globalmente con los objetivos propuestos que se propongan como proyecto

🤖  **Desarrollo del Modelo** :

* Entrenar un modelo de machine learning, ya sea de clasificación supervisada o no supervisada.
* Asegurar que el modelo esté alineado con los objetivos del proyecto.

🚀  **Puesta en Producción** :

* Implementar el modelo en un entorno de producción para que pueda ser utilizado en tiempo real.
* Validar y ajustar el modelo continuamente para mejorar su precisión y eficacia.

### **EXTRA: Objetivos del Proyecto**

1. **Análisis de Sentimientos** :

* 😊 Analizar las reseñas de Yelp y Google Maps para determinar el sentimiento general (positivo, negativo, neutral).
* 🔍 Identificar tendencias y patrones en las opiniones de los usuarios.

1. **Predicción de Crecimiento** :

* 📈 Predecir cuáles rubros de negocios crecerán o decaerán.
* 📉 Identificar áreas de oportunidad o riesgo.

1. **Emplazamiento de Nuevos Locales** :

* 🗺️ Determinar las mejores ubicaciones para abrir nuevos locales basados en análisis de mercado y datos de reseñas.

1. **Sistema de Recomendación** :

* 🤖 Desarrollar un sistema que ofrezca recomendaciones personalizadas de restaurantes y otros negocios.
* 🌟 Permitir a los usuarios descubrir nuevos sabores y experiencias basadas en sus reseñas previas.

---

## **Ideas de análisis e implementación**

### 1_Mejoramiento de estrategias de marketing: campañas microsegmentadas

📊  **Análisis de Segmentación de Usuarios** :

* Identificar distintos segmentos de usuarios basados en sus comportamientos y opiniones en Yelp y Google Maps.
* Usar técnicas de clustering para agrupar usuarios con características similares.

📈  **Campañas Personalizadas** :

* Desarrollar campañas de marketing específicas para cada segmento.
* Personalizar mensajes y ofertas según las preferencias y comportamientos de cada grupo.

🎯  **Optimización de Publicidad** :

* Analizar la efectividad de las campañas en tiempo real.
* Ajustar estrategias basadas en los resultados y feedback de los usuarios.

### 2_ Sistemas de recomendación: Sobre algún lugar en particular, pueden ser comercios como restaurantes, hoteles, entre otros.

🤖  **Desarrollo de Algoritmo de Recomendación** :

* Implementar un sistema de recomendación que sugiera lugares específicos como restaurantes y hoteles.
* Utilizar modelos de filtrado colaborativo y basado en contenido para mejorar la precisión de las recomendaciones.

⭐  **Personalización de Recomendaciones** :

* Ofrecer recomendaciones personalizadas basadas en las experiencias previas y preferencias del usuario.
* Incluir opciones para descubrir nuevos lugares y experiencias.

🌟  **Interfaz de Usuario Amigable** :

* Desarrollar una interfaz intuitiva para que los usuarios interactúen fácilmente con el sistema de recomendación.
* Integrar el sistema en plataformas como aplicaciones móviles y sitios web.

### 3_ Datos adicionales a cruzar: Cotizaciones en bolsa, tendencias en redes sociales y medios de comunicación sobre comercios en expansíón.

📈  **Cotizaciones en Bolsa** :

* Analizar el rendimiento de las empresas en bolsa relacionadas con la industria de restaurantes y turismo.
* Correlacionar las tendencias de mercado con las opiniones de los usuarios.

📱  **Tendencias en Redes Sociales** :

* Monitorizar las tendencias en redes sociales sobre comercios en expansión.
* Utilizar herramientas de análisis de redes sociales para identificar patrones y menciones relevantes.

📰  **Medios de Comunicación** :

* Analizar artículos y noticias sobre la expansión de comercios.
* Correlacionar la cobertura mediática con las reseñas y opiniones de los usuarios.

### **EXTRA: Implementación**

🔧  **Integración de Datos** :

* Crear pipelines de datos para recopilar, procesar y almacenar información de distintas fuentes.
* Asegurar la calidad y consistencia de los datos antes de su análisis.

🛠️  **Herramientas y Tecnologías** :

* Utilizar herramientas de análisis de datos como Python, R, y SQL.
* Implementar modelos de machine learning con frameworks como TensorFlow y Scikit-learn.
* Emplear herramientas de visualización de datos como Tableau y Power BI.

📊  **Dashboards e Informes** :

* Desarrollar dashboards interactivos para visualizar los resultados del análisis.
* Generar informes periódicos para informar a los stakeholders sobre los hallazgos y recomendaciones.

## **Datasets y fuentes complementarias**

### **1. Datos Principales**

📊  **Yelp y Google Maps** :

* **Ubicación de los Comercios** : Coordenadas geográficas y direcciones.
* **Categoría de los Comercios** : Tipo de negocio (restaurante, hotel, etc.).
* **Puntajes Promedios** : Calificaciones promedio otorgadas por los usuarios.
* **Estado de los Comercios** : Información sobre si los comercios están abiertos o cerrados.
* **Datos de Usuarios** : Perfiles de usuarios, incluyendo el número de reseñas hechas y votos recibidos.
* **Reseñas de Usuarios** : Contenido de las reseñas, fecha, y puntuación.

### **2. Datasets Adicionales(información pertinente al pedido)**

📈  **Valores de Acciones de las Empresas** :

* **Fuente** : Yahoo Finance, Google Finance, o API de mercado de valores.
* **Contenido** : Precios históricos de las acciones, volúmenes de negociación, capitalización de mercado, y otros indicadores financieros.

🌍  **Información Geográfica Adicional** :

* **Fuente** : OpenStreetMap, US Census Bureau, Google Maps API.
* **Contenido** : Datos demográficos, información sobre infraestructuras (transporte, servicios públicos), zonas comerciales y residenciales.

📱  **Tendencias en Redes Sociales** :

* **Fuente** : APIs de redes sociales (Twitter, Facebook, Instagram).
* **Contenido** : Menciones y hashtags relevantes, sentimiento general, tendencias de búsqueda.

📰  **Medios de Comunicación** :

* **Fuente** : APIs de noticias (NewsAPI, Google News).
* **Contenido** : Artículos y noticias relacionadas con la industria de restaurantes y turismo.

### **3. Técnicas de Procesamiento**

🛠️  **Procesamiento de Lenguaje Natural (NLP)** :

* **Limpieza y Preprocesamiento de Textos** : Eliminación de ruido, tokenización, lematización.
* **Análisis de Sentimientos** : Determinar el tono de las reseñas (positivo, negativo, neutral).
* **Extracción de Temas** : Identificar los temas más comunes en las reseñas usando técnicas como LDA (Latent Dirichlet Allocation).
* **Resumen Automático** : Generar resúmenes automáticos de reseñas largas para obtener insights rápidos.

### **Implementación y Herramientas**

🔧  **Integración de Datos** :

* **ETL (Extract, Transform, Load)** : Pipelines para extracción, transformación y carga de datos.
* **Bases de Datos** : Utilizar bases de datos relacionales (PostgreSQL, MySQL) y no relacionales (MongoDB) para almacenar datos.

🛠️  **Herramientas de Análisis** :

* **Python** : Librerías como Pandas, NumPy, Scikit-learn, NLTK, SpaCy.
* **R** : Librerías como dplyr, ggplot2, caret, tm (text mining).
* **SQL** : Para consultas y gestión de bases de datos.

📊  **Visualización de Datos** :

* **Tableau** : Para crear dashboards interactivos.
* **Power BI** : Para informes y visualizaciones dinámicas.
* **Matplotlib y Seaborn** : Para visualización en Python.

### **Resumen**

🌟 Los datos principales se extraen de Yelp y Google Maps, con información detallada sobre ubicaciones comerciales, categorías de negocios, puntajes promedios, estado de apertura, datos de usuarios y reseñas.

📈 Estos datos se complementan con información sobre valores de acciones, datos geográficos adicionales, tendencias en redes sociales y noticias relevantes.

💬 El uso de técnicas avanzadas de Procesamiento de Lenguaje Natural (NLP) es crucial para analizar las reseñas y extraer insights significativos.

🚀 Estos insights pueden ser empleados para mejorar estrategias de marketing, desarrollar sistemas de recomendación personalizados y respaldar decisiones empresariales estratégicas.


### **Fuentes de datos**

+ [Diccionario de Datos](https://docs.google.com/document/d/1ASLMGAgrviicATaP1UJlflpmBCXtuSTHQGWdQMN6_2I/edit)

Fuentes de datos obligatorias:

+ [Dataset de Google Maps](https://drive.google.com/drive/folders/1Wf7YkxA0aHI3GpoHc9Nh8_scf5BbD4DA?usp=share_link)
+ [Dataset de Yelp!](https://drive.google.com/drive/folders/1TI-SsMnZsNP6t930olEEWbBQdo_yuIZF?usp=sharing)
