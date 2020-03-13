from AFN import AFN
from AFN import AFD
from AlgoritmoLex import Lexico

class Calculadora:
	def __init__(self,AFD,cadena):
		self.Lexico=(cadena,AFD)
		self.MAS=10
		self.MENOS=20
		self.MULT=30
		self.DIV=40
		self.POT=50
		self.PAR_I=60
		self.PAR_D=70
		self.SIN=80
		self.COS=90
		self.TAN=100
		self.NUM=110
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
		if token==self.MAS or token==self.MENOS:
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
		if token==self.MULT or token==self.DIV:
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
		if token==self.POT:
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
		if token==self.PAR_I:
			if E():
				tupla=self.Lexico.getToken()
				token=tupla[1]
				if token==self.PAR_D:
					return True
				return False
		if token==self.SIN:
			tupla=self.Lexico.getToken()
			token=tupla[1]
			if token==self.PAR_I:
				if E():
					tupla=self.Lexico.getToken()
					token=tupla[1]
					if token==self.PAR_D:
						return True
					return False
		if token==self.COS:
			tupla=self.Lexico.getToken()
			token=tupla[1]
			if token==self.PAR_I:
				if E():
					tupla=self.Lexico.getToken()
					token=tupla[1]
					if token==self.PAR_D:
						return True
					return False
		if token==self.TAN:
			tupla=self.Lexico.getToken()
			token=tupla[1]
			if token==self.PAR_I:
				if E():
					tupla=self.Lexico.getToken()
					token=tupla[1]
					if token==self.PAR_D:
						return True
					return False
		if token==self.NUM:
			return True
	#----------------------------------------------------

digitos=AFN(simbolo='0')
uno=AFN(simbolo='1')
dos=AFN(simbolo='2')
tres=AFN(simbolo='3')
cuatro=AFN(simbolo='4')
cinco=AFN(simbolo='5')
seis=AFN(simbolo='6')
siete=AFN(simbolo='7')
ocho=AFN(simbolo='8')
nueve=AFN(simbolo='9')

digitos.union(uno)
digitos.union(dos)
digitos.union(tres)
digitos.union(cuatro)
digitos.union(cinco)
digitos.union(seis)
digitos.union(siete)
digitos.union(ocho)
digitos.union(nueve)

digitos.cerradura_positiva()

mas=AFN(simbolo='+')
menos=AFN(simbolo='-')
mult=AFN(simbolo='*')
div=AFN(simbolo='/')
pot=AFN(simbolo='^')
i=AFN(simbolo='(')
d=AFN(simbolo=')')



sin=AFN(simbolo='s')
sin.concatenacion(AFN(simbolo='i'))
sin.concatenacion(AFN(simbolo='n'))

cos=AFN(simbolo='c')
cos.concatenacion(AFN(simbolo='o'))
cos.concatenacion(AFN(simbolo='s'))

tan=AFN(simbolo='t')
tan.concatenacion(AFN(simbolo='a'))
tan.concatenacion(AFN(simbolo='n'))

mas.union_especial([menos,mult,div,pot,i,d,sin,cos,tan,digitos])
AFDD=mas.ir_a()
Lexemas=Lexico("+-*/^()sincostan24",AFDD)

tupla = Lexemas.getToken()
while tupla[0]!='$' and tupla[0]!='ERROR':
	print(tupla)
	tupla = Lexemas.getToken()
print(tupla)







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
