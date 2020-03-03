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
			#print("Ingresando un nuevo estado: "+str(id))
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
		for elemento in AFN2.alfabeto:
			if elemento not in self.alfabeto:
				self.alfabeto.append(elemento)

		self.estado_inicial = -1
		self.agregar_estado(-1)
		self.anadir_transicion(-1,'ε',0)
		numero_nodos_AFN1=len(list(self.estados))
		#Agregando la otra ruta de la union.
		self.anadir_transicion(self.estado_inicial,'ε',self.estado_inicial+numero_nodos_AFN1)
		#print("Generando una transicion del "+str(self.estado_inicial)+" e "+str(self.estado_inicial+numero_nodos_AFN1))

		#Actualizar los numeros de los nodos.
		self.estados=self.recorrer_estados(self.estados,1)
		for key in list(self.estados.keys()):
			#print("AFN1 "+str(key))
			self.estados.get(key).actualizar_transiciones(1)
			#print(self.estados.get(key).transiciones)

		#Actualizar los numeros de los nodos del segundo AFN.
		AFN2.estados=self.recorrer_estados(AFN2.estados,numero_nodos_AFN1)
		for key in list(AFN2.estados.keys()):
			#print("AFN2 "+str(key))
			AFN2.estados.get(key).actualizar_transiciones(numero_nodos_AFN1)
			#print(AFN2.estados.get(key).transiciones)

		numero_nodos_total=len(list(self.estados))+len(list(AFN2.estados))
		self.anadir_transicion(numero_nodos_AFN1-1,'ε',numero_nodos_total)
		self.estados_aceptacion=[numero_nodos_total]
		self.agregar_estado(numero_nodos_total)
		AFN2.anadir_transicion(numero_nodos_total-1,'ε',numero_nodos_total)
		self.estado_inicial=0
		self.estados.update(AFN2.estados)
#		self.imprimir_transiciones()
	#Hacer una concatenacion de AFNs.
	def concatenacion(self,AFN2):
		for elemento in AFN2.alfabeto:
			if elemento not in self.alfabeto:
				self.alfabeto.append(elemento)
		numero_nodos_AFN1=len(list(self.estados))-1
		#Actualizar los numeros de los nodos del segundo AFN.
		AFN2.estados=self.recorrer_estados(AFN2.estados,numero_nodos_AFN1)
		for key in list(AFN2.estados.keys()):
			#print("AFN2 "+str(key))
			AFN2.estados.get(key).actualizar_transiciones(numero_nodos_AFN1)
			#print(AFN2.estados.get(key).transiciones)
		self.estados.update(AFN2.estados)
#		self.imprimir_transiciones()
		numero_nodos_total=len(list(self.estados))-1
		self.estados_aceptacion=[numero_nodos_total]
	#Actualizar los id de los estados al agregar nodos antes.
	def cerradura_positiva(self):
		self.estado_inicial = -1
		self.agregar_estado(-1)
		self.anadir_transicion(-1,'ε',0)
		#Recorrer los estados.
		self.estados=self.recorrer_estados(self.estados,1)
		for key in list(self.estados.keys()):
			self.estados.get(key).actualizar_transiciones(1)
		#Agregar el ultimo nodo y las transiciones para la cerradura positiva.
		numero_nodos_total=len(list(self.estados))
		self.anadir_transicion(numero_nodos_total-1,'ε',numero_nodos_total)
		self.estados_aceptacion=[numero_nodos_total]
		self.agregar_estado(numero_nodos_total)
		self.anadir_transicion(numero_nodos_total-1,'ε',1)
#		self.imprimir_transiciones()
	#La cerradura de kleene se forma de una positiva mas una transicion epsilon.
	def cerradura_kleene(self):
		self.cerradura_positiva()
		self.anadir_transicion(0,'ε',len(list(self.estados))-1)
#		self.imprimir_transiciones()
	#No se como se llama esta operacion.
	def interrogacion(self):
		self.estado_inicial = -1
		self.agregar_estado(-1)
		self.anadir_transicion(-1,'ε',0)
		#Recorrer los estados.
		self.estados=self.recorrer_estados(self.estados,1)
		for key in list(self.estados.keys()):
			self.estados.get(key).actualizar_transiciones(1)
		#Agregar el ultimo nodo y las transiciones para la cerradura positiva.
		numero_nodos_total=len(list(self.estados))
		self.anadir_transicion(numero_nodos_total-1,'ε',numero_nodos_total)
		self.estados_aceptacion=[numero_nodos_total]
		self.agregar_estado(numero_nodos_total)
		self.anadir_transicion(0,'ε',numero_nodos_total)
#		self.imprimir_transiciones()

	#La funcion que reemplaza los numeros de estados viejos por los nuevos.
	def recorrer_estados(self,estados,no_posiciones):
		nuevos_estados={}

		for key in list(estados.keys()):
			nuevos_estados.setdefault(key+no_posiciones,estados.get(key))

		return nuevos_estados
	#Funcion para imprimimir los conjuntos de transiciones.
	def imprimir_transiciones(self):
		for key in range(len(list(self.estados.keys()))):
			print("FINAL "+str(key))
			print(self.estados.get(key).transiciones)
	#Funcion ir_a
	def ir_a(self):
		conjunto_conjuntos=[]
		cerraduras_revisadas=[]
		conjuntos_por_revisar=[]
		conjuntos_por_revisar.append([0])
		conjuntos_transiciones=['ε']

		while len(conjuntos_por_revisar)>0:
			s=[]
			print("Conjuntos por revisar: ",end="")
			print(conjuntos_por_revisar)
			print("Cerraduras revisadas:",end="")
			print(cerraduras_revisadas)

			e=conjuntos_por_revisar.pop()
			print("e:")
			print(e)
			print("Cerradura epsilon")

			for var in e:
				s=list(set(s)|set(self.cerradura_e(var)))

			if s not in conjunto_conjuntos:
				conjunto_conjuntos.append(s)
				cerraduras_revisadas.append(e)
			print("s:")
			print(s)

			for simbolo in self.alfabeto:
				m=self.mover(s,simbolo)
				if m in cerraduras_revisadas or len(m) == 0:
					print("Ya se tiene el conjunto.")
				else:

					conjuntos_por_revisar.append(m)
					print("\tm:")
					print("\t"+str(m))
				if [e,simbolo,m] not in conjuntos_transiciones:
					conjuntos_transiciones.append([e,simbolo,m])

		print("Cerraduras revisadas:",end="")
		print(cerraduras_revisadas)
		print("Conjuntos:",end="")
		print(conjunto_conjuntos)
		print("Transiciones:",end="")
		print(conjuntos_transiciones)
	#Funcion mover
	def mover(self,conjunto_epsilon,simbolo):
		lista_resultado=[]
		for var in conjunto_epsilon:
			if(self.estados.get(var).transiciones.get(simbolo)!=None):
				for elemento in self.estados.get(var).transiciones.get(simbolo):
					lista_resultado.append(elemento)
		return lista_resultado
	#Funcion cerradura epsilon
	def cerradura_e(self,var):
		lista_temp=[]
		lista_temp.append(var)
		nueva_lista=[]
		nueva_lista2=[]
		while len(lista_temp) != 0:
			var=lista_temp.pop()


			if var not in nueva_lista:
				nueva_lista.append(var)

				if(self.estados.get(var).transiciones.get('ε')!=None):
					nueva_lista2=self.estados.get(var).transiciones.get('ε')
					for elemento in nueva_lista2:
						lista_temp.append(elemento)
				else:
					print("Entro en el error")

		return nueva_lista

a=AFN(simbolo='a')
b=AFN(simbolo='b')
c=AFN(simbolo='c')
a.union(b)
a.cerradura_kleene()
c.cerradura_positiva()
a.concatenacion(c)

a.imprimir_transiciones()
a.ir_a()
