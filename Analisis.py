import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(archivo="datos.csv"):
    try:
        return pd.read_csv(archivo)
    except FileNotFoundError:
        return pd.DataFrame()
