import numpy as np
from scipy import stats 
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.power import TTestIndPower

# Datos proporcionados
datos = np.array([
    1.18, 1.18, 1.18, 1.18, 1.19, 1.19, 1.19, 1.20, 1.20, 1.20, 1.20, 1.20,
    1.21, 1.21, 1.21, 1.22, 1.22, 1.22, 1.22, 1.22, 1.23, 1.23, 1.23, 1.23,
    1.23, 1.24, 1.24, 1.24, 1.24, 1.24, 1.25, 1.25, 1.25, 1.25, 1.26, 1.26,
    1.26, 1.29, 1.29, 1.29, 1.29, 1.30, 1.30, 1.30, 1.31, 1.31, 1.31, 1.31,
    1.33, 1.33, 1.34, 1.34, 1.34])

# 1. Prueba de normalidad (Shapiro-Wilk)
shapiro_test = stats.shapiro(datos)
print("--- Prueba de Normalidad (Shapiro-Wilk) ---")
print(f"Estadístico W: {shapiro_test.statistic:.4f}")
print(f"Valor p: {shapiro_test.pvalue:.4f}")

if(shapiro_test.pvalue > 0.05):
    print("Conclusión: Los datos siguen una distribución normal (p > 0.05).")
else:
    print("Conclusión: Los datos no siguen una distribución normal (p = 0.05).")

# 2. Tamaño de muestra (80% confianza, error estándar bajo por costo alto)
# Usando la formula para media poblacional: n= (Z * s / E)^2
confianza = 0.80
alpha = 1 - confianza
Z = stats.norm.ppf(1 -alpha/2) # Z para 80% confianza ~ 1.28
sigma = np.std(datos, ddof=1) # Desviación estándar muestral
E = 0.01 # Margen de error pequeño (por costo alto)
n_formula = (Z * sigma / E) ** 2
print("\n--- Tamaño de Muestra (Fórmula) ---")
print(f"Nivel de confianza: {confianza*100:.0f}%")
print(f"Z: {Z:.2f}")
print(f"Desviación estándar (s): {sigma:.4f}")
print(f"Margen de error (E): {E:.4f}")
print(f"Tamaño de muestra requerido (n): {n_formula:.0f}")

# 3. Comparación con MIL-STD-105E (Nivel de inspección general II, AQL 1.0%)
# Para lote de 52 unidades (similar a los datos), tabla sugiere n=8
print("\n--- Comparación con MIL-STD-105E ---")
print("Condiciones:")
print(" - Nivel de inspección: General II")
print(" - AQL: 1.0% (calidad aceptable)")
print(" - Tamaño de lote: ~50 (similar a los datos)")
print("Tamaño de muestra según tabla: n * 8")

# 4. Medidas de tendencia central
media = np.mean(datos)
mediana = np.median(datos)
moda = stats.mode(datos, keepdims=True).mode[0]

print("\n--- Medidas de Tendencia Central ---")
print(f"Media: {media:.4f} cm.")
print(f"Mediana: {mediana:.4f} cm.")
print(f"Moda: {moda:.4f} cm.")

# 5. Medidas de dispersión
desviacion_std = np.std(datos, ddof=1)
varianza = np.var(datos, ddof=1)
rango = np.max(datos) - np.min(datos)
rango_intercuartil = stats.iqr(datos)   

print("\n--- Medidas de Dispersión ---")
print(f"Desviación estándar: {desviacion_std:.4f} cm.")
print(f"Varianza: {varianza:.6f} cm^2.")
print(f"Rango: {rango:.4f} cm.")
print(f"Rango intercuartil (IQR): {rango_intercuartil:.4f} cm.")

# 6. Visualización de datos
plt.figure(figsize=(12, 5))

# Histograma + curva de densidad
plt.subplot(1, 2, 1)
sns.histplot(datos, kde=True, bins=10, color='blue')
plt.title("Histograma del diametro de monedas")
plt.xlabel("Diámetro (cm)")
plt.ylabel("Frecuencia")

# Grafico Q-Q
plt.subplot(1, 2, 2)    
stats.probplot(datos, dist="norm", plot=plt)
plt.title("Gráfico Q-Q")

plt.tight_layout()
plt.show()

# 7. Interpretación 
print("\n--- Interpretación de resultados ---")
if(shapiro_test.pvalue > 0.05):
    print("Los datos son normales, se pueden aplicar métodos paramétricos.") 
else:
    print("Los datos NO son normales, considere pruebas no paramétricas o transformaciones.") 

print(f"- La media del diametro es {media:.2f} cm. Si el estandar es 1.25 cm, hay desviaciones.")
print(f"- La desviación estandar ({desviacion_std:.4f} cm) indica variabilidad en el proceso de fabricación.")