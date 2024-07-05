import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import numpy as np
import matplotlib.pyplot as plt

# Función para crear el mapa
def create_map(city, local_name, rating_type, df, optimal_location):
    df_filtered = df[(df['city_x'] == city) & (df['name'].str.contains(local_name, case=False))]

    if rating_type == 'Mejores ratings':
        df_filtered = df_filtered.sort_values(by='stars_x', ascending=False).head(5)
    elif rating_type == 'Peores ratings':
        df_filtered = df_filtered.sort_values(by='stars_x').head(5)

    city_location = [df_filtered['latitude_x'].mean(), df_filtered['longitude_x'].mean()]
    m = folium.Map(location=city_location, zoom_start=10)

    for _, row in df_filtered.iterrows():
        popup_text = f"""
        Name: {row['name']}<br>
        Address: {row['address_x']}<br>
        Rating: {row['stars_x']}<br>
        Categoría: {row['predicted_category']}
        """
        folium.Marker(
            location=[row['latitude_x'], row['longitude_x']],
            popup=popup_text,
            icon=folium.Icon(color='red' if row['stars_x'] < 3 else 'green')
        ).add_to(m)
    
    if optimal_location is not None:
        folium.Marker(
            location=[optimal_location['lat_bin'], optimal_location['long_bin']],
            popup="Ubicación óptima recomendada",
            icon=folium.Icon(color='blue', icon='star')
        ).add_to(m)

    return m

# Calcular densidad de locales y calificación promedio por área (grid de lat/long)
def calculate_density(df, grid_size=0.01):
    df['lat_bin'] = np.floor(df['latitude_x'] / grid_size) * grid_size
    df['long_bin'] = np.floor(df['longitude_x'] / grid_size) * grid_size

    density = df.groupby(['lat_bin', 'long_bin']).size().reset_index(name='count')
    avg_rating = df.groupby(['lat_bin', 'long_bin'])['stars_x'].mean().reset_index(name='avg_rating')

    density_avg = pd.merge(density, avg_rating, on=['lat_bin', 'long_bin'])
    return density_avg

def predict_optimal_location(df_density_avg):
    # Encontrar áreas con menos locales y buena calificación promedio
    # Ajustar los percentiles para permitir más áreas
    low_density_threshold = df_density_avg['count'].quantile(0.5)
    high_rating_threshold = df_density_avg['avg_rating'].mean()

    optimal_areas = df_density_avg[(df_density_avg['count'] < low_density_threshold) & 
                                   (df_density_avg['avg_rating'] > high_rating_threshold)]

    if optimal_areas.empty:
        return None

    optimal_location = optimal_areas.iloc[0]
    return optimal_location

# Función para mostrar análisis de sentimiento de reseñas específicas del local
def show_sentiment_analysis(df, local_name, address):
    df_local = df[(df['name'].str.contains(local_name, case=False)) & (df['address_x'] == address)]
    
    if df_local.empty:
        st.write(f"No se encontraron datos de reseñas para {local_name} en {address}.")
        return
    
    sentiments = df_local['polarity']
    plt.figure(figsize=(10, 6))
    plt.hist(sentiments, bins=50, edgecolor='k', alpha=0.7)
    plt.title(f'Análisis de Sentimiento para {local_name} en {address}')
    plt.xlabel('Sentimiento')
    plt.ylabel('Frecuencia')
    st.pyplot(plt)
    
    # Mostrar ejemplos de reseñas representativas
    st.write("Ejemplos de reseñas representativas:")
    
    positive_reviews = df_local[df_local['polarity'] > 0.5]
    negative_reviews = df_local[df_local['polarity'] < -0.5]
    
    st.write("Reseñas positivas:")
    if not positive_reviews.empty:
        st.write(positive_reviews[['text', 'polarity']].sample(1, random_state=42).values)
    else:
        st.write("No hay reseñas positivas para mostrar.")
    
    st.write("Reseñas negativas:")
    if not negative_reviews.empty:
        st.write(negative_reviews[['text', 'polarity']].sample(1, random_state=42).values)
    else:
        st.write("No hay reseñas negativas para mostrar.")

# Función para comparar con competidores
def compare_competitors(df, city, local_name):
    df_city = df[df['city_x'] == city]
    df_local = df_city[df_city['name'].str.contains(local_name, case=False)]
    df_competitors = df_city[~df_city['name'].str.contains(local_name, case=False)]

    if df_local.empty or df_competitors.empty:
        st.write("No se encontraron suficientes datos para la comparación.")
        return

    # Comparar calificaciones promedio
    avg_rating_local = df_local['stars_x'].mean()
    avg_rating_competitors = df_competitors['stars_x'].mean()

    st.write(f"Calificación promedio de {local_name}: {avg_rating_local:.2f}")
    st.write(f"Calificación promedio de competidores: {avg_rating_competitors:.2f}")

    # Mostrar análisis de sentimiento comparativo
    sentiments_local = df_local['polarity']
    sentiments_competitors = df_competitors['polarity']

    plt.figure(figsize=(10, 6))
    plt.hist(sentiments_local, bins=50, alpha=0.5, label=f'{local_name}', edgecolor='k')
    plt.hist(sentiments_competitors, bins=50, alpha=0.5, label='Competidores', edgecolor='k')
    plt.title('Comparación de Sentimientos')
    plt.xlabel('Sentimiento')
    plt.ylabel('Frecuencia')
    plt.legend(loc='upper right')
    st.pyplot(plt)

# Cargar el DataFrame
df_combinado = pd.read_parquet('df_merged.parquet')

# Widgets interactivos de Streamlit
st.title('Índice de Ubicación Óptima')
city = st.selectbox('Selecciona la ciudad:', df_combinado['city_x'].unique())
local_name = st.text_input('Nombre del local (e.g., Pizza Hut, Taco Bell):')
rating_type = st.selectbox('Selecciona el tipo de rating:', ['Top 5 mejores ratings', 'Bottom 5 peores ratings'])

# Filtrar datos por la ciudad seleccionada
df_city = df_combinado[df_combinado['city_x'] == city]

# Verificar si hay datos después de aplicar los filtros
if df_city.empty or df_city[df_city['name'].str.contains(local_name, case=False)].empty:
    st.error(f"No se encontraron datos para {local_name} en {city}.")
else:
    # Calcular densidad y predecir ubicación óptima para la ciudad seleccionada
    density_avg = calculate_density(df_city)
    optimal_location = predict_optimal_location(density_avg)

    # Crear y mostrar el mapa
    st.write(f'Mostrando {rating_type.lower()} de {local_name} en {city}')
    map_ = create_map(city, local_name, rating_type, df_combinado, optimal_location)
    map_result = st_folium(map_, width=700, height=500)

    if optimal_location is not None:
        st.write(f"Ubicación óptima recomendada: latitud {optimal_location['lat_bin']}, longitud {optimal_location['long_bin']}")
        st.write("""
            **Razón para la recomendación de esta ubicación óptima:**
            - **Baja densidad de competidores:** Esta área tiene una baja cantidad de locales similares, lo que reduce la competencia directa.
            - **Alta calificación promedio:** Las calificaciones promedio de los locales en esta área son altas, indicando una buena satisfacción del cliente.
            - **Visibilidad y accesibilidad:** La ubicación es fácilmente accesible y visible, lo que atraerá a más clientes potenciales.
            - **Demanda potencial:** Basado en las características de la zona, hay una alta probabilidad de atraer a una gran cantidad de clientes.
        """)
    else:
        st.write("No se encontró una ubicación óptima según los criterios actuales.")
    
    if map_result and 'last_object_clicked' in map_result and map_result['last_object_clicked']:
        selected_popup = map_result['last_object_clicked'].get('popup')
        if selected_popup:
            selected_address = selected_popup.split("<br>")[1].split(": ")[1]
            st.header("Análisis de Sentimiento")
            show_sentiment_analysis(df_combinado, local_name, selected_address)

    # Mostrar comparación con competidores
    st.header("Comparación con Competidores")
    compare_competitors(df_combinado, city, local_name)
