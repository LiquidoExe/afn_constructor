from AFN import AFN
from AFN import AFD
from AlgoritmoLex import Lexico

class Calculadora:
	def __init__(self,AFD,cadena):
		self.Lex=Lexico(cadena,AFD)
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
		print('E:',end='')
		if self.T():
			if self.Ep():
			 return True
		return False
	#----------------------------------------------------
	def Ep(self):
		print('Ep:',end='')
		tupla=self.Lex.getToken()
		token=tupla[1]
		print(tupla[0],token)
		if token==self.MAS or token==self.MENOS:
			if self.T():
				if self.Ep():
					return True
			return False
		self.Lex.rewind(tupla[0])
		return True
	#----------------------------------------------------
	def T(self):
		print('T:',end='')
		if self.P():
			if self.Tp():
			 return True
		return False
	#----------------------------------------------------
	def Tp(self):
		print('Tp:',end='')
		tupla=self.Lex.getToken()
		token=tupla[1]
		print(tupla[0],token)
		if token==self.MULT or token==self.DIV:
			if self.P():
				if self.Tp():
					return True
			return False
		self.Lex.rewind(tupla[0])
		return True
	#----------------------------------------------------
	def P(self):
		print('P:',end='')
		if self.F():
			if self.Pp():
			 return True
		return False
	#----------------------------------------------------
	def Pp(self):
		print('Pp:',end='')
		tupla=self.Lex.getToken()
		token=tupla[1]
		print(tupla[0],token)
		if token==self.POT:
			if self.F():
				if self.Pp():
					return True
			return False
		self.Lex.rewind(tupla[0])
		return True
	#----------------------------------------------------
	def F(self):
		print('F:',end='')
		tupla=self.Lex.getToken()
		token=tupla[1]
		print(tupla[0],token)
		if token==self.PAR_I:
			if self.E():
				tupla=self.Lex.getToken()
				token=tupla[1]
				if token==self.PAR_D:
					return True
				return False
		if token==self.SIN:
			tupla=self.Lex.getToken()
			token=tupla[1]
			if token==self.PAR_I:
				if self.E():
					tupla=self.Lex.getToken()
					token=tupla[1]
					if token==self.PAR_D:
						return True
					return False
		if token==self.COS:
			tupla=self.Lex.getToken()
			token=tupla[1]
			if token==self.PAR_I:
				if self.E():
					tupla=self.Lex.getToken()
					token=tupla[1]
					if token==self.PAR_D:
						return True
					return False
		if token==self.TAN:
			tupla=self.Lex.getToken()
			token=tupla[1]
			if token==self.PAR_I:
				if self.E():
					tupla=self.Lex.getToken()
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

MiCalculadora=Calculadora(AFDD,"24+48")
MiCalculadora.E()
