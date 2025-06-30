import pandas as pd
#creamos un diccionario de series para los datos
datos = {
    "nombres": ["Lucia", "Adrian", "Antonia", "Diana"],
    "edad": [22, 26, 46, 43],
    "ciudad": ["Alicante", "Toledo", "Burgos", "Soria"]
}
#Almacenamos los datos dentro de un DataFrame
df = pd.DataFrame(datos)
print(df)
#Podemos hacer acciones sobre los datos, por ejemplo filtrar
#por la edad
# df[ df['columna'] == valor]
print("Filtrar por edad")
df_filtrado = df[df['edad']>30]
print(df_filtrado)
#Ordenar los datos
df_sorted = df.sort_values('edad')
print(df_sorted)
