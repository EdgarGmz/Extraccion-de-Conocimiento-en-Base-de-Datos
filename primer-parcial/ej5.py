# EL programa generará una ventana con un gráfioco de líneas que permite comparar visualmente
# el desempeño de ambas empresas. La Empresa A (línea azul) parte de ventas más altas en 2019,
# pero la Empresa B (línea Roja) muestra un crecimiento más acelerado, alcanzando las mismas 
# ventas que A en 2022.

# Libreria
import matplotlib.pyplot as plt 

# Datos
years = [2019, 2020, 2021, 2022]
sales_a = [14, 18, 23, 32]
sales_b = [11, 12, 26, 32]

# Configurar las caracteristicas del grafico 
plt.plot(years, sales_a, color='green', linewidth=3, label='Empresa A')
plt.plot(years, sales_b, color='red', linewidth=3, label='Empresa B')

# Definir titulo y nombre de ejes
plt.title("Diagrama de Ventas")
plt.ylabel("Ventas")
plt.xlabel("Años")
plt.xticks(years)

# Mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()