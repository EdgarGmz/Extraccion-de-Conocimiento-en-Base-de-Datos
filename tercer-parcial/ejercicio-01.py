# El objetivo del código porpocionado es crear una visualización fráfica de
# figuras geométricas básicas utilizando la biblioteca matplotlib en Python.
# Más especificamente:
# 1. Un putno rojo (usando plt.plot).
# 2. Un rectangulo verde (con plt.Rectangle).
# 3. Un circulo (con plt.Circle).
# 4. Un triángulo (con plt.Polygon).

import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from pathlib import Path

# Ajustar figura  y asignar coordenadas
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

pp0 = plt.plot(1, 2, marker="o", color="red")
pp1 = plt.Rectangle((2, 10), 6, 4, color="green")
pp2 = plt.Circle((12, 7), radius=2, color="green")
pp3 = plt.Polygon([[8, 5], [3, 4], [5, 8]], color="yellow")

# depict illuctrations
ax.add_patch(pp1)
ax.add_patch(pp2)
ax.add_patch(pp3)
plt.ylim(0, 15)
plt.xlim(0, 15)
plt.title("Figuras geométricas básicas")

if "agg" in plt.get_backend().lower():
	output_path = Path(__file__).with_name("ejercicio-01.png")
	plt.savefig(output_path, dpi=150, bbox_inches="tight")
	print(f"Figura guardada en: {output_path}")
else:
	plt.show()