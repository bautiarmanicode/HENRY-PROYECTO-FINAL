import os
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Configuración de conexión a MySQL en AWS RDS
db_user = 'root'
db_password = 'root1234'
db_host = 'database-fl.c94uigocespw.us-east-2.rds.amazonaws.com'
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
    'df_business.parquet': 'yelp_business',
    'df_review.parquet': 'yelp_reviews',
    'df_checkin.parquet': 'yelp_checkins',
    'df_tip.parquet': 'yelp_tips',
    'df_user_yelp.parquet': 'yelp_users',
    'review-florida.parquet': 'google_reviews',
    'metadata-sitios.parquet': 'google_metadata'
}

# ETL para cada parte del proceso
def run_full_etl():
    negocios_unicos = etl_business()
    etl_review(negocios_unicos)
    etl_checkin(negocios_unicos)
    etl_tip()
    etl_user_yelp()
    etl_google_reviews()
    etl_google_metadata()
    run_etl()

def etl_business():
    # Lectura del archivo business.pkl
    df_business = pd.read_pickle('../0_Dataset/Data_Sucia/Yelp/business.pkl')
    df_business = df_business.loc[:, ~df_business.columns.duplicated()]
    df_business = df_business.dropna(subset=['categories'])
    df_restaurantes = df_business[df_business['categories'].str.lower().str.contains('restaurant')].reset_index(drop=True)

    # Fijamos los límites de latitud y longitud para filtrar los restaurantes en Florida
    latitud_max = 31.0
    latitud_min = 24.5
    longitud_max = -80.0
    longitud_min = -87.6

    # Se establecen las mascaras para filtrar el df
    mascara_latitud = (df_restaurantes['latitude'] >= latitud_min) & (df_restaurantes['latitude'] <= latitud_max)
    mascara_longitud = (df_restaurantes['longitude'] >= longitud_min) & (df_restaurantes['longitude'] <= longitud_max)

    # Se filtra el dataframe
    df_restaurantes_FL = df_restaurantes[mascara_latitud & mascara_longitud]
    df_restaurantes_FL = df_restaurantes_FL.reset_index(drop=True)

    # Se filtra por negocios abiertos y se elimina la columna que lo representa
    df_restaurantes_FL = df_restaurantes_FL[df_restaurantes_FL['is_open'] == 1].reset_index(drop=True)
    df_restaurantes_FL.drop(columns=['is_open', 'state'], inplace=True)

    # Definimos las categorías de interés
    categorias_interes = ['Pizza', 'Mexican']

    # Convertir la columna 'categories' a minúsculas y realizar la búsqueda para cada palabra clave
    condiciones = [df_restaurantes_FL['categories'].apply(lambda x: palabra.lower() in x.lower()) for palabra in categorias_interes]

    # Aplicar la lógica OR a las condiciones para obtener el DataFrame filtrado
    df_restaurantes_FL = df_restaurantes_FL[pd.concat(condiciones, axis=1).any(axis=1)]

    # Simplificamos la columna 'categories' para reflejar solo 'Pizza' o 'Mexican'
    df_restaurantes_FL['categories'] = df_restaurantes_FL['categories'].apply(lambda x: 'Pizza' if 'Pizza' in x else 'Mexican')

    # Eliminamos las columnas especificadas del DataFrame
    drop_columns = ['postal_code', 'attributes', 'hours']
    df_restaurantes_FL = df_restaurantes_FL.drop(columns=drop_columns)

    # Definimos los IDs únicos de business para usarlos posteriormente en el DataFrame de review
    negocios_unicos = df_restaurantes_FL['business_id'].unique().tolist()

    df_restaurantes_FL.to_parquet(os.path.join(yelp_dir, 'df_business.parquet'))
    return negocios_unicos

def etl_review(negocios_unicos):
    # Se determina la cantidad de datos por porción
    chunk_size = 50000
    # Se carga la info en un dataframe de pandas
    chunks = pd.read_json('../0_Dataset/Data_Sucia/Yelp/review.json', lines=True, chunksize=chunk_size)

    # Se crea una lista vacía donde se almacenarán los distintos dataframes
    dfs = []
    for chunk in chunks:
        dfs.append(chunk)

    # Se define el punto de corte para separar al dataframe en 2
    corte = int(len(dfs) / 2)

    # Se define la primera mitad del dataframe
    dfs1 = dfs[:corte]
    df_reviews1 = pd.concat(dfs1, axis=0, ignore_index=True)

    yelp_rev = df_reviews1[df_reviews1["business_id"].isin(negocios_unicos)]
    yelp_rev = yelp_rev.drop(columns=["useful", "funny", "cool"]).reset_index(drop=True)

    # Se define la segunda mitad del dataframe
    dfs2 = dfs[corte:]
    df_reviews2 = pd.concat(dfs2, axis=0, ignore_index=True)

    yelp_rev2 = df_reviews2[df_reviews2["business_id"].isin(negocios_unicos)]
    yelp_rev2 = yelp_rev2.drop(columns=["useful", "funny", "cool"]).reset_index(drop=True)

    yelp_rev = pd.concat([yelp_rev, yelp_rev2], axis=0, ignore_index=True)
    yelp_rev["date"] = pd.to_datetime(yelp_rev["date"]).dt.date

    yelp_rev.to_parquet(os.path.join(yelp_dir, 'df_review.parquet'))

def etl_checkin(negocios_unicos):
    # Abrimos el archivo
    df_checkin = pd.read_json('../0_Dataset/Data_Sucia/Yelp/checkin.json', lines=True)
    # Separamos por las comas y hacemos un explode
    df_checkin["date"] = df_checkin["date"].str.split(',')
    df_checkin = df_checkin.explode("date")
    df_checkin = df_checkin.reset_index(drop=True)

    # Filtramos por los negocios que vamos a analizar
    df_checkin = df_checkin[df_checkin["business_id"].isin(negocios_unicos)]
    df_checkin = df_checkin.reset_index(drop=True)

    # Modificamos los datos para que queden de la manera adecuada
    df_checkin["date"] = df_checkin["date"].str.strip()
    df_checkin["date"] = pd.to_datetime(df_checkin["date"])
    df_checkin["ano"] = df_checkin["date"].dt.year
    df_checkin["date"] = df_checkin["date"].dt.date

    df_checkin.to_parquet(os.path.join(yelp_dir, 'df_checkin.parquet'))

def etl_tip():
    # Abrimos el archivo
    df_tip_FL = pd.read_json('../0_Dataset/Data_Sucia/Yelp/tip.json', lines=True)

    # Elimino duplicados y columnas irrelevantes
    duplicados = df_tip_FL[df_tip_FL.duplicated(keep=False)]
    df_tip_FL = df_tip_FL.drop(columns="compliment_count")
    df_tip_FL = duplicados.drop_duplicates()

    df_tip_FL.to_parquet(os.path.join(yelp_dir, 'df_tip.parquet'))

def etl_user_yelp():
    # Abrimos el archivo
    df_user_FL = pd.read_parquet('../0_Dataset/Data_Sucia/Yelp/user-001.parquet')

    # Elimino columnas irrelevantes y borro duplicados
    columns_drop = ['useful', 'funny', 'cool', 'elite', 'friends', 'fans', 'compliment_hot', 'compliment_more', 'compliment_profile', 'compliment_cute', 'compliment_list',
                    'compliment_note', 'compliment_plain', 'compliment_cool', 'compliment_funny', 'compliment_writer',
                    'compliment_photos']
    df_user_FL = df_user_FL.drop(columns=columns_drop)
    df_user_FL.drop_duplicates(inplace=True)

    df_user_FL.to_parquet(os.path.join(yelp_dir, 'df_user_yelp.parquet'))

def etl_google_reviews():
    # Dataframe review-florida
    carpeta_1 = "../0_Dataset/Data_Sucia/Google/review-Florida"

    # Se crea lista vacía donde se almacenarán los dataframes de cada archivo
    reviews = []

    # Se recorre por todos los archivos en la carpeta
    for filename in os.listdir(carpeta_1):
        if filename.endswith('.json'):
            # Se carga el archivo JSON en un DataFrame de Pandas
            filepath = os.path.join(carpeta_1, filename)
            df_reviews_Google = pd.read_json(filepath, lines=True)
            # Se agrega el DataFrame a la lista
            reviews.append(df_reviews_Google)

    # Combinar todos los DataFrames en uno solo y llamarlo df_reviews_Google
    df_reviews_Google = pd.concat(reviews, ignore_index=True)
    df_reviews_Google = df_reviews_Google.drop(columns=["pics", "resp"])

    # Creamos la función que asignará la escala de satisfacción
    def asignar_escala(rating):
        if rating <= 1:
            return "Very Dissatisfied"
        elif rating <= 2:
            return "Dissatisfied"
        elif rating <= 3:
            return "Neutral"
        elif rating <= 4:
            return "Satisfied"
        else:
            return "Very Satisfied"

    # Luego creamos una columna en el dataframe donde aplicamos la función creada anteriormente
    df_reviews_Google["escala_satisfaccion"] = df_reviews_Google["rating"].apply(asignar_escala)

    # Rellenamos los valores NaN en la columna 'text' con los valores de 'escala_satisfaccion'
    df_reviews_Google["text"] = df_reviews_Google["text"].fillna(df_reviews_Google["escala_satisfaccion"])

    # Eliminamos la columna agregada anteriormente
    df_reviews_Google = df_reviews_Google.drop(columns="escala_satisfaccion")

    # Creamos una función para obtener el timestamp en segundos
    def convertir_timestamp(milisegundo):
        timestamp_seg = milisegundo / 1000
        fecha_hora = datetime.utcfromtimestamp(timestamp_seg)
        return fecha_hora

    # Verificamos si la columna "time" existe en df_reviews_Google y si es un DataFrame
    if isinstance(df_reviews_Google, pd.DataFrame) and 'time' in df_reviews_Google.columns:
        # Creamos la columna "fecha" utilizando la función creada anteriormente
        df_reviews_Google["fecha"] = df_reviews_Google["time"].apply(convertir_timestamp)

    df_reviews_Google.to_parquet(os.path.join(google_dir, 'review-florida.parquet'))

def etl_google_metadata():
    # Dataframe metadata-sitios
    carpeta_metadata = "../0_Dataset/Data_Sucia/Google/metadata-sitios"

    # Se crea lista vacía donde se almacenarán los dataframes de cada archivo
    metadata_list = []

    # Se recorre por todos los archivos en la carpeta
    for file in os.listdir(carpeta_metadata):
        if file.endswith('.json'):
            # Se carga el archivo JSON en un DataFrame de Pandas
            path = os.path.join(carpeta_metadata, file)
            df = pd.read_json(path, lines=True)
            # Se agrega el DataFrame a la lista
            metadata_list.append(df)

    # Combinar todos los DataFrames en uno solo y llamarlo df_metadata
    df_metadata = pd.concat(metadata_list, ignore_index=True)
    df_metadata = df_metadata.drop(columns=["address", "price", "hours", "state", "relative_results", "url", "MISC", "description"])

    # Observamos el total de categorías comprendidas en los locales
    categorias = df_metadata["category"].explode().unique()
    # Eliminamos valores faltantes en "name"
    df_metadata = df_metadata.dropna(subset="name")

    # Se abre el dataframe en las diferentes categorías
    apertura_cat = df_metadata.explode("category")
    df_metadata = apertura_cat.reset_index()

    df_metadata = df_metadata[df_metadata['category'].isin(['Pizza', 'Mexican restaurant', 'Pizza restaurant'])]
    df_metadata.loc[df_metadata['category'] == 'Pizza restaurant', 'category'] = 'Pizza'
    df_metadata.loc[df_metadata['category'] == 'Mexican restaurant', 'category'] = 'Mexican'

    df_metadata.to_parquet(os.path.join(google_dir, 'metadata-sitios.parquet'))

def extract_data(file_path):
    df = pd.read_parquet(file_path)
    return df

def transform_data(df):
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
    
    if 'rating' in df.columns and ((df['rating'] < 1).any() or (df['rating'] > 5).any()):
        print(f"Error: La columna 'rating' contiene valores fuera del rango esperado en la tabla {table_name}.")
        return False

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
    for file_name in os.listdir(google_dir):
        if file_name in file_to_table_map:
            process_file(os.path.join(google_dir, file_name), file_to_table_map[file_name])

    for file_name in os.listdir(yelp_dir):
        if file_name in file_to_table_map:
            process_file(os.path.join(yelp_dir, file_name), file_to_table_map[file_name])

if __name__ == "__main__":
    run_full_etl()
