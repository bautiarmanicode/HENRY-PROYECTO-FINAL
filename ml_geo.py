import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import os

@st.cache_data
def load_parquet_file(file_path):
    if os.path.exists(file_path):
        return pd.read_parquet(file_path)
    else:
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

def main():
    st.title('Geolocalización de Negocios y Rankings')

    google_maps_file_path = r'C:\Users\loren\Documents\GitHub\HENRY-PROYECTO-FINAL\0_Dataset\Data_Limpia\Google\G_review_FL_reducido.parquet'
    yelp_file_path = r'C:\Users\loren\Documents\GitHub\HENRY-PROYECTO-FINAL\0_Dataset\Data_Limpia\Yelp\review_FL_reducido.parquet'
    business_file_path = r'C:\Users\loren\Documents\GitHub\HENRY-PROYECTO-FINAL\0_Dataset\Data_Limpia\Yelp\business.parquet'

    # Cargar los datos de Google Maps
    with st.spinner('Cargando datos de Google Maps...'):
        try:
            df_google_maps = load_parquet_file(google_maps_file_path)
            st.success('Datos de Google Maps cargados')
        except FileNotFoundError as e:
            st.error(e)
            return

    # Cargar los datos de Yelp
    with st.spinner('Cargando datos de Yelp...'):
        try:
            df_yelp = load_parquet_file(yelp_file_path)
            st.success('Datos de Yelp cargados')
        except FileNotFoundError as e:
            st.error(e)
            return

    # Cargar los datos de negocios
    with st.spinner('Cargando datos de negocios...'):
        try:
            df_business = load_parquet_file(business_file_path)
            st.success('Datos de negocios cargados')
        except FileNotFoundError as e:
            st.error(e)
            return

    st.write('Datos de Google Maps, Yelp y negocios cargados exitosamente.')

    # Renombrar columnas para unificar formato
    df_google_maps = df_google_maps.rename(columns={'rating': 'stars', 'time': 'date'})
    df_yelp = df_yelp.rename(columns={'stars': 'rating'})

    # Concatenar ambos DataFrames de reseñas
    df_reviews = pd.concat([df_google_maps, df_yelp], ignore_index=True)

    # Convertir la columna 'date' a formato datetime
    df_reviews['date'] = pd.to_datetime(df_reviews['date'], errors='coerce')
    df_reviews = df_reviews.dropna(subset=['date'])  # Eliminar filas con fechas inválidas

    # Unir los DataFrames de reseñas con el DataFrame de negocios
    df_reviews = df_reviews.merge(df_business[['business_id', 'latitude', 'longitude', 'city']], on='business_id', how='left')

    # Filtrar por ciudades y rankings
    cities = df_reviews['city'].dropna().unique()
    selected_city = st.selectbox('Selecciona una Ciudad', cities)

    df_city_filtered = df_reviews[df_reviews['city'] == selected_city]

    st.write(f'Negocios en {selected_city}:')

    # Peores rankings
    top_n = st.slider('Selecciona el número de negocios con peores rankings', 1, 20, 5)
    df_worst = df_city_filtered.nsmallest(top_n, 'rating')
    st.write('Negocios con peores rankings:', df_worst[['name', 'rating', 'latitude', 'longitude']])

    # Mapas de negocios
    if not df_city_filtered.empty:
        m = folium.Map(location=[df_city_filtered['latitude'].mean(), df_city_filtered['longitude'].mean()], zoom_start=12)

        for _, row in df_worst.iterrows():
            if pd.notna(row['latitude']) and pd.notna(row['longitude']):
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup=f"{row['name']} (Rating: {row['rating']})",
                    icon=folium.Icon(color='red')
                ).add_to(m)

        folium_static(m)
    else:
        st.warning('No hay datos para mostrar en el mapa.')

if __name__ == '__main__':
    main()
