import math

def cosseno(x):  
    n=0
    somatorio=0

    while n<=2:
        somatorio=somatorio+math.pow(-1,n)*math.pow(x,2*n)/math.factorial(2*n)
        n=n+1    
    
    return somatorio

angle=0.5
teorico=math.cos(angle)

y=cosseno(angle)
