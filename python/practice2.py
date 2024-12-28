import numpy as np
import matplotlib.pyplot as plt

a=0
b=np.pi/2
N=20

dx=(b-a)/N

x=np.linspace(a,b,N-1)

y=np.cos(x)

A=np.trapezoid(y,x,dx)
print(2*A)

def plot(x,y):
    plt.plot(x,y)
    plt.show()
    
plot(x,y)