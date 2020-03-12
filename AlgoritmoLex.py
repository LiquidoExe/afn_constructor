def AlgoritmoLex(cadena,AFD):
	estados = AFD.estados
	tokens = AFD.finales
	transiciones = AFD.transiciones
	Salida=[]
	TamañoCadena = len(cadena)
	estado_Actual = 0
	antes_vista = 0
	posicionCadena = 0
	posicionUltimoAceptado = 0

	if TamañoCadena == 0:
			return str(" $ "+" -> "+str(token))

	cadenaAux = ""

	while len(cadena) != 0:
		print("------------------------------------------------")
		print(estado_Actual)
		print(antes_vista)
		print(cadenaAux)
		caracter = cadena[0:1]
		cadena=cadena[1:]
		print(caracter)
		print(cadena)
		print("------------------------------------------------")

		if BuscarTransicion(caracter,transiciones,estado_Actual) > -1:
			estado_Actual = BuscarTransicion(caracter,transiciones,estado_Actual)
			cadenaAux+= caracter
			token = ChecarToken(estado_Actual,estados,tokens)
			if token > 0:
				antes_vista = 1
		else:
			if (antes_vista == 0):
				return str(" ERROR "+" -> "+str(-1))
			else:
				return str(cadenaAux+" -> "+str(token))

	if (antes_vista != 0):
		return str(cadenaAux+" -> "+str(token))


def ChecarToken(estado,estados,tokens):
	print("TOKENS")
	print(estados)
	print(tokens)
	print(estado)
	indice = estados.index(estado)

	return tokens[indice]

def BuscarTransicion(caracter,transiciones,estado_Actual):
	transicionesDelEstado = transiciones.get(estado_Actual)

	if transicionesDelEstado != None:
		for i in transicionesDelEstado:
			if caracter == i[0]:
				return i[1]

	return -1
