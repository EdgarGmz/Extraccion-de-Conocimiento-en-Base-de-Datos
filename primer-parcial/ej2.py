import math

# Dimensiones de la terraza (cm)
largo = 425
ancho = 275

# Calculamos el MCD para la dimesión del mosaico
mcd = math.gcd(largo, ancho)
dimension_mosaico = mcd

# Calculamos el número de mosaicos
num_mosaicos = (largo * ancho) // (mcd ** 2)

print(f"Dimensiones máximas de cada mozaico: {dimension_mosaico} cm * {dimension_mosaico} cm")
print(f"Número de mosiacos necesarios: {num_mosaicos}")
