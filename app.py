import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import streamlit as st

def load_reviews(file_path):
    df = pd.read_csv(file_path)
    return df

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def add_sentiment_column(df):
    df['sentiment'] = df['text'].apply(analyze_sentiment)
    return df

def save_results(df, output_path):
    df.to_csv(output_path, index=False)

def calculate_kpi(df):
    positive_reviews = df[df['sentiment'] > 0.1].shape[0]
    negative_reviews = df[df['sentiment'] < -0.1].shape[0]
    neutral_reviews = df[(df['sentiment'] <= 0.1) & (df['sentiment'] >= -0.1)].shape[0]
    total_reviews = df.shape[0]

    positive_percentage = (positive_reviews / total_reviews) * 100
    negative_percentage = (negative_reviews / total_reviews) * 100
    neutral_percentage = (neutral_reviews / total_reviews) * 100

    return positive_percentage, negative_percentage, neutral_percentage

def main():
    st.title("Análisis de Sentimiento de Reseñas")

    # Ruta al archivo CSV que contiene las reseñas y resultados del análisis de sentimiento
    input_file_path = '1 Jupyter Notebooks/sentiment_analysis_results.csv'
    
    # Cargar reseñas
    reviews_df = load_reviews(input_file_path)

    # Mostrar las primeras filas del DataFrame
    st.write("Primeras filas del DataFrame:")
    st.write(reviews_df.head())

    # Mostrar información del DataFrame
    st.write("Información del DataFrame:")
    st.write(reviews_df.info())

    sentiment_avg_by_category = reviews_df.groupby('business_id')['sentiment'].mean().reset_index()
    st.write("Promedio de polaridad de sentimiento por categoría de negocio:")
    st.write(sentiment_avg_by_category.head())

    plt.hist(reviews_df['sentiment'], bins=50, color='blue', edgecolor='black')
    plt.title('Distribución de Sentimientos')
    plt.xlabel('Polaridad del Sentimiento')
    plt.ylabel('Frecuencia')
    st.pyplot(plt.gcf())

    most_positive_reviews = reviews_df.nlargest(5, 'sentiment')
    st.write("Reseñas más positivas:")
    st.write(most_positive_reviews[['text', 'sentiment']])

    most_negative_reviews = reviews_df.nsmallest(5, 'sentiment')
    st.write("Reseñas más negativas:")
    st.write(most_negative_reviews[['text', 'sentiment']])

    positive_percentage, negative_percentage, neutral_percentage = calculate_kpi(reviews_df)
    st.write(f"Porcentaje de reseñas positivas: {positive_percentage:.2f}%")
    st.write(f"Porcentaje de reseñas negativas: {negative_percentage:.2f}%")
    st.write(f"Porcentaje de reseñas neutrales: {neutral_percentage:.2f}%")

    sentiment_avg_by_category.to_csv('sentiment_avg_by_category.csv', index=False)
    st.success("Promedio de polaridad de sentimiento por categoría guardado en 'sentiment_avg_by_category.csv'")

if __name__ == "__main__":
    main()
