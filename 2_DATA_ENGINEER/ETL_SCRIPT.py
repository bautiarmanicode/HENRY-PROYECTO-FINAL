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

# Obtén la ruta absoluta del directorio en el que se encuentra este script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construye las rutas absolutas a los directorios de los archivos Parquet
google_dir = os.path.join(base_dir, 'Data_Limpia', 'Google')
yelp_dir = os.path.join(base_dir, 'Data_Limpia', 'Yelp')

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
    if 'categories' in df.columns:
        df['categories'] = df['categories'].fillna('Unknown')
    if 'text' in df.columns:
        df['text'] = df['text'].fillna('')
    if 'pics' in df.columns:
        df['pics'] = df['pics'].apply(lambda x: [] if pd.isna(x) else x)
    if 'resp' in df.columns:
        df['resp'] = df['resp'].apply(lambda x: {} if pd.isna(x) else x)
    if 'address' in df.columns:
        df['address'] = df['address'].fillna('Unknown')
    if 'description' in df.columns:
        df['description'] = df['description'].fillna('No description')
    if 'category' in df.columns:
        df['category'] = df['category'].apply(lambda x: [] if pd.isna(x) else x)
    if 'price' in df.columns:
        df['price'] = df['price'].fillna('Unknown')
    if 'hours' in df.columns:
        df['hours'] = df['hours'].apply(lambda x: {} if pd.isna(x) else x)
    if 'MISC' in df.columns:
        df['MISC'] = df['MISC'].apply(lambda x: {} if pd.isna(x) else x)
    if 'state' in df.columns:
        df['state'] = df['state'].fillna('Unknown')
    if 'relative_results' in df.columns:
        df['relative_results'] = df['relative_results'].apply(lambda x: [] if pd.isna(x) else x)
    return df

def validate_data(df, table_name):
    # Validación de datos para columnas críticas
    validations = {
        'google_metadata': ['name', 'address', 'gmap_id'],
        'google_reviews': ['user_id', 'gmap_id', 'rating'],
        'yelp_business': ['business_id', 'name', 'address'],
        'yelp_reviews': ['review_id', 'user_id', 'business_id'],
        'yelp_users': ['user_id', 'name'],
        'yelp_checkins': ['business_id'],
        'yelp_tips': ['text', 'business_id', 'user_id']
    }
    
    critical_columns = validations.get(table_name, [])
    for col in critical_columns:
        if col in df.columns and df[col].isnull().any():
            print(f"Error: La columna {col} contiene valores nulos en la tabla {table_name}.")
            return False
    
    # Validación de rango de valores (ejemplo para ratings)
    if 'rating' in df.columns and ((df['rating'] < 1).any() or (df['rating'] > 5).any()):
        print(f"Error: La columna 'rating' contiene valores fuera del rango esperado en la tabla {table_name}.")
        return False

    # Validación de duplicados en base a columnas clave
    key_columns = {
        'google_metadata': ['gmap_id'],
        'google_reviews': ['user_id', 'gmap_id'],
        'yelp_business': ['business_id'],
        'yelp_reviews': ['review_id'],
        'yelp_users': ['user_id'],
        'yelp_checkins': ['business_id'],
        'yelp_tips': ['business_id', 'user_id']
    }
    
    keys = key_columns.get(table_name, [])
    if keys and df.duplicated(subset=keys).any():
        print(f"Error: Hay duplicados en las columnas clave {keys} en la tabla {table_name}.")
        return False

    return True

def load_data(df, table_name):
    # Carga de datos a MySQL en AWS RDS
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

def process_file(file_path, table_name):
    df = extract_data(file_path)
    df_cleaned = transform_data(df)
    if validate_data(df_cleaned, table_name):
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