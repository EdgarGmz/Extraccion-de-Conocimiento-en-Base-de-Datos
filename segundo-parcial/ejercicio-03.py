import pandas as pd
import matplotlib.pyplot as plt
import os

# Leer archivo CSV
file_path = os.path.join(os.path.dirname(__file__), 'dispersion.csv')
try:
	df = pd.read_csv(file_path)
	# Limpiar espacios en los nombres de las columnas
	df.columns = df.columns.str.strip()
except FileNotFoundError:
	print(f"Error: El archivo '{file_path}' no fue encontrado.")
	exit()
except pd.errors.EmptyDataError:
	print("Error: El archivo CSV está vacío.")
	exit()

# Validar que las columnas necesarias existan
required_columns = ['materia', 'tiempo', 'nota']
if not all(col in df.columns for col in required_columns):
	print(f"Error: Las columnas requeridas no existen. Columnas disponibles: {df.columns.tolist()}")
	exit()

# Filtrar los datos por materia
algebra_data = df[df['materia'] == 'Algebra']
quimica_data = df[df['materia'] == 'Quimica']

# Extraer las columnas de tiempo y notas
tiempo_algebra = algebra_data['tiempo']
notas_algebra = algebra_data['nota']

tiempo_quimica = quimica_data['tiempo']
notas_quimica = quimica_data['nota']

# Caracteristicas del gráfico
plt.scatter(tiempo_algebra, notas_algebra, color='black', label='Algebra')
plt.scatter(tiempo_quimica, notas_quimica, color='red', label='Quimica')

# Título y etiquetas
plt.title('Diagramas de dispersión')
plt.xlabel('Horas de estudio')
plt.ylabel('Notas de estudio')

# Mostrar leyenda y gráficos
plt.legend(loc="upper left")
plt.grid()
output_path = os.path.join(os.path.dirname(__file__), 'diagrama_dispersion.png')
plt.savefig(output_path)
plt.show()

# Interpretación del Gráfico
# Posible correlación positiva. Si los puntos tienden a subir hacia la 
# derecha, sugiere que a mas horas de estudio, mejores notas.

# Diferencia entre asignaturas: Permite comparar si una materia requiere 
# más tiempo para lograr notas similares.

# Outliers: Puntos alejados de la tendencia (ej. en Química, 9 horas ? nota 11)
# podrían indicar otros factores influyentes.