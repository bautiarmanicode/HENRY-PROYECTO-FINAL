import streamlit as st
import pandas as pd
from textblob import TextBlob
import os

@st.cache_data
def load_parquet_file(file_path):
    if os.path.exists(file_path):
        return pd.read_parquet(file_path)
    else:
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

def obtener_sentimiento(texto):
    analisis = TextBlob(texto)
    if analisis.sentiment.polarity > 0:
        return 'Positivo'
    elif analisis.sentiment.polarity < 0:
        return 'Negativo'
    else:
        return 'Neutral'

def main():
    st.title('Análisis de Sentimiento de Reseñas')

    google_maps_file_path = 'C:\\Users\\loren\\Documents\\GitHub\\HENRY-PROYECTO-FINAL\\0_Dataset\\Data_Limpia\\Google\\G_review_FL_reducido.parquet'
    yelp_file_path = 'C:\\Users\\loren\\Documents\\GitHub\\HENRY-PROYECTO-FINAL\\0_Dataset\\Data_Limpia\\Yelp\\review_FL_reducido.parquet'

    with st.spinner('Cargando datos de Google Maps...'):
        df_google_maps = load_parquet_file(google_maps_file_path)
        st.success('Datos de Google Maps cargados')

    with st.spinner('Cargando datos de Yelp...'):
        df_yelp = load_parquet_file(yelp_file_path)
        st.success('Datos de Yelp cargados')

    st.write('Datos de Google Maps y Yelp cargados exitosamente.')

    df_google_maps = df_google_maps.rename(columns={'rating': 'stars', 'time': 'date'})
    df_yelp = df_yelp.rename(columns={'stars': 'rating'})

    df_reviews = pd.concat([df_google_maps, df_yelp], ignore_index=True)
    df_reviews['text'] = df_reviews['text'].fillna('')
    df_reviews['sentimiento'] = df_reviews['text'].apply(obtener_sentimiento)

    # Convertir la columna 'date' a formato datetime
    df_reviews['date'] = pd.to_datetime(df_reviews['date'], errors='coerce')
    df_reviews = df_reviews.dropna(subset=['date'])  # Eliminar filas con fechas inválidas

    # Crear la aplicación Streamlit
    business_ids = df_reviews['business_id'].unique()
    selected_business_id = st.selectbox('Selecciona un Business ID', business_ids)

    df_filtered = df_reviews[df_reviews['business_id'] == selected_business_id]
    years = df_filtered['date'].dt.year.unique()
    selected_year = st.selectbox('Selecciona un Año', years)

    df_filtered = df_filtered[df_filtered['date'].dt.year == selected_year]

    st.write('Primeras filas de las reseñas filtradas:', df_filtered.head())

    sentimiento_resumen = df_filtered['sentimiento'].value_counts(normalize=True) * 100
    st.write('Resumen del Sentimiento:', sentimiento_resumen)

    st.bar_chart(sentimiento_resumen)

if __name__ == '__main__':
    main()



