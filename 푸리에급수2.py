import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def Fouriercoeff(f,N,p):
    A = np.zeros(N+1)
    B = np.zeros(N+1)
    A[0] = 1/p * quad(f,-p,p)[0]
    for i in range(1,N+1):
        g = lambda x: f(x)*np.cos(i*x)
        A[i] = 1/np.pi * quad(g,-p,p)[0]
        h = lambda x: f(x)*np.sin(i*x)
        B[i] = 1/np.pi * quad(h,-p,p)[0]
    return A,B

def f(x):
    if x>-np.pi and x<np.pi:
        return x

def g(x):
    return f(x-2*np.pi*np.floor((x+np.pi)/(2*np.pi)))

print(Fouriercoeff(g,4,np.pi))

def p(x):
    A,B = Fouriercoeff(g, 10, np.pi)
    res = 1/2*A[0]
    n = len(A)
    for i in range(1,n):
        res = res + A[i]*np.cos(i*x)+B[i]*np.sin(i*x)
    return res

Xk = np.arange(-5,8,0.1)
Yk = [p(xk) for xk in Xk]
Zk = [g(xk) for xk in Xk]
#print(Yk)

plt.plot(Xk,Yk,'-')
plt.plot(Xk,Zk,'.')
plt.show()