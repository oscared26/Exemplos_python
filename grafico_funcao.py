import numpy as np  
import matplotlib.pyplot as plt  
def f(x): return x**3 + 1 

x = np.linspace(-2,2)
plt.plot(x, f(x))  
plt.grid()  
plt.show()
