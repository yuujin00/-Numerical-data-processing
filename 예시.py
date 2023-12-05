import numpy as np

n=5000
num=0
'''
for i in range(1,n+1):
    for j in range(1,25):
        d1= int(np.ceil(np.random.rand()*6))
        d2= int(np.ceil(np.random.rand()*6))
        if d1+d2==12:
            num+=1
            break
    if i%1000==0:
        print([i,num/i]) # #번째, 실험확률

print(num,num/n)
'''

            # 이론, 실험
            # 1000번이 10000번보다 좋다고 할 수 없다.
            # 수업시간 예제 만큼 
'''
n = 5000
num = 0

for i in range(1,n+1):
    v = np.pi*np.random.rand()
    u = 1/2*np.random.rand()
    if u <= 1/2*np.sin(v):
        num=num+1
    if i % 1000 == 0:
        print([i,num/i, 2*i/num, 2/np.pi]) # #번째, 실험확률, pi값, 이론확률
'''

n=5000
num=0

for i in range(1,n+1): # 시뮬레이션
    x=1
    for j in range(1,8): # 1+cos1+cos2+...+cos7
        v = np.pi*np.random.rand()
        x += np.cos(v)
        if x > 5:
            num+=1
            break 
    if i % 1000 == 0:
        print([i,num/i*100]) # #번, 퍼센트

# 30보다 작은 구간만 프린트하고 멈춰라
'''
for i in range(1,101):
    if i<30:
        print(i)
    else:
        break
'''