import math

def fatorial(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact

def seno(x,j):
  soma=0
  for n in range(0,j+1):
    soma=soma+(math.pow(-1,n)*math.pow(x,2*n+1)/fatorial(2*n+1))
  return soma

def cosseno(x,j):
  soma=0
  for n in range(0,j+1):
    soma=soma+(math.pow(-1,n)*math.pow(x,2*n)/fatorial(2*n))
  return soma
  

print("Sin serie=> {0}, math=> {1}".format(seno(0.4,1),math.sin(0.4)))

erro_absoluto=math.fabs(seno(0.4,1)-math.sin(0.4))/math.sin(0.4)

print("Error=>",erro_absoluto)
