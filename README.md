# bienestar_app
Descripción.

bienestar_app es una aplicación de escritorio para gestionar usuarios y actividades en un Centro de Bienestar Comunitario. Permite registros, modificaciones, control de asistencias y generación de reportes.
Características

    - Registro y gestión de usuarios (nombre, edad, actividad, clases).
    - Cálculo automático de pagos.
    - Modificación y eliminación de usuarios.
    - Registro de asistencias.
    - Visualización de listado de inscritos y reportes analíticos con gráficos (distribución de edades, usuarios por actividad, etc.).

# Requisitos e Instalación

    Python 3.x
    Bibliotecas: pandas, matplotlib (Tkinter usualmente viene con Python).
    Bash

    pip install pandas matplotlib

    (Según requeriments.txt)

*¡Importante!* Configuración de datos.csv

    La lógica (logica.py) guarda en "datos/datos.csv".
    Los reportes (gui.py) leen de "datos.csv" (en la raíz del proyecto).


# En logica.py
    class GestorUsuarios:
        def __init__(self, archivo="datos.csv"): # Asegúrate que diga "datos.csv"
            self.archivo = archivo

Esto asegura que el archivo de datos datos.csv se cree y lea consistentemente desde la raíz del proyecto.

# Cómo Ejecutar

Desde el directorio del proyecto, ejecuta:

    Bash   
    python gui.py

## Uso Básico
* **Ventana Principal:** Ingresa datos del usuario y haz clic en "Registrar Usuario". Accede a otras funciones mediante los botones "Modificaciones" o "Mostrar Reporte".
* **Ventana de Modificaciones:** Permite eliminar usuarios, registrar asistencias, modificar datos de usuarios y mostrar un listado completo de inscritos.
* **Reportes:** Muestra estadísticas y gráficos sobre los usuarios y sus actividades.
