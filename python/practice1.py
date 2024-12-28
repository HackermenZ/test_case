import numpy as np
import matplotlib.pyplot as plt

a=1
b=10
N=100
dx=(b-a)/N
x=np.linspace(a,b,N-1)
y=x*np.exp(x)

A=np.trapezoid(y,x,dx)
print(A)

def plot(x,y):
    plt.plot(x,y)
    plt.show()
    
plot(x,y)