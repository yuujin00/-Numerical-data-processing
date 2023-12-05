import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 푸리에 급수
def Fouriercoeff(f,N,p):
    A = np.zeros(N+1)
    B = np.zeros(N+1)
    A[0] = 1/p * quad(f,-p,p)[0] # 적분값만 받기위해 [0]
    for i in range(1,N+1):
        g = lambda x: f(x)*np.cos(i*np.pi*x)
        A[i] = 1/p * quad(g,-p,p)[0]
        h = lambda x: f(x)*np.sin(i*np.pi*x)
        B[i] = 1/p * quad(h,-p,p)[0]
    return A,B

# 함수
def f(x):
    if x>-1 and x<=0:
        return x+1
    elif x>0 and x<1:
        return 1

# 주기 
def g(x):
    return f(x-2*np.floor((x+1)/(2)))

print(Fouriercoeff(g,4,1))

def p(x,N):
    A,B= Fouriercoeff(g,N,1)
    n = len(A)
    res = 1/2 * A[0]
    for i in range(1,n):
        res = res + A[i]*np.cos(i*np.pi*x)+B[i]*np.sin(i*np.pi*x)
    return res

print(quad(g,-1,1))

Xk = np.arange(-3,3,0.1)
Yk = [g(xk) for xk in Xk]


Zk1 = [p(xk,1) for xk in Xk]
Zk2 = [p(xk,2) for xk in Xk]
Zk3 = [p(xk,3) for xk in Xk]
Zk10 = [p(xk,10) for xk in Xk]
plt.plot(Xk,Yk,'.')
plt.plot(Xk,Zk1,'-')
plt.plot(Xk,Zk2,'-')
plt.plot(Xk,Zk3,'-')
plt.plot(Xk,Zk10,'-')
plt.show()