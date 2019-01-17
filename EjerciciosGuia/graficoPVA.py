#DEFINICION DE FUNCIONES
#IMPORTACION DE FUNCIONES
from numpy import *
from math import pi
import matplotlib.pyplot as plt
#BLOQUE DE DEFINICIONES
#Constantes
W= (2*pi)/3
A=2
vector = arange(0,20.1,0.1)
print vector
#BLOQUE PRINCIPAL
#PROCESAMIENTO
#ESCRIBIMOS LA FUNCION RESPECTIVA
wt = W*vector
funcionPosicion = A * sin( wt)
funcionVelocidad = A*W * cos(wt)
funcionAceleracion = A*(W**2)* sin(wt)
#DIBUJAMOS NUESTROS GRAFICOS
grafico1 = plt.plot(vector,funcionPosicion, label = "g(t)")
grafico2 = plt.plot(vector,funcionVelocidad, label = "f(t)")
grafico3 = plt.plot(vector,funcionAceleracion, label = "h(t)")
#CARACTERISTICAS DE NUESTROS GRAFICOS (ESTILO)
plt.setp(grafico1,"color","r")
plt.setp(grafico2,"color","b")
plt.setp(grafico3,"color","g")
#MOSTRAR GRAFICO POR PANTALLA
plt.legend()
plt.show()
