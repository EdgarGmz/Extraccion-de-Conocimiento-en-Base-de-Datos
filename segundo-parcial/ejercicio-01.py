# La empresa Rinco Matic S.A de C.V, se dedica a la fabricacion de muebles
# escolares, asi como muebles de cocina, es una empresa reconocida por la 
# calidad que ofrece en sus productos, sin embargo en este ultimo mes de abril
# del presente año ha recibido quejas por parte de sus clientes que adquieren
# muebles como pupitres escolares, puesto que la cubierta de terciado de las 
# las paletas para los mesa-bancos se desprendian con facilidad. Es por ello 
# que la empresa ha reaccionado de la manera mas rapida posible, encomendando 
# al jefe de producción le justifique el porqué de esos mesa-bancos, por lo que 
# empresa pidió respaldo de lo mencionado y tomara cartas en el asunto y desde
# luego brindará una respuesta inmediata.
# Por lo que el jefe de producción primeramente ha de determinar el tamaño de la
# muestra a analizar tomada de un lote de producción identificando ensamble de 
# los mesa-bancos se tenían dificultades a la hora de fijar con las pijas.
#
# Los datos obtenidos fueron los siguientes:
# 17.89, 17.91, 17.03, 17.03, 17.97, 17.97, 18.01, 18.01, 18.05, 18.08, 18.11, 18.12, 18.14
# 18.12, 18.14, 18.14, 18.16, 18.16, 18.17, 18.18, 18.19, 18.21, 18.22, 18.32

# Comprobar que los datos tengan un comportamiento normal, por medio de una 
# prueba de normalidad, antes de hacer cualquier analisis.

# Determinar las medidas de tendencia central y de dispersión.

# Interpretar los resultados.

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Datos proporcionados
datos = np.array([17.89, 17.91, 17.03, 17.03, 17.97, 17.97, 18.01, 18.01, 18.05, 18.08, 18.11, 18.12, 18.14,
         18.12, 18.14, 18.14, 18.16, 18.16, 18.17, 18.18, 18.19, 18.21, 18.22, 18.32])

# Prueba de normalidad (Shapiro-Wilk)
shapiro_test = stats.shapiro(datos)
print("---Prueba de Normalidad (Shapiro-Wilk)---")
print(f"Estadístico W: {shapiro_test.statistic:.4f}")
print(f"Valor p: {shapiro_test.pvalue:.4f}")

if(shapiro_test.pvalue > 0.05):
    print("Conclusión: Los datos siguen una distribución normal (p > 0.05).")
else:
    print("Conclusión: Los datos NO siguen una distribución normal (p = 0.05).")


# Medida de tendencia central
media = np.mean(datos)
mediana = np.median(datos)
moda = stats.mode(datos, keepdims=True).mode[0]

print("\n--- Medidas de Tendencia Central ---")
print(f"Media: {media:.4f}")
print(f"Mediana: {mediana:.4f}")
print(f"Moda: {moda:.4f}")

# Medidas de dispersión
desviacion_std = np.std(datos, ddof=1) #ddof=1 para muestra (no población)
varianza = np.var(datos, ddof=1)
rango = np.max(datos) - np.min(datos)
rango_intercuartil = stats.iqr(datos)

print("\n--- Medidas de Dispersión ---") 
print(f"Desviación Estándar: {desviacion_std:.4f}mm.")
print(f"Varianza: {varianza:.4f}")
print(f"Rango: {rango:.4f}")
print(f"Rango Intercuartil: {rango_intercuartil:.4f}mm2.")

# Visualización 
plt.figure(figsize=(12, 5))

# Histograma + curva de densidad
plt.subplot(1, 2, 1)
sns.histplot(datos, kde=True, color='blue', bins=6)
plt.title("Distribución del grosor de terciado")
plt.xlabel('Grosor (mm)')
plt.ylabel('Frecuencia')

# Gráfico Q-Q
plt.subplot(1, 2, 2)
stats.probplot(datos, plot=plt)
plt.title("Gráfico Q-Q para normalidad")

plt.tight_layout()
plt.savefig('distribution_plots.png')

# Interpretación adicional
print("\n--- Interpretación de Resultados ---")
if(shapiro_test.pvalue > 0.05):
    print("Los datos son normales, por lo que técnicas paramétricas son válidas.")
else:
    print("Los datos NO son normales. Concidere pruebas no parametricas.")