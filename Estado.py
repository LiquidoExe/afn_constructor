class Estado:

	def __init__(self,id):
		self.id = id
		self.transiciones = {}

	def anadir_transicion(self,simbolo,id_final):
		if self.transiciones.get(simbolo) == None:
			print("Hay un nuevo simbolo en el estado.")
			self.transiciones.setdefault(simbolo,[id_final])
			print(self.transiciones)
		else:
			print("Agregando transicion.")
			conjunto_ids = self.transiciones.get(simbolo)
			conjunto_ids.append(id_final)
			print(self.transiciones)

	def actualizar_transiciones(self,no_posiciones):
		for valores in list(self.transiciones.values()):
