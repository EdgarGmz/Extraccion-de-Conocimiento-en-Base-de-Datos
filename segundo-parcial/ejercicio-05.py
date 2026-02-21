# El objetivo de este código es visualizar y comparar dos conjuntos
# de puntos tridimensionales (3D) en un gráfico de dispersión 3D, 
# utilizando colores distintos para diferenciar los grupos. Esto
# permite analizar la distribución espacial, agrupamientos y patrones
# entre los datos.

# Escenario posible: 
# Un investigador o analista de datos requiere estudiar la relación 
# entre tres variables numéricas en dos grupos diferentes (por ejemplo, 
# Grupo A y Grupo B).

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Creamos la figura 
fig = plt.figure(figsize=(10, 7))

# Creamos el plano 3D
ax1 = fig.add_subplot(111, projection='3d')

# Definimos los datos de prueba (Grupo A)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z = [1, 2, 6, 3, 2, 7, 7, 3, 7, 2]

# Datos adicionales (Grupo B)
x2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
y2 = [-5, -6, -7, -8, -2, -5, -6, -3, -7, -2]
z2 = [1, 2, 6, 3, 2, 7, 7, 3, 7, 2]

# Agregamos los puntos en el plano 3D
ax1.scatter(x, y, z, c='g', marker='o', label='Grupo A')
ax1.scatter(x2, y2, z2, c='r', marker='o', label='Grupo B')

# Títulos y etiquetas de los ejes
ax1.set_title('Diagrama de Dispersión 3D')
ax1.set_xlabel('Eje X')
ax1.set_ylabel('Eje Y')
ax1.set_zlabel('Eje Z')

# Mostrar leyenda
ax1.legend()

# Guardar el gráfico
output_path = os.path.join(os.path.dirname(__file__), 'grafico_3d.png')
plt.savefig(output_path)
print(f"Gráfico guardado en: {output_path}")

# Mostramos el gráfico
plt.show()