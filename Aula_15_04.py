import numpy as np  
import matplotlib.pyplot as plt

def Id(Is,n,Vt,Vd):
    return Is*(np.exp(Vd/(n*Vt))-1)

Vd=np.linspace(0,1)
n=1.45
Is=76.9e-12
K=1.38064852e-23#Constante de Boltzman
q=1.602176634e-19#Carga do elétron
T=25#temperatura
T=T+273.15
Vt=K*T/q

function=Id(Is,n,Vt,Vd)


plt.plot(Vd,function, "-r", label="funcao exp")
plt.plot([0,2],[0.5,0], "-b", label="linha")
plt.legend(loc="upper left")
plt.ylim(0, 2)
plt.grid() 
plt.show()
