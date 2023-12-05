import numpy as np

# 아이스크림 콘
n = 10000
num_A = 0  # 박스안의 점의 개수
num_D = 0  # 영역안의 점의 개수
while num_A < n:
    x = 2*np.random.rand()-1
    y = 2*np.random.rand()-1
    z = 2*np.random.rand()
    num_A = num_A + 1
    if np.sqrt(x**2 + y**2) <= z and x**2 + y**2 + (z-1)**2 <= 1:
       num_D = num_D + 1
    if num_A % 1000 == 0:
       print([num_A,num_D,8*num_D/num_A])  # 박스부피 2*2*2=8


# 생일문제
num = 51
# 이론값

for n in range(1,num):
    p = 1
    for k in range(1,n+1):
        p *= (365-k+1)/365
    if n % 5 == 0:
        print([n,round((1-p)*100)/100]) # round = 반올림

# 시뮬레이션
res = 0
for k in range(0,1000):
        B = np.zeros(n)
        for j in range(0,n):
            B[j] = int(365*(np.random.rand()))  # ceil = 올림
        if len(set(B)) < n:  # set 집합    --> set이 중복요소 체크로 n보다 작으면 중복 존재 
            res = res + 1
if n % 5 == 0:
    print([n,round((1-p)*1000)/1000,res/1000])


#주사위
n = 10000
num = 0
for i in range(1,n+1):
    for j in range(1,25):
        d1 = int(np.ceil(6*np.random.rand()))
        d2 = int(np.ceil(6*np.random.rand()))
        if d1 + d2 == 12:
            num += 1
            break
    if i % 1000 == 0:
        print([i,num/i])

# 뷔퐁의 바늘문제
n = 15000
num = 0
for i in range(1,n+1):
    u = 1/2 * np.random.rand() #y
    v = np.pi * np.random.rand() #x
    if u <= 1/2 * np.sin(v):
        num = num + 1
    if i % 1000 == 0:
        print([i,2*i/num, np.pi])    # num/i ~ 2/pi  따라서 pi= 2*i/num

# 중성자 차폐
n = 5000
num = 0

for i in range(1,n+1):
    x = 1
    for j in range(1,8):
        v = np.pi * np.random.rand()
        x = x + np.cos(v)
        if x > 5:
            num = num + 1
            break
    if i % 1000 == 0:
        print([i, num / i * 100])
