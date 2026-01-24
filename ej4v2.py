# Datos iniciales
hbrs_i = 209
dias_i = 10
dias_n = 19

def calcular_hombres_necesarios(hombres_iniciales, dias_iniciales, dias_nuevos):
    trabajo_total = hombres_iniciales * dias_iniciales
    return int(trabajo_total / dias_nuevos)

print(f"Resultado: {calcular_hombres_necesarios(hbrs_i, dias_i, dias_n)}")