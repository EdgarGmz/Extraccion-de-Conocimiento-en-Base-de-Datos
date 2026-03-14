import numpy as np
import matplotlib.pyplot as plt

def mostrar_grafico():
	if 'agg' in plt.get_backend().lower():
		plt.close()
	else:
		plt.show()

# Datos
x = np.linspace(0, 10, 25)
y = np.sin(x) + x/2

x1 = np.linspace(0, 10, 25)
y1 = np.sin(x) + x/2

x2 = np.linspace(0, 10, 25)
y2 = np.cos(x) + x/2

# 1. Gráfico de líneas
plt.figure()
plt.plot(x, y)
plt.title('1. Gráfico de líneas')
mostrar_grafico()

# 2. Color de Línea
plt.figure()
plt.plot(x, y, color='green')
plt.title('2. Color de Línea')
mostrar_grafico()

# 3. Grosor de línea
plt.figure()
plt.plot(x, y, linewidth=4)
plt.title('3. Grosor de línea')
mostrar_grafico()

# 4. Gráfico de líneas con estilo
plt.figure()
plt.plot(x, y, linestyle='--')
plt.title('4. Gráfico con línea discontinua')
mostrar_grafico()

# 5. Agregar simbolos a las lineas
plt.figure()
plt.plot(x, y, marker='o')
plt.title('5. Símbolos en las líneas')
mostrar_grafico()

# 6. Líneas y símbolos con colores
plt.figure()
plt.plot(x, y, color='red', marker='s', markerfacecolor='black')
plt.title('6. Líneas y símbolos con colores')
mostrar_grafico()

# 7. Usar Formato
plt.figure()
plt.plot(x, y, '*g-')
plt.title('7. Formato compacto')
mostrar_grafico()

# 8. Gráfica con varias líneas 
plt.figure()
plt.plot(x1, y1, marker='o', label='Sin(x) + x/2')
plt.plot(x2, y2, marker='o', label='Cos(x) + x/2')
plt.legend()
plt.title('8. Gráfica con varias líneas')
mostrar_grafico()

# 9. Gráfica de varios niveles
plt.figure()
plt.plot(x1, y1, "c^", x2, y2, 'd--')
plt.title('9. Gráfica de varios niveles')
mostrar_grafico()

# 10. Function step
plt.figure()
plt.step(x, y)
plt.title('10. Función step')
mostrar_grafico()