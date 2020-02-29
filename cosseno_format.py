#Série do cosseno de x em radianos
import math
from fatorial import fatorial
i=0
cosseno=0
temp0=0
temp1=0
x= 0.25  #ângulo em radianos
for i in range(6):
    temp0=math.pow(x,2*i)
    temp1=fatorial(2*i)
    cosseno=cosseno+(temp0/temp1)*math.pow(-1,i)
print("O valor do cosseno do ângulo {0} rad é de {1}".format(x,cosseno))