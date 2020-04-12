import numpy as np  
import matplotlib.pyplot as plt  
import math

def Id(Is,Vd,n,Vt): 
  return Is*(np.exp(Vd/(n*Vt))-1)
  
Is=76.9e-12
n=1.45
T=25#temperatura
K=1.38064852e-23#Constante de Boltzman
q=1.602176634e-19#Carga do elétron
T=T+273.15
Vt=K*T/q


Vd = np.linspace(0,0.7)
plt.plot(Vd, Id(Is,Vd,n,Vt),'r')  
plt.plot([0,8],[8/2200,0],'b')
# Show the major grid lines with dark grey lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.show()
