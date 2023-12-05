import numpy as np
import matplotlib.pyplot as plt

#고차테일러(연립)

n, a, b, x, y = 100, 0, 1, 1, 0
t = a
h = (b-a)/n
T = [t]
X = [x]
Y = [y]
for k in range(1,n+1):
    x1 = x - y + t*(2-t*(1+t))
    y1 = x + y + t**2*(-4+t)
    x2 = x1 - y1 + 2 - t*(2+3*t)
    y2 = x1 + y1 + t*(-8+3*t)
    x3 = x2 - y2 - 2 - 6*t
    y3 = x2 + y2 - 8 + 6*t
    x4 = x3 - y3 -6
    y4 = x3 + y3 +6
    x = x + h*x1 + 1/2*h**2*x2 + 1/6*h**3*x3 + 1/24*h**4*x4
    y = y + h*y1 + 1/2*h**2*y2 + 1/6*h**3*y3 + 1/24*h**4*y4
    t = t + h
    T.append(t)
    X.append(x)
    Y.append(y)

print('%4s %9s %9s %9s' % ('n', 't', 'x', 'y'))
for i in range(0, n + 1):
    print('%4d %9.4f %9.8f %9.8f' % (i, T[i], X[i], Y[i]))

plt.plot(T,X,'*')
plt.plot(T,Y,'-')
plt.show()


#고차테일러(연립,벡터표현)

n, a, b, x, y = 100, 0, 1, 1, 0
t = a
h = (b-a)/n
T,X,Y = [t], [x], [y]
d = np.array([x,y])

for k in range(1,n+1):
    d1 = np.array([d[0] - d[1] + t*(2-t*(1+t)), d[0] + d[1] + t**2*(-4+t)])
    d2 = np.array([d1[0] - d1[1] + 2 - t*(2+3*t), d1[0] + d1[1] + t*(-8+3*t)])
    d3 = np.array([d2[0] - d2[1] - 2 - 6*t, d2[0] + d2[1] - 8 + 6*t])
    d4 = np.array([d3[0] - d3[1] -6, d3[0] + d3[1] +6])
    d = d + h*d1 + 1/2*h**2*d2 + 1/6*h**3*d3 + 1/24*h**4*d4
    t = t + h
    T.append(t)
    X.append(d[0])
    Y.append(d[1])

print('%4s %9s %9s %9s' % ('n', 't', 'x', 'y'))
for i in range(0, n + 1):
    print('%4d %9.4f %9.8f %9.8f' % (i, T[i], X[i], Y[i]))

plt.plot(T,X,'*')
plt.plot(T,Y,'-')
plt.show()


#룽게쿠타법 4차 (연립)

def RK4(F,t,D,h,n):
    a = t
    T = [a]
    X, Y = [D[0]], [D[1]]  # D = [x,y]
    for j in range(1,n+1):
        K_1 = h*F(t,D)
        K_2 = h*F(t+1/2*h,D+1/2*K_1)
        K_3 = h*F(t+1/2*h,D+1/2*K_2)
        K_4 = h*F(t+h,D+K_3)
        D = D + 1/6*(K_1+2*K_2+2*K_3+K_4)
        t = a + j*h
        T.append(t)
        X.append(D[0])
        Y.append(D[1])
    return np.array(T), np.array(X), np.array(Y)

def F(t,X): return np.array([X[0]-X[1]+2*t-t**2-t**3,X[0]+X[1]-4*t**2+t**3])

n = 100
a,b,D = 0,1,[1,0]
h = (b-a)/n
t = a
T, X, Y = RK4(F,t,D,h,n)

print('%4s %9s %9s %9s' %('n', 't', 'x', 'y'))
for i in range(0,n+1):
    print('%4d %9.4f %9.4f %9.4f' %(i,T[i],X[i],Y[i]))

plt.plot(T,X,'-')
plt.plot(T,Y,'-')
plt.show()


#로트카 볼테라

def RK4(F,t,D,h,n):
    a = t
    T = [a]
    X, Y = [D[0]], [D[1]]  # D = [x,y]
    for j in range(1,n+1):
        K_1 = h*F(t,D)
        K_2 = h*F(t+1/2*h,D+1/2*K_1)
        K_3 = h*F(t+1/2*h,D+1/2*K_2)
        K_4 = h*F(t+h,D+K_3)
        D = D + 1/6*(K_1+2*K_2+2*K_3+K_4)
        t = a + j*h
        T.append(t)
        X.append(D[0])
        Y.append(D[1])
    return np.array(T), np.array(X), np.array(Y)

def F(t,X): return np.array([0.6*X[0]*(1-X[0]/1000)-0.02*X[0]*X[1],-0.4*X[1]+0.001*X[0]*X[1]])
n = 100
a,b = 0,50 # 여우가 10, 32, 60일때 비교
h = (b-a)/n
t = a
T, X10, Y10 = RK4(F,t,[500,28],h,n)
T, X32, Y32 = RK4(F,t,[500,32],h,n)
T, X60, Y60 = RK4(F,t,[500,29],h,n)

'''
print('%4s %9s %9s %9s' %('n', 't', 'x', 'y'))
for i in range(0,n+1):
    print('%4d %9.4f %9.8f %9.8f' %(i,T[i],X[i],10*Y[i]))
'''
# plt.plot(T,X,'r-')
plt.plot(X10,Y10,'b-')
plt.plot(X32,Y32,'r-')
plt.plot(X60,Y60,'g-')
plt.show()