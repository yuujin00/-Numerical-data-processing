import numpy as np
import matplotlib.pyplot as plt

#고차 테일러 급수법

n = 30
a , b, x = 1, 2, -4
h = (b-a)/n
t = a
T, X = [t], [x]
for k in range(1, n+1) :
     x1 = 1 + x**2 + t**3
     print('x=',x1)
     x2 = 2*x*x1 + 3*t**2
     x3 = 2*x*x2 + 2*x1**2 + 6*t
     x4 = 2*x*x3 + 6*x1*x2 + 6
     x = x + h*x1 + 1/2*h**2*x2 + 1/6*h**3*x3 + 1/24*h**4*x4
     t = t + h
     T.append(t)
     X.append(x)

print('%4s %9s %9s' %('n', 't', 'x'))
for i in range(0,n+1):
    print('%4d %9.4f %9.8f' %(i,T[i],X[i]))

plt.plot(T,X,'*')
#plt.plot(T,np.exp(T),'r-')
plt.show()

