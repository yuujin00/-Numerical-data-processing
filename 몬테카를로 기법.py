import numpy as np

# 랜덤값 가지고 적분값 계산 -> 이중적분, 입체, 넓이, 부피도 가능(다음시간)
# 0에서1 x**2 적분값 = 1/3 = 0.3333 근사
'''
for j in range(10, 500):
    R = np.zeros(100)
    for i in range(1, 100):
        R[i] = (np.random.rand())**2
    result = 1/100 * sum(R)
    print(result)
'''

# 부피
n = 50000
num_A = 0  # 박스안의 점의 개수
num_D = 0  # 영역안의 점의 개수
while num_A < n:
    x = np.random.rand()
    y = np.random.rand()
    z = np.random.rand()
    num_A = num_A + 1
    if x**2 + np.sin(y) <= z and x - z + np.exp(y) <= 1:
        num_D = num_D + 1
    if num_A % 1000 == 0:
        print([num_A, num_D, num_D/num_A])

# 수치이중적분
n = 5000
sum = 0
for i in range (0,n):
    x = np.random.rand()
    y = np.random.rand()
    if ((x-1/2)**2 + (y-1/2)**2) <= 1/4:
        sum += np.sin(np.sqrt((np.log(x+y+1))))
        i += 1
        if i % 1000 == 0:
            res = np.pi/4 * sum / i   # 범위 넓이 * 1/(개수) * 함수 시그마(합)
            print([i, res])
