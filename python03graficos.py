import matplotlib.pyplot as plt

#La mayoría de gráficos tienen un Eje X y un eje Y para representar sus datos
x = ["Atletico de Madrid", "Elche", "Barcelona", "Real Madrid"]
y = [9, 3, 10, 20]
#Mediante la librería plt indicamos el tipo de gráfico que deseamos dibujar
plt.bar(x, y)
#Personalizar el grafico
plt.title("Grafico 30 junio")
plt.xlabel("Equipos")
plt.ylabel("Presupuesto")
#Almacenamos la imagen fisica
plt.savefig('images/equipos.png')
plt.show()