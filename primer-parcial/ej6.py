# Este código utiliza la librería Matplotlib en Python para generar
# un diagrama de barras que muestra los lengiajes de programación más
# demandados en 2022, junto con su porcentaje de popularidad. El gráfico
# se guarda automáticamente como una imagen (diagrama_barras.png) y 
# también se muestra en una ventana.

# Librería
import matplotlib.pyplot as plt

# Datos lenguajes de programación  mayor demanda 2022
porcentajes = [14,12,11,10,8]
lenguajes = ["Python", "C", "Java", "C++", "C#"]

# Configurar las características de la gráfica
plt.bar(lenguajes, porcentajes, label="ENCUESTA 2022", width=0.4, color="green")

# Configurar el título de la gráfica 
plt.title("Diagrama de Barras")
plt.xlabel("Lenguajes de Programación")
plt.ylabel("Porcentajes")

# Mostrar la gráfica
plt.legend()

# Guardar automático
plt.savefig("diagrama_barras.png")

plt.show()