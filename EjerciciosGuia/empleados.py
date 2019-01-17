

def leerArchivo(nombreArchivo):
	archivo = open(nombreArchivo, "r")

	contenido = archivo.readlines()
	print(contenido)
	archivo.close()

	return contenido

# d => Funcion que dado las lineas 
# 		de un archivo como lista de strings
#		genera una matriz (lista de listas)
#		con los datos de las personas.
# e => lineas del archivo
# s => matriz con los datos
def darFormato(lineasArchivo):
	matriz = []

	for linea in lineasArchivo:
		linea = linea.strip('\r\n')
		persona = linea.split(',')
		matriz.append(persona)

	return matriz

def obtenerJovenes(listadoPersonas):
	personasJovenes = []
	for persona in listadoPersonas:
		if int(persona[2]) < 20:
			personasJovenes.append(persona)
	return personasJovenes

def obtenerJubiladas(listadoPersonas):
	personasJubiladas = []
	for persona in listadoPersonas:
		if persona[1] == 'F' and int(persona[2]) >= 60:
			personasJubiladas.append(persona[0])

		if persona[2] == 'M' and int(persona[2]) >= 65:
			personasJubiladas.append(persona[0])

	return personasJubiladas


def escribirArchivoJubilados():
	pass

def escribirArchivoJovenes():
	pass

# BLOQUE PRINCIPAL

lineasArchivo = leerArchivo("empleados.txt")

personas = darFormato(lineasArchivo)

jovenes = obtenerJovenes(personas)

viejos = obtenerJubiladas(personas)

if escribirArchivoJubilados(viejos) == True:
	print "Archivo generado correctamente"
if escribirArchivoJovenes(jovenes) == True:
	print "Archivo generado correctamente"
