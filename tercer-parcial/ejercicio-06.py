# Graficar MySQL
import os
import sys

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


def crear_conexion():
    """Crea una conexion usando variables de entorno para evitar credenciales fijas."""
    config = {
        "host": os.getenv("MYSQL_HOST", "localhost"),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DATABASE", "pruebas"),
    }

    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print(f"Error de conexion MySQL: {err}")
        print("Configura tus credenciales antes de ejecutar, por ejemplo:")
        print("export MYSQL_HOST=localhost")
        print("export MYSQL_USER=tu_usuario")
        print("export MYSQL_PASSWORD=tu_password")
        print("export MYSQL_DATABASE=pruebas")
        sys.exit(1)


def consultar_dataframe(conexion, query):
    """Ejecuta un query y devuelve un DataFrame sin usar SQLAlchemy."""
    cursor = conexion.cursor(dictionary=True)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return pd.DataFrame(rows)


conexion = crear_conexion()

# Prueba de conexion
my_data1 = consultar_dataframe(conexion, "SELECT * FROM productos")
my_data2 = consultar_dataframe(
    conexion,
    "SELECT c.categoria, sum(p.cantidad) as total "
    "FROM productos as p "
    "INNER JOIN categorias as c ON p.categoria_id = c.id "
    "GROUP BY c.categoria",
)
labels = my_data2["categoria"].tolist()
my_data2["total"] = pd.to_numeric(my_data2["total"], errors="coerce")
print(my_data2)

my_data2.plot(y="total", kind="pie", autopct="%1.01f%%", labels=labels, legend=False)
plt.title("Porcentaje por categorias")
if "agg" in plt.get_backend().lower():
    output_path = "grafico_categorias_mysql.png"
    plt.savefig(output_path, dpi=120, bbox_inches="tight")
    print(f"Grafica guardada en {output_path} (entorno no interactivo).")
else:
    plt.show()

conexion.close()