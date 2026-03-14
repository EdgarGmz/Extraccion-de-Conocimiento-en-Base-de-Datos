import matplotlib.pyplot as plt
import pandas as pd
import os

def mostrar_grafico():
	if 'agg' in plt.get_backend().lower():
		plt.close()
	else:
		plt.show()

# Cargar datos desde el archivo CSV
# Se espera un archivo 'datagraficas.csv' con las siguientes
# columnas: years_plot1, dolares, productos, cantidad, tiempo_algebra,
# notas_algebra, notas_algebra, tiempo_quimica, notas_quimica,
# years_plot4, sales_a, sales_b
# Cada columna puede tener diferente longitud; los valores faltantes
# se deben ignorar.

file_path = os.path.join(os.path.dirname(__file__), 'datagraficas.csv')
df = pd.read_csv(file_path)



# ----- plot 1: Ventas anuales -----
# Tomar columnas years_plot1 y dolares, eliminar filas con Nan
plot1_data = df [['years_plot1', 'dolares']].dropna()
years1 = plot1_data['years_plot1'].astype(int).tolist()
dolares = plot1_data['dolares'].astype(float).tolist()

# ----- plot 2: Productos más vendidos -----
# Tomar columnas productos y cantidad, eliminar filas con NaN
plot2_data = df [['productos','cantidad']].dropna()
productos = plot2_data['productos'].tolist()
cantidad = plot2_data['cantidad'].astype(int).tolist()

# ----- plot 3: Diagrama de dispersión -----
# Datos de Algebra
algebra_data = df [['tiempo_algebra', 'notas_algebra']].dropna()
tiempo_algebra = algebra_data['tiempo_algebra'].astype(int).tolist()
notas_algebra = algebra_data['notas_algebra'].astype(float).tolist()

# Datos Química
quimica_data = df [['tiempo_quimica', 'notas_quimica']].dropna()
timepo_quimica = quimica_data['tiempo_quimica'].astype(int).tolist()
notas_quimica = quimica_data['notas_quimica'].astype(int).tolist()

# ----- plot 4: Diagramas de áreas (comparativa empresas) -----
# Tomar columnas years_plot4, sales_a, sales_b, eliminar filas con NaN
plot4_data = df [['years_plot4', 'sales_a', 'sales_b']].dropna()
years4 = plot4_data['years_plot4'].astype(int).tolist()
sales_a = plot4_data['sales_a'].astype(float).tolist()
sales_b = plot4_data['sales_b'].astype(float).tolist()

# ----- Creación de los gráficos (sin cambios en los estilos) -----
plt.figure()

# Plot 1
plt.subplot(2, 2, 1)
plt.plot(years1, dolares, linewidth=3)
plt.xticks(years1)
plt.ylabel('Dolares')
plt.title('Ventas Anuales', fontsize=12)

# Plot 2
plt.subplot(2, 2, 2)
plt.pie(cantidad, labels=productos, autopct='%1.0f%%')
plt.title('Productos mas vendidos', fontsize=12)

# Plot 3
plt.subplot(2, 2, 3)
plt.scatter(tiempo_algebra, notas_algebra, color='black', label='Algebra')
plt.scatter(timepo_quimica, notas_quimica, color='red', label='Quimica')
plt.title('Diagrama de Dispersion', fontsize=12)
plt.xlabel('Horas de estudio')
plt.ylabel('Notas de estudio')

# Plot 4
plt.subplot(2, 2, 4)
plt.fill_between(years4, sales_a, label='Empresa A', color='green')
plt.fill_between(years4, sales_b, label='Empresa B', color='blue')
plt.title('Diagrama de areas', fontsize=12)
plt.legend(loc='upper left')

plt.suptitle('Multiples Diagramas', fontsize=18)

# Guardar el gráfico antes de mostrarlo
output_path = os.path.join(os.path.dirname(__file__), 'ejercicio_06_multiples.png')
plt.savefig(output_path)
print(f"Gráfico guardado en: {output_path}")

mostrar_grafico()