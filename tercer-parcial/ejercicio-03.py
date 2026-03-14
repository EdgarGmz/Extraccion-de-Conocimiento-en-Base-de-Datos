# El código actual gera un mapa de calor que podría ser perfectamente
# utilizando para:

# Representar datos epidemiológicos (como casos/muertes/vacaciones por COVID-19)

# Mostrar la distribucón mensual del impacto del coronavirus.
# Comprar el comportamiento de la pandemia entre distintas regiones peruanas.

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Datos 
data = np.random.random((6, 12))  

# Etiquetas
xlabs = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
         'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 
         'Diciembre']

ylabs = ['Lima', 'Piura', 'Arequipa', 'Cusco', 'Puno', 'Ica']

# Mapa de calor
fig, ax = plt.subplots()
im = ax.imshow(data)

# Agregar las etiquetas
ax.set_xticks(np.arange(len(xlabs)), labels = xlabs)
ax.set_yticks(np.arange(len(ylabs)), labels = ylabs)

# Agregar la leyenda
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Leyenda', rotation = -90, va = "bottom")

# Agregar los valores a la gráfica
for i in range(len(ylabs)):
    for j in range(len(xlabs)):
        text = ax.text(j, i, round(data[i, j], 2), ha = "center", va = "center", color = "white")

plt.setp(ax.get_xticklabels(), rotation = 40, ha = "right", rotation_mode = "anchor")

plt.title("Mapa de Calor - CORONAVIRUS (2022)")
backend = plt.get_backend().lower()

if "agg" in backend:
    output_path = Path(__file__).with_name("ejercicio-03.png")
    plt.savefig(output_path, dpi=150)
    print(f"Backend no interactivo detectado ({backend}). Gráfica guardada en: {output_path}")
else:
    plt.show()