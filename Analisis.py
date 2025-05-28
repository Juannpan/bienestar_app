import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(archivo="datos.csv"):
    try:
        return pd.read_csv(archivo)
    except FileNotFoundError:
        return pd.DataFrame()
    
def generar_reporte():
    df = cargar_datos()
    if df.empty:
        print("No hay datos para analizar.")
        return

    print(f"Total de usuarios registrados: {len(df)}")
    print(f"Usuarios con datos incompletos:\n{df[df.isnull().any(axis=1)]}")
    print(f"Promedio de pagos: ${df['valor_pagado'].mean():,.2f}")
    print(f"Actividad con más inscritos: {df['actividad'].mode()[0]}")
    print(f"Usuario que más ha pagado:\n{df.loc[df['valor_pagado'].idxmax()]}")

    df["edad"].plot.hist(bins=10, title="Distribución de edades")
    plt.xlabel("Edad")
    plt.show()

    df["actividad"].value_counts().plot(kind="bar", title="Usuarios por actividad", color="skyblue")
    plt.ylabel("Cantidad de usuarios")
    plt.show()

    df["actividad"].value_counts().plot.pie(autopct="%1.1f%%", title="Distribución por actividad")
    plt.ylabel("")
    plt.show()