import pandas as pd
print("Lectura CSV")

df = pd.read_csv('data/datos.csv', delimiter=";")
#print(df)
#Las primeras 5 filas
print(df.head())
#Podemos agrupar por la ocupación de cada persona
df_grupo = df.groupby('ocupacion').size()
print(df_grupo)