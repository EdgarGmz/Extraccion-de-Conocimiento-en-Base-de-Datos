import mysql.connector
import pandas as pd
import plotly.express as px
import os
import sys


def crear_conexion_mysql():
    """Crea la conexion usando variables de entorno para evitar credenciales hardcodeadas."""
    config = {
        "host": os.getenv("MYSQL_HOST", "localhost"),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DATABASE", "ecbd"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
    }

    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        # En Ubuntu, root suele usar auth_socket y rechaza password vacio por TCP.
        if getattr(err, "errno", None) == 1698:
            print(
                "Error 1698: acceso denegado para root@localhost. "
                "Configura un usuario/password de MySQL en variables de entorno:\n"
                "  export MYSQL_HOST=localhost\n"
                "  export MYSQL_PORT=3306\n"
                "  export MYSQL_USER=tu_usuario\n"
                "  export MYSQL_PASSWORD=tu_password\n"
                "  export MYSQL_DATABASE=ecbd\n"
                "Luego vuelve a ejecutar: python3 ejercicio-08.py"
            )
            sys.exit(1)
        if getattr(err, "errno", None) == 1045:
            print(
                "Error 1045: usuario o password invalidos para MySQL.\n"
                "Revisa que el usuario exista, tenga permisos sobre ecbd y que las variables de entorno coincidan.\n"
                "Variables actuales usadas por el script:\n"
                f"  MYSQL_HOST={config['host']}\n"
                f"  MYSQL_PORT={config['port']}\n"
                f"  MYSQL_USER={config['user']}\n"
                f"  MYSQL_DATABASE={config['database']}\n"
                "Vuelve a definir MYSQL_PASSWORD y ejecuta otra vez."
            )
            sys.exit(1)
        raise

# Conectar a la base de datos MySQL
conexion = crear_conexion_mysql()

cursor = conexion.cursor()

# Obtener los datos de la tabla
cursor.execute("SELECT variable, valor FROM datos_radar")
resultados = cursor.fetchall()

# Convertir los datos a una DataFrame de pandas
df = pd.DataFrame(resultados, columns=['variable', 'valor'])

# Cerrar la conexion a la base de datos
cursor.close()
conexion.close()

# Generar el grafico de radar
fig = px.line_polar(df, r = 'valor', theta = 'variable', line_close = True)

# Mostrar el grafico
fig.show()
