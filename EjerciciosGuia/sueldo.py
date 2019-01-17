#BLOQUE DE DEFICIONES
#MODULOS IMPORTADOS
from numpy import array
#BLOQUE PRINCIPAL
#ENTRADA
sueldoBase = input("sueldo base: ")
asignacionesImponibles = input("asignaciones imponibles: ")
porcentajePrevision = input("porcentaje prevision: ")
porcentajeSalud = input("porcentaje salud: ")
bonosNoImponibles = input("bonos no imponibles: ")
#PROCESAMIENTO
#transformo la lista a arreglos de numpy para utilizar sus operaciones.
vectorSueldoBase = array(sueldoBase)
vectorAsignacionImponibles = array(asignacionesImponibles)
vectorPrevision = array(porcentajePrevision)
vectorSalud = array(porcentajeSalud)
vectorBonos = array(bonosNoImponibles)
#calculo el total imponible como la suma de los vectores
totalImponible = vectorSueldoBase + vectorAsignacionImponibles
#para las cotizaciones se hace una regla de 3, para obtener el monto que se desea descontar del total imponible
cotizacionPrevision = (totalImponible*vectorPrevision)/100
cotizacionSalud = (totalImponible*vectorSalud)/100
#finalmente obtengo el sueldo liquido.
sueldoLiquido = totalImponible - cotizacionPrevision - cotizacionSalud + vectorBonos
#SALIDA
#muestro por pantalla el sueldo liquido y cotizaciones de cada trabajador.
i = 0
while i<len(sueldoBase):
    #en este caso hago un i + 1, solo para que el primer print diga trabajador 1.
    print "trabajador ", i+1
    #accedo a los elementos del arreglo tal cual como se hace en las listas (a traves del indice)
    print "sueldo Liquido : ",sueldoLiquido[i]
    print "cotizacion prevision : ", cotizacionPrevision[i]
    print "cotizacion salud: ", cotizacionSalud[i]
    i = i + 1
