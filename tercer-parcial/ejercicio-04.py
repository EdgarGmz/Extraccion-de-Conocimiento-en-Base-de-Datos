# GENERAR EXCEL
import pandas as pd
from prompt_toolkit import ANSI #create dataframe
Edf_marks=pd. DataFrame({ 'Nombre': ['Luis', "Andrea", 'Miguel', 'Samir'],
'Quimica': [68,74,77,78],
'Algebra' : [84,56,73,69],
'Geometria': [78,88,82,87]})
#Create excel
writer=pd. ExcelWriter ('Puntajes.xlsx')
#Write dataframe to excel
Edf_marks. to_excel (writer)
#save
writer. close()
print("Archivo excel creado correctamente...")
