import numpy as np
import matplotlib.pyplot as plt

# 원 안에 10000개 점 찍기
n = 10000
X = np.zeros(n) # 1차원 n개 배열에 모두 0
Y = np.zeros(n) 
j = 0  # 카운트

# x와 y 원 안의 점 찍기
while j < n:
    x = 4 * np.random.rand() - 2  # (-2,2)
    y = 4 * np.random.rand() - 2  # (-2,2)

    if (x**2 + y**2) <= 4:
        X[j], Y[j] = x, y
        j = j + 1
#    r = np.random.rand()
#    t = np.random.rand()
#    X[j] = 2*r * np.cos(np.pi*2*t)
#    Y[j] = 2*r * np.sin(np.pi*2*t)
#    j = j + 1

# 0.01간격으로 x점 잡기
Xk = np.arange(-2, 2, 0.01)
# x^2+y^2=4 원 그리기
Yk1 = (4-Xk**2)**(1/2)
Yk2 = -Yk1
# Xk = [-1,0,1]
# Yk1 = [0,1,0]
# Yk2 = [0,-1,0]

plt.plot(Xk, Yk1, 'b-')
plt.plot(Xk, Yk2, 'r-')
plt.plot(X, Y, 'g.')
plt.show()
