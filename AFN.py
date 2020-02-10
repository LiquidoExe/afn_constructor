from Estado import Estado

class AFN:
	#Constructor de la clase.
	def __init__(self, simbolo = None):
		if simbolo == None:
			self.estado_inicial = 0
			self.estados_aceptacion = []
			self.alfabeto = []
			self.estados = {}
		else:
			self.estado_inicial = 0
			self.estados_aceptacion = [1]
			self.alfabeto = [simbolo]
			self.estados = {}
			self.agregar_estado(0)
			self.agregar_estado(1)
			self.anadir_transicion(0,simbolo,1)
	#Agregar un simbolo al lenguaje.
	def agregar_simbolo(self,simbolo):
		if simbolo in self.alfabeto:
			print("El simbolo |"+simbolo+"| ya se encuentra en el alfabeto.")
		else:
			print("Insertando simbolo en el alfabeto.")
			self.alfabeto.append(simbolo)
			print(self.alfabeto)
	#Agregar un estado al lenguaje.
	def agregar_estado(self,id):
		if self.estados.get(id) == None:
			print("Ingresando un nuevo estado: "+str(id))
			self.estados.setdefault(id,Estado(id))
		else:
			print("El estado ya se encuentra en el conjunto")
	#Agregar una transicion a un estado existente:
	def anadir_transicion(self,id,simbolo,id_final):
		if self.estados.get(id) == None:
			print("El estado no existe")
		else:
			self.estados.get(id).anadir_transicion(simbolo,id_final)
	#Agregar un estado dd aceptacion a la lista:
	def anadir_estado_aceptacion(self,simbolo):
		self.estados_aceptacion.append(simbolo)
	#Hacer una union entre dos AFNs.
	def union(self,AFN2):
		self.estado_inicial = self.estado_inicial-1
		self.agregar_estado(self.estado_inicial)
		self.anadir_transicion(self.estado_inicial,'ε',self.estado_inicial+1)
		self.estados=self.recorrer_estados(self.estados,1)

		for key in list(self.estados.keys()):
			print("AFN1 "+str(key))
			self.estados.get(key).actualizar_transiciones(1)
			print(self.estados.get(key).transiciones)

		numero_nodos_AFN1=len(list(self.estados))
		AFN2.estados=self.recorrer_estados(AFN2.estados,numero_nodos_AFN1)
		for key in list(AFN2.estados.keys()):
			print("AFN2 "+str(key))
			AFN2.estados.get(key).actualizar_transiciones(numero_nodos_AFN1)
			print(AFN2.estados.get(key).transiciones)

		self.estados_aceptacion=[len(list(self.estados))+len(list(AFN2.estados))]
		print(self.estados_aceptacion)

	#Actualizar los id de los estados al agregar nodos antes.
	def recorrer_estados(self,estados,no_posiciones):
		nuevos_estados={}

		for key in list(estados.keys()):
			nuevos_estados.setdefault(key+no_posiciones,estados.get(key))

		return nuevos_estados

nuevo_AFN = AFN()
print(nuevo_AFN.estados_aceptacion,nuevo_AFN.alfabeto,nuevo_AFN.estados)

nuevo_AFN.agregar_simbolo('a')
nuevo_AFN.agregar_simbolo('b')
nuevo_AFN.agregar_simbolo('a')

nuevo_AFN.agregar_estado(0)
nuevo_AFN.agregar_estado(1)
nuevo_AFN.agregar_estado(2)

nuevo_AFN.anadir_transicion(0,'a',1)
nuevo_AFN.anadir_transicion(0,'b',2)
nuevo_AFN.anadir_transicion(0,'b',3)
nuevo_AFN.anadir_transicion(0,'ε',2)
nuevo_AFN.anadir_transicion(1,'ε',3)

v2 = AFN(simbolo='a')

nuevo_AFN.union(v2)
