# In[8]:


import numpy as np
x=np.array([0.5,1.2,3.5,4])
print(x)


# In[13]:


import numpy as np
x=np.linspace(0,1,5)
print(x)


# In[12]:


import numpy as np
x=np.arange(0,1,0.15)
print(x)


# In[17]:


import numpy as np
x=np.linspace(0,1,10)
y=np.sin(x)
print("Vector x=> \n",x)
print("Vector y=> \n",y)


# In[21]:


import numpy as np
def f(x):
    return x**2+x+1

x=np.array([-1,-2,-3,-4,0,1,2,3,4,5])
y=f(x)
print("Vector x=> \n",x)
print("Vector y=> \n",y)


# In[23]:


import numpy as np
a=np.ones((2,3))
print(a)


# In[25]:


import numpy as np
a=np.zeros((2,3))
print(a)


# In[154]:


import numpy as np
#a=np.zeros((2,3,2))
#print(a)
#a=np.ones((2,3))
#print(a)
a=np.random.randint(10, size=(2, 4,3))
print(a)


# In[157]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2+x+1

x=np.array([-1,-2,-3,-4,0,1,2,3,4,5])
y=f(x)

plt.plot(x,y)
plt.show()

#print("Vector x=> \n",x)
#print("Vector y=> \n",y)


# In[160]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=np.linspace(-1,1,10)
y=f(x)

plt.plot(x,y)
plt.show()


# In[165]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=np.linspace(-np.pi,np.pi,40)
y=np.exp(x)

plt.plot(x,y)
plt.show()


# In[171]:


import math
x=1
n=0
pi=0
while x>=0.000001:
  z=pi
  pi=pi+pow(-1,n)/(2*n+1)
  f=pi
  x=abs(z-f)/f
  n=n+1
  print(pi)
else:
  m=4*pi
  print('O valor de π e:',m)


# In[173]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=np.linspace(-np.pi,np.pi,40)
y=f(x)

plt.plot(x,y)
plt.grid()
plt.show()


# In[181]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=np.linspace(-np.pi,np.pi,40)
y=f(x)

plt.plot(x,y,'ro-')
plt.grid()
plt.show()


# In[182]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=np.linspace(-np.pi,np.pi,40)
y=f(x)

plt.plot(x,y,color='blue',marker='o')
plt.grid()
plt.show()


# In[184]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=np.linspace(-np.pi,np.pi,40)
y=f(x)

plt.plot(x,y,color='green',marker='s')
plt.grid()
plt.show()


# In[194]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=np.linspace(-np.pi,np.pi,40)
y=f(x)

plt.plot(x,y,color='cyan',marker='^')
plt.grid()
plt.show()


# In[193]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=np.linspace(-np.pi,np.pi,40)
y=f(x)

plt.plot(x,y,color='magenta',marker='o',markersize=4)
plt.grid()
plt.show()


# In[202]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=np.linspace(-np.pi,np.pi,40)
y1=f(x)
y2=np.sin(x)
y3=np.cos(x)

plt.plot(x,y1,color='magenta',marker='o',markersize=4,label="Parábola")
plt.plot(x,y2,color='red',marker='o',markersize=4,label="Seno")
plt.plot(x,y3,color='green',marker='o',markersize=4,label="Cosseno")
plt.legend(loc="upper right")
plt.grid()
plt.show()


# In[213]:


import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 5.0,10)
x2 = np.linspace(0.0, 2.0,10)

y1 = np.sin(x1)
y2 = np.cos(x2)
y3 = x**2

plt.subplot(3, 3, 1)
plt.plot(x1, y1, 'r')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(3, 3, 9)
plt.plot(x2, y2, 'b')
plt.xlabel('time (s)')
plt.ylabel('Undamped')



# In[219]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def f(x,y):
    return np.sin(np.sqrt(x**2+y**2))

x=np.linspace(-6,6,30)
y=np.linspace(-6,6,30)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_wireframe(X,Y,Z,color='black')
ax.set_title('Figura')
plt.show()


# In[221]:


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-6, 6, 0.25)
Y = np.arange(-6, 6, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-2, 2)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)


# In[217]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def f(x,y):
    return np.sin(np.sqrt(x**2+y**2))

x=np.linspace(-6,6,5)
y=np.linspace(-6,6,5)
X,Y=np.meshgrid(x,y)
print("Vector x=> \n",x)
print("Meshgrid x=> \n",X)


# In[218]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def f(x,y):
    return np.sin(np.sqrt(x**2+y**2))

x=np.linspace(-6,6,5)
y=np.linspace(-6,6,5)
X,Y=np.meshgrid(x,y)
print("Vector y=> \n",y)
print("Meshgrid y=> \n",Y)


# In[224]:


import numpy as np
a=np.array([[100,1.5,2.5,3.5,200],[60,6.5,7.5,8.5,9.5],[10.5,11.12,50,14.5,15.5]])
row,col=a.shape
print(row,col)


# In[230]:


import numpy as np
a=np.array([[100,1.5,2.5,3.5,200],[60,6.5,7.5,8.5,9.5],[10.5,11.12,50,14.5,15.5]])

print("Antes => \n",a)
a[1,3]=1000
print("Depois=> \n",a)


# In[234]:


import numpy as np
a=np.array([[100,1.5,2.5,3.5,200],[60,6.5,7.5,8.5,9.5],[10.5,11.12,50,14.5,15.5]])

b=a[0,0:4]
print(b)


# In[235]:


import numpy as np
a=np.array([[100,1.5,2.5,3.5,200],[60,6.5,7.5,8.5,9.5],[10.5,11.12,50,14.5,15.5]])

b=a[0:2,0:4]
print(b)


# In[236]:


import numpy as np
a=np.array([[100,1.5,2.5,3.5,200],[60,6.5,7.5,8.5,9.5],[10.5,11.12,50,14.5,15.5]])

b=a[0,0:]
print(b)


# In[237]:


import numpy as np
a=np.array([[100,1.5,2.5,3.5,200],[60,6.5,7.5,8.5,9.5],[10.5,11.12,50,14.5,15.5]])

b=a[0:,0]
print(b)


# In[238]:


import numpy as np
a=np.array([[100,1.5,2.5,3.5,200],[60,6.5,7.5,8.5,9.5],[10.5,11.12,50,14.5,15.5]])
mask=a>50
print(mask)


# In[241]:


import numpy as np
a=np.array([[100,1.5,2.5,3.5,200],[60,6.5,7.5,8.5,9.5],[10.5,11.12,50,14.5,15.5]])
mask=a>=100
b=a[mask]
print(b)


# In[243]:


import numpy as np
a=np.array([[100,1.5,2.5,3.5,200],[60,6.5,7.5,8.5,9.5],[10.5,11.12,50,14.5,15.5]])
mask=a>=100
b=a[mask]
n=b.shape
print("Dimensão=> \n",n)

