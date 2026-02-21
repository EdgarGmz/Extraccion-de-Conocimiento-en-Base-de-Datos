# El objetivo de este codigo es visualizar la relacion entre horas
# de estudio y las notas obtenidas en dos diferentes asignaturas
# (Algebra y Quimimica) mediante un diagrama de dispersion (scatter plot).

# Este tipo de grafico ayuda a identificar patrones, tendencias o 
# correlaciones entre variables analizadas.

# Un profesor o investigador educativo quiere analizar como influye el
# tiempo de estudio en el rendimiento academico de los estudiantes en 
# dos materias: Algebra y Quimica. 

import matplotlib.pyplot as plt

# DATA
tiempo_algebra = [1, 3, 5, 7]
notas_algebra =[9, 12, 14, 16]

tiempo_quimica = [2, 4, 6, 9]
notas_quimica = [12, 15, 13, 11]

# Caracteristicas 
plt.scatter(tiempo_algebra, notas_algebra, color='black', label='Algebra')
plt.scatter(tiempo_quimica, notas_quimica, color='red', label='Quimica')

# Titulo
plt.title('Diagrama de dispersion')
plt.xlabel('Horas de estudio')
plt.ylabel('Notas de estudio')

# Mostrar
plt.legend()
plt.savefig('diagrama_dispersion2.png') 
plt.grid() 
plt.show()
