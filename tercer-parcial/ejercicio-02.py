# El código tiene como objetivo como graficar y comparar la funciones trigonométricas 
# básicas (seno, coseno y tangente) en un rango  de -2p a 2p, permitiendo:

# Identificar patrones (periodicidad, amplitud, asíntotas).
# Entender diferencias clave entre las funciones (ej. ceros, máximos/mínimos).
# Visualizar conceptos matemáticos como:
# Puntos notables (p/2, p, etc.).
# Comportamiento de la tangente (discontinuidades).

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# =====================================================
# 1. CONFIGURACIÓN INICIAL Y GENERACIÓN DE DATOS
# =====================================================
# Rango de -2p a 2p con 1000 puntos para suavidad
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Puntos notables en el eje X (multiplos de p/2)
puntos_notables = [i * np.pi / 2 for i in range(-4, 5)]
etiquetas = ["-2p", "-3p/2", "-p", "-p/2", "0", "p/2", "p", "3p/2", "2p"]

# =====================================================
# 2. CREACIÓN DE LA FIGURA CON DOS SUBPLOTS
# =====================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# =====================================================
# 3. GRAFICA 1: FUNCIONES TRIGONOMÉTRICAS BÁSICAS
# =====================================================
ax1.plot(x, np.sin(x), label='Seno (y = sen x)', color='blue')
ax1.plot(x, np.cos(x), label='Coseno (y = cos x)', color='orange')
ax1.plot(x, np.tan(x), label='Tangente (y = tan x)', color='green')

# Configuración de los ejes
ax1.set_xticks(puntos_notables)
ax1.set_xticklabels(etiquetas)
ax1.set_ylim(-5, 5)  # Limita rango en 'y' para evitar picos infinitos de la tangente
ax1.axhline(0, color='black', linewidth=0.8) # eje horizontal
ax1.axvline(0, color='black', linewidth=0.8)  # eje vertical

# Líneas punteadas para las asíntotas de la tangente (donde cos(X) = 0)
for k in range(-3, 4):
    asintota = (2*k + 1) * np.pi / 2
    if -2*np.pi <= asintota <= 2*np.pi:
        ax1.axvline(asintota, color='red', linestyle='--', linewidth=0.8, alpha=0.5)

ax1.set_title("Funciones Trigonométricas Básicas")
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left')
ax1.set_xlabel('x (radianes)')
ax1.set_ylabel('y')

# =========================================================
# 4. GRÁFICA 2: CASO PRÁCTICO - MOVIMIENTO ARMÓNICO SIMPLE
# =========================================================
# Ejemplo: Un resorte con masa oscila verticalmente.
# La posición en función del tiempo se modela como:
#   y(t) = A * cos(? t + f)
# donde:
#   A = amplitud (desplazamiento máximo) = 2 metros.
#   ? = frecuencia angular = 2 rad/s
#   f = fase inicial = p/4 radianes  (45°)
A = 2
omega = 2
fase = np.pi / 4

# Definimos la funcion  para el caso practico
y_mas_resorte = A * np.cos(omega * x + fase)

# Graficamos
ax2.plot(x, y_mas_resorte, label='x(t) = 2 . cos(2t + p/4)', color='purple')

# Configuracion
ax2.set_xticks(puntos_notables)
ax2.set_xticklabels(etiquetas)
ax2.axhline(0, color='black', linewidth=0.8) 
ax2.axvline(0, color='black', linewidth=0.8)
ax2.set_ylim(-3, 3) # Un poco mas que la amplitud para ver los limites
ax2.set_title('Caso Practico: Movimiento Armonico Simple (masa-resorte)')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper left')
ax2.set_xlabel('Tiempo t (segundos)')
ax2.set_ylabel('Posicion x (metros)')

# =========================================================
# 5. AJUSTE FINAL Y VISUALIZACIÓN
# =========================================================
plt.tight_layout()
backend = plt.get_backend().lower()

if "agg" in backend:
    output_path = Path(__file__).with_name("ejercicio-02.png")
    plt.savefig(output_path, dpi=150)
    print(f"Backend no interactivo detectado ({backend}). Gráfica guardada en: {output_path}")
else:
    plt.show()