# GRAFICAR EXCEL
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
width=0.25
workbook="Puntajes.xlsx"
df=pd. read_excel (workbook)
print(df.head())
datos=df[["Nombre", "Algebra", "Quimica"]]
#datos. plot.bar (x="name", y="Algebra", color="green", width=width, rot=0)
datos. plot(x="Nombre", kind="bar", rot=0)
plt. title("Grafico excel")
plt. xlabel ("Nombres")
plt. ylabel ("Puntajes")
plt. grid()
if matplotlib.get_backend().lower().endswith("agg"):
	salida="grafico_excel.png"
	plt.savefig(salida, dpi=150, bbox_inches="tight")
	print(f"Backend no interactivo detectado ({matplotlib.get_backend()}). Grafico guardado en {salida}")
else:
	plt. show()
