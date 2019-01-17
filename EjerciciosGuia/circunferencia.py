#BLOQUE DE DEFINICIONES
#MODULOS IMPORTADOS
#importo los modulos con alias.
import matplotlib.pyplot as plt
import numpy as np

#DEFINICION DE FUNCIONES
#funcion que traduce el color ingresado a la sigla del color para matplotlib
#ENTRADA: colorUsuario(string)
#SALIDA: color (string)
def colorMatplotlib(colorUsuario):
    if colorUsuario == "rojo":
        color = "r"
    elif colorUsuario == "azul":
        color = "b"
    elif colorUsuario == "verde":
        color = "g"
    elif colorUsuario == "magenta":
        color = "m"
    elif colorUsuario == "cian":
        color = "c"
    elif colorUsuario == "negro":
        color = "k"
    elif colorUsuario == "blanco":
        color = "w"
    elif colorUsuario == "amarillo":
        color = "y"
    return color
#BLOQUE PRINCIPAL
#ENTRADA
r = input ("ingrese el radio r: ")
a = input ("ingrese a: ")
b = input ("ingrese b: ")
colorUsuario = raw_input ("ingrese el nombre del color para la circunferencia: ")
color = colorMatplotlib(colorUsuario)
#PROCESAMIENTO
#Operacion de vectores
vectorX = np.arange(a-r,r+a+0.01,0.01)
vectorY1 = np.sqrt(np.abs(r**2 - (vectorX - a)**2)) + b
vectorY2= - np.sqrt(np.abs(r**2 - (vectorX - a)**2)) + b
#SALIDA
#Grafico
y1 = plt.plot(vectorX,vectorY1)
y2 = plt.plot(vectorX,vectorY2)
plt.setp(y1,"color",color)
plt.setp(y2,"color",color)
plt.show()

