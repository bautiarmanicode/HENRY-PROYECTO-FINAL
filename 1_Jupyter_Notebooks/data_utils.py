# Funciones utiles para ETL Y EDA
from textblob import TextBlob
import datetime
import inspect
import re
import matplotlib.pyplot as plt
import inspect
import pandas as pd
import gzip
import os

def data_type_check(df):
    """
    Genera un resumen del DataFrame que incluye la proporción de valores nulos y no nulos, 
    el tipo de datos y la cantidad total de nulos por columna.

    Parámetros:
    df (pandas.DataFrame): El DataFrame a ser analizado.

    Retorna:
    None: Esta función imprime el resumen del DataFrame en la consola.
    """
    # Crear un diccionario para almacenar el resumen de los datos
    dataframe = {
        "columna": [], 
        "%_no_nulos": [], 
        "%_nulos": [], 
        "total_nulos": [], 
        "tipo_dato": []
    }
    
    # Encabezado del resumen
    print("\n" + "=" * 40)
    print(" Resumen del dataframe:")
    print("\n" + "=" * 40)
    
    for columna in df.columns:
        # Calcular el porcentaje de valores no nulos
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        # Obtener el tipo de dato directamente
        tipo_dato = df[columna].dtype  
        # Agregar la información al diccionario
        dataframe["columna"].append(columna)
        dataframe["%_no_nulos"].append(round(porcentaje_no_nulos, 2))
        dataframe["%_nulos"].append(round(100 - porcentaje_no_nulos, 2))
        dataframe["total_nulos"].append(df[columna].isnull().sum())
        dataframe["tipo_dato"].append(tipo_dato)
    
    # Crear el DataFrame con la información recopilada
    df_info = pd.DataFrame(dataframe)
    print("Dimensiones: ", df.shape)
    print(df_info) 
    
