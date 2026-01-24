# ¿Cuántos hombres se necesitan para realizar en 19 días un trabajo que 209 hombres pueden hacer en 10 días?

# Datos iniciales
hombres_iniciales = 209
dias_iniciales = 10
dias_nuevos = 19

# Calcular el trabajo total en hombres-dia
trabajo_total = hombres_iniciales * dias_iniciales

# Calcular el numero de hombres para los nuevos dias
hombres_necesarios = trabajo_total / dias_nuevos

# Resultado
print(f"Se necesitan {int(hombres_necesarios)} hombres para realizar el trabajo.")