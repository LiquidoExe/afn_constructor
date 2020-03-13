#import pdb; pdb.set_trace()
from Estado import Estado
class AFD:
	def __init__(self,estados,transiciones,finales,alfabeto):
		self.estados=estados
		self.transiciones=transiciones
		self.finales=finales
		self.tokens = []
		self.alfabeto = alfabeto

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
	#La cerradura de kleene se forma de una positiva mas una transicion epsilon.
	def cerradura_kleene(self):
		self.cerradura_positiva()
		self.anadir_transicion(0,'ε',len(list(self.estados))-1)
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
		conjuntos_transiciones=[]
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
		lista_finales=[]

		#Asignar los tokens a los nuevos estados del AFN:
		for lista in conjunto_conjuntos:
			lista_finales.append(0)
			token=10
			for final in self.estados_aceptacion:
				if final in lista:
					lista_finales.pop()
					lista_finales.append(token)
				token+=10
		#print(lista_finales)
		return(self.crear_AFD(cerraduras_revisadas,conjuntos_transiciones,lista_finales,self.alfabeto))
	#Crear un nuevo AFD
	def crear_AFD(self,cerraduras,transiciones,finales,alfabeto):
		print("CREANDO AFD")
	########################################################
		#Cambiando los indices de los conjuntos:
		lista_temp=[]
		indice_temp=0
		a=0
		b=0
		for x in range(len(finales)):
			for posicion in range(len(finales)-1):
				if cerraduras[posicion]>cerraduras[posicion+1]:
					a=cerraduras[posicion+1]
					cerraduras[posicion+1]=cerraduras[posicion]
					cerraduras[posicion]=a

					b=finales[posicion+1]
					finales[posicion+1]=finales[posicion]
					finales[posicion]=b
		for lista in cerraduras:
			lista_temp.append(indice_temp)
			for transicion in transiciones:
				if lista in transicion:
					if lista == transicion[0]:
						transicion.pop(0)
						transicion.insert(0,indice_temp)
					if lista == transicion[2]:
						transicion.pop(2)
						transicion.insert(2,indice_temp)
			indice_temp-=1
		for lista in transiciones:
			lista[0]*=-1
			lista[2]*=-1
		dic_AFD={}
		for lista in transiciones:
			if not isinstance(lista[2],list):
				if dic_AFD.get(lista[0]) == None:
					dic_AFD.setdefault(lista[0],[[lista[1],lista[2]]])
				else:
					conjunto_ids = dic_AFD.get(lista[0])
					conjunto_ids.append([lista[1],lista[2]])
		cerraduras=[]
		for elemento in lista_temp:
			cerraduras.append(elemento*-1)
		nuevo_AFD=AFD(cerraduras,dic_AFD,finales,self.alfabeto)


		return nuevo_AFD
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
	#Recorrer los numeros de los estados finales.
	def recorrer_finales(self,posiciones):
		for posicion in range(len(self.estados_aceptacion)):
			#print("Cambiando el estado final de "+str(elemento)+" a "+str(elemento+posiciones))
			self.estados_aceptacion[posicion]+=posiciones
	#Unir varios AFN a un solo inicio:
	def union_especial(self,lista_AFN):
		for AFNx in lista_AFN:
			for simbolo in AFNx.alfabeto:
				if simbolo not in self.alfabeto:
					self.alfabeto.append(simbolo)
		posicion=0
		self.agregar_estado(-1)
		self.anadir_transicion(-1,'ε',0)
		self.estados=self.recorrer_estados(self.estados,1)
		self.recorrer_finales(1)
		for key in list(self.estados.keys()):
			self.estados.get(key).actualizar_transiciones(1)
		posicion+=len(list(self.estados))
		print("Recorriendo "+str(posicion))
		for AFN in lista_AFN:
			self.anadir_transicion(0,'ε',posicion)
			AFN.estados=AFN.recorrer_estados(AFN.estados,posicion)
			AFN.recorrer_finales(posicion)
			for key in list(AFN.estados.keys()):
				AFN.estados.get(key).actualizar_transiciones(posicion)
			posicion+=len(list(AFN.estados))

		for AFN in lista_AFN:
			for estado in AFN.estados_aceptacion:
				self.estados_aceptacion.append(estado)
			self.estados.update(AFN.estados)
