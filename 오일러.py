import numpy as np
import matplotlib.pyplot as plt

#오일러 방법

def f(t,x) : return 1 + x**2 + t**3

n, a, b, x = 100, 1, 2, -4
h = (b-a) / n
t = a

for k in range (1, n+1) :
    x += h * f(t,x)
    t += h
print(x)


#오일러 방법2
def Euler(f,x,a,b,n) :
    T = []
    X = []
    T.append(a)
    X.append(x)
    h = (b-a)/n
    t = a
    
    for k in range (1,n+1) :
        x += h * f(t,x)
        t += h
        T.append(t)
        X.append(x)
    return np.array(T), np.array(X)

def f(t,x) : return 1 + x**2 + t**3
T,X = Euler(f,-4,1,2,30000)
print('%4s %9s %9s' %('n','t','x'))

for i in range(0,30000+1) :
    print('%4d %9.4f %9.8f' %(i,T[i],X[i]))

plt.plot(T,X,'*')
plt.plot(T,np.exp(T),'r-')
plt.show()