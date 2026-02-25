import mysql.connector
import matplotlib.pyplot as plt

# Conectar a la base de datos MySQL
conexion = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="edgar_app", # Cambia por tu usuario de MySQL
    password="ClaveSegura123!", # Cambia por tu usuario de MySQL
    database="escuela"
)

cursor=conexion.cursor()

# Obtener datos para el plot 1 (Ventas anuales)
cursor.execute("SELECT year, dolares FROM ventas_anuales")
resultados = cursor.fetchall()
years = [fila[0] for fila in resultados]
dolares = [fila[1] for fila in resultados]

# Obtener datos para el plot 2 (Productos mas vendidos)
cursor.execute("SELECT producto, cantidad FROM productos_vendidos")
resultados = cursor.fetchall()
productos = [fila[0] for fila in resultados]
cantidad = [fila[1] for fila in resultados]

# Obtener datos para el plot 3 (Notas de estudio)
cursor.execute("SELECT tiempo, nota FROM notas_estudio WHERE materia = 'Algebra'")
resultados = cursor.fetchall()
tiempo_algebra = [fila[0] for fila in resultados]
notas_algebra = [fila[1] for fila in resultados]

cursor.execute("SELECT tiempo, nota FROM notas_estudio WHERE materia = 'Quimica'")
resultados = cursor.fetchall()
tiempo_quimica = [fila[0] for fila in resultados]
notas_quimica = [fila[1] for fila in resultados]

# Obtener datos para el plot 4 (Ventas de empresas)
cursor.execute("SELECT year, ventas_a, ventas_b FROM ventas_empresas")
resultados = cursor.fetchall()
years_empresas = [fila[0] for fila in resultados]
sales_a = [fila[1] for fila in resultados]
sales_b = [fila[2] for fila in resultados]

# Cerrar la conexión a la base de datos
conexion.close()
cursor.close()

# ----- Generar las graficas -----
plt.figure(figsize=(12, 8))

# Plot 1: Ventas anuales
plt.subplot(2, 2, 1)
plt.plot(years, dolares, linewidth = 3)
plt.xticks(years)
plt.ylabel("Dolares")
plt.title("Ventas Anuales", fontsize=12)

# ----- Plot 2: Productos mas vendidos -----
plt.subplot(2, 2, 2)
plt.pie(cantidad, labels=productos, autopct='%1.0f%%')
plt.title("Productos mas vendidos", fontsize=12)

# ----- Plot 3: Diagrama de dispersion (Notas de estudio) -----
plt.subplot(2, 2, 3)
plt.scatter(tiempo_algebra, notas_algebra, color='black', label="Algebra")
plt.scatter(tiempo_quimica, notas_quimica, color='red', label="Quimica")
plt.title("Diagrama de Dispersion", fontsize=12)
plt.xlabel("Horas de estudio")
plt.ylabel("Notas de estudio")
plt.legend(loc="upper left")

# --- Plot 4: Diagrama de areas (Ventas de empresas) -----
plt.subplot(2, 2, 4)
plt.fill_between(years_empresas, sales_a, label="Empresa A", color="green")
plt.fill_between(years_empresas, sales_b, label="Empresa B", color="blue")
plt.title("Diagrama de Areas", fontsize=12)
plt.legend(loc="upper left")

# Titulo general
plt.suptitle("Multiples Diagramas", fontsize=18)

# Mostrar los graficos
plt.tight_layout()
plt.savefig("segundo-parcial/ejercicio-07.png", dpi=150)
print("Gráfico guardado en segundo-parcial/ejercicio-07.png")
plt.close()


