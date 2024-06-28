import os
import pandas as pd
from sqlalchemy import create_engine

# Configuración de conexión a MySQL en AWS RDS
db_user = 'root'
db_password = 'root1234'
db_host = 'http://database-fl.c94uigocespw.us-east-2.rds.amazonaws.com/'
db_name = 'database-fl'

# Crear conexión con SQLAlchemy
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}')

# Rutas a los directorios de los archivos Parquet
google_dir = 'Data_Limpia/Google/'
yelp_dir = 'Data_Limpia/Yelp/'

# Mapeo de archivos a tablas en MySQL
file_to_table_map = {
    'G_metadata_FL.parquet': 'google_metadata',
    'reviews_FL.parquet': 'google_reviews',
    'business.parquet': 'yelp_business',
    'reviews.parquet': 'yelp_reviews',
    'users.parquet': 'yelp_users',
    'checkins.parquet': 'yelp_checkins',
    'tips.parquet': 'yelp_tips'
}

def extract_data(file_path):
    # Extracción de datos desde archivo Parquet
    df = pd.read_parquet(file_path)
    return df

def transform_data(df):
    # Manejo de valores nulos y limpieza de datos
    df['categories'] = df['categories'].fillna('Unknown')
    df['text'] = df['text'].fillna('')
    df['pics'] = df['pics'].apply(lambda x: [] if pd.isna(x) else x)
    df['resp'] = df['resp'].apply(lambda x: {} if pd.isna(x) else x)
    df['address'] = df['address'].fillna('Unknown')
    df['description'] = df['description'].fillna('No description')
    df['category'] = df['category'].apply(lambda x: [] if pd.isna(x) else x)
    df['price'] = df['price'].fillna('Unknown')
    df['hours'] = df['hours'].apply(lambda x: {} if pd.isna(x) else x)
    df['MISC'] = df['MISC'].apply(lambda x: {} if pd.isna(x) else x)
    df['state'] = df['state'].fillna('Unknown')
    df['relative_results'] = df['relative_results'].apply(lambda x: [] if pd.isna(x) else x)
    return df

def validate_data(df):
    # Validación de datos para columnas críticas
    critical_columns = ['name', 'address', 'gmap_id']
    for col in critical_columns:
        if col in df.columns and df[col].isnull().any():
            print(f"Error: La columna {col} contiene valores nulos.")
            return False
    return True

def load_data(df, table_name):
    # Carga de datos a MySQL en AWS RDS
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

def process_file(file_path, table_name):
    df = extract_data(file_path)
    df_cleaned = transform_data(df)
    if validate_data(df_cleaned):
        load_data(df_cleaned, table_name)
        print(f"Datos de {file_path} cargados exitosamente en la tabla {table_name}")
    else:
        print(f"Validación fallida para {file_path}. Datos no cargados.")

def run_etl():
    # Procesamiento de archivos Parquet en directorio Google
    for file_name in os.listdir(google_dir):
        if file_name in file_to_table_map:
            process_file(os.path.join(google_dir, file_name), file_to_table_map[file_name])

    # Procesamiento de archivos Parquet en directorio Yelp
    for file_name in os.listdir(yelp_dir):
        if file_name in file_to_table_map:
            process_file(os.path.join(yelp_dir, file_name), file_to_table_map[file_name])

if __name__ == "__main__":
    run_etl()
