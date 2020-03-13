from AFN import AFN
from AFN import AFD
from AlgoritmoLex import Lexico

class Calculadora:
	def __init__(self,AFD,cadena):
		self.Lexico=(cadena,AFD)
	#----------------------------------------------------
	def E(self):
		if T():
			if Ep():
			 return True
		return False
	#----------------------------------------------------
	def Ep(self):
		tupla=self.Lexico.getToken()
		token=tupla[1]
		print(token)
		if token==MAS or token==MENOS:
			if T():
				if Ep():
					return True
			return False
		self.Lexico.rewind(token=tupla[0])
		return True
	#----------------------------------------------------
	def T(self):
		if P():
			if Tp():
			 return True
		return False
	#----------------------------------------------------
	def Tp(self):
		tupla=self.Lexico.getToken()
		token=tupla[1]
		print(token)
		if token==MULT or token==DIV:
			if P():
				if Tp():
					return True
			return False
		self.Lexico.rewind(token=tupla[0])
		return True
	#----------------------------------------------------
	def P(self):
		if F():
			if Pp():
			 return True
		return False
	#----------------------------------------------------
	def Pp(self):
		tupla=self.Lexico.getToken()
		token=tupla[1]
		print(token)
		if token==POT:
			if F():
				if Pp():
					return True
			return False
		self.Lexico.rewind(token=tupla[0])
		return True
	#----------------------------------------------------
	def F(self):
		tupla=self.Lexico.getToken()
		token=tupla[1]
		if token==PAR_I:
			if E():
				tupla=self.Lexico.getToken()
				token=tupla[1]
				if token==PAR_D:
					return True
				return False
		if token==SIN:
			tupla=self.Lexico.getToken()
			token=tupla[1]
			if token==PAR_I:
				if E():
					tupla=self.Lexico.getToken()
					token=tupla[1]
					if token==PAR_D:
						return True
					return False
		if token==COS:
			tupla=self.Lexico.getToken()
			token=tupla[1]
			if token==PAR_I:
				if E():
					tupla=self.Lexico.getToken()
					token=tupla[1]
					if token==PAR_D:
						return True
					return False
		if token==TAN:
			tupla=self.Lexico.getToken()
			token=tupla[1]
			if token==PAR_I:
				if E():
					tupla=self.Lexico.getToken()
					token=tupla[1]
					if token==PAR_D:
						return True
					return False
		if token==NUM:
			return True
	#----------------------------------------------------


'''
a=AFN(simbolo='a')
b=AFN(simbolo='b')
c=AFN(simbolo='c')
d=AFN(simbolo='d')
f=AFN(simbolo='f')
g=AFN(simbolo='g')
a.concatenacion(b)
c.concatenacion(d)
f.union(g)


a.union_especial([c,f])


AFDD=a.ir_a()
print(AFDD.transiciones)
print(AFDD.estados)

print(AFDD.finales)



Lexemas=Lexico("abcdgf",AFDD)
print(Lexemas.getToken())
print(Lexemas.getToken())
print(Lexemas.getToken())
print(Lexemas.getToken())
'''
