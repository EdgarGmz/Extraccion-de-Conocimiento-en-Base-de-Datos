import pandas as pd
import matplotlib.pyplot as plt

# https://www.datosabiertos.gob.pe/group/datos-abiertos-de-covid-19
# Leer las tablas
csv = pd.read_csv('fallecidos_covid.csv', sep=';', decimal=',', low_memory=False)
dataframe=pd.DataFrame(csv[["FECHA_FALLECIMIENTO", "SEXO", "DEPARTAMENTO"]])
sexo=dataframe["SEXO"].value_counts()
departamento=dataframe["DEPARTAMENTO"].value_counts().head()
print(departamento)

"------ Grafica #1 ------"
plt.subplot(1, 2, 1)
sexo.plot(kind='pie', autopct='%1.01f%%')
plt.title("Fallecidos por sexo")

"------ Grafica #2 ------"
plt.subplot(1, 2, 2)
departamento.plot(kind='bar', rot=20)
plt.title("Fallecidos por departamento")
plt.xticks(fontsize=9)

plt.suptitle("Grafica COVID-19 Fallecidos")
if "agg" in plt.get_backend().lower():
    plt.savefig("grafico_covid.png", dpi=120, bbox_inches="tight")
    print("Grafica guardada en grafico_covid.png")
else:
    plt.show()