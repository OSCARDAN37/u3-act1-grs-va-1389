import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas d redes sociales con 4 elementos por lista
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# Creamos una lista de listas (conformando la tabla)
lista_redes_sociales = [fb, twt, ig, wsp, tel, lkn]
#print(lista_redes_sociales)
# S cada columna le ponemos su nombre
df_redes_sociales = pd.DataFrame(lista_redes_sociales,
                                 columns=["Nombre", "Cantidad", "Es_FB", "año"])
print(df_redes_sociales)
df_redes_sociales.to_csv("RedesSociales.csv", index=False)
# Crear graficas de lineas
# X = Nombre en el Eje Horzontal 
# Y = Cantidad en el Eje vertical
plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Grafica Redes Sociales 1389")
plt.xlabel("Nombre de redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Crear Grafica de puntos
plt.scatter(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Grafica Redes Sociales 1389")
plt.xlabel("Nombre de redes")
plt.ylabel("Cantidad de usuarios")
plt.show()

plt.bar(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Grafica Redes Sociales 1389")
plt.xlabel("Nombre de redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# irdebar la grafica de barras de manera decendente
# de la gran a la pequeña
df_rs_ordenar = df_redes_sociales.sort_values('Cantidad', ascending = False)
plt.bar(df_rs_ordenar["Nombre"], df_rs_ordenar["Cantidad"])
plt.title("Grafica Redes Sociales 1389")
plt.xlabel("Nombre de redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# colorear la grafica de barras
df_rs_ordenar = df_redes_sociales.sort_values('Cantidad', ascending = False)
plt.bar(df_rs_ordenar["Nombre"], df_rs_ordenar["Cantidad"],
        color=['b','g','c','m','y','r'])
plt.title("Grafica Redes Sociales 1389")
plt.xlabel("Nombre de redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Grafica de pie
# plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],labels=df_redes_sociales["Nombre"])
plt.title("Grafica Redes Sociales 1389")
plt.show()
