# Luis fabrica un anuncio luminoso con focos de color rojo, amarillo
# y verde. De tal manera que los focos rojos se encienden cada 10 segundos,
# los amarillos cada 6 segundos y los verdes cada 15 segundos, si al probar
# los focos a la vez, ¿después dd cuántos segundos volverán a encender junto?.

import math

def mcm(a, b, c):
    # Calculamos el mcm de dos números usando la relación mcm(a, b) = (a * b) // mcd(a, b)
    mcm_ab = (a * b) // math.gcd(a, b)
    mcm_abc = (mcm_ab * c) // math.gcd(mcm_ab, c)
    return mcm_abc

#Intervalos de encendido de los focos (en segundos)
rojo = 10
amarillo = 6
verde = 15

# Calculamos el mcm de los tres intervalos
tiempo_simultaneo = mcm(rojo, amarillo, verde)

# Imprimir resultado
print(f"Los focos volverán a encender juntos depués de {tiempo_simultaneo} segundos.")