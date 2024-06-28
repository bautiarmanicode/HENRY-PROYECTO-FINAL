import pandas as pd
from sqlalchemy import create_engine
import pymysql

# Conexión a MySQL
engine = create_engine('mysql+pymysql://username:password@localhost/yelp_google')

def load_data_from_json(file_path):
    return pd.read_json(file_path, lines=True)

def clean_user_data(df):
    df['yelping_since'] = pd.to_datetime(df['yelping_since'])
    df.fillna({'elite': '', 'average_stars': 0, 'useful': 0, 'funny': 0, 'cool': 0}, inplace=True)
    return df

def clean_business_data(df):
    df.fillna({'address': '', 'city': '', 'state': '', 'postal_code': '', 'categories': ''}, inplace=True)
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df.dropna(subset=['latitude', 'longitude'], inplace=True)
    return df

def clean_review_data(df):
    df['text'] = df['text'].fillna('')
    df['pics'] = df['pics'].fillna('').astype(str)
    df['resp'] = df['resp'].fillna('').astype(str)
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['user_id', 'business_id', 'rating', 'date'], inplace=True)
    return df

def load_data_to_mysql(df, table_name):
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

# Ruta de los archivos JSON
user_file_path = 'path/to/user.json'
business_file_path = 'path/to/business.json'
review_file_path = 'path/to/review.json'

# Carga y limpieza de datos
user_df = load_data_from_json(user_file_path)
user_df = clean_user_data(user_df)

business_df = load_data_from_json(business_file_path)
business_df = clean_business_data(business_df)

review_df = load_data_from_json(review_file_path)
review_df = clean_review_data(review_df)

# Carga de datos en MySQL
load_data_to_mysql(user_df, 'Dim_User')
load_data_to_mysql(business_df, 'Dim_Business')
load_data_to_mysql(review_df, 'Fact_Review')
