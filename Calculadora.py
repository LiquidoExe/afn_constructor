from AFN import AFN
from AFN import AFD
from AlgoritmoLex import Lexico


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
