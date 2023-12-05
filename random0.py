import numpy as np

#나머지(mod) = %
'''
def rand0(n,x0):
    X = np.zeros(n+1)
    X[0] = x0
    R = np.zeros(n+1)
    for i in range(0,n):
        X[i+1] = (110351545 * X[i] + 12345) % (2**31)
        R[i+1] = X[i+1] / 2**31
    return R

#print(rand0(100,3))
'''

def rand0(n,x0):
    X = np.zeros(n+1)
    X[0] = x0
    R= np.zeros(n+1)
    for i in range(0,n):
        X[i+1]=(110351545 * X[i] + 12345) % (2**31)
        R[i+1]=X[i+1]/2**31
    return R

testnum = 50000 # R = rand0(testnum,3)
m = 0 # rand()에서 1/2보다 작은 수의 개수 -> 50%여야 랜덤
for i in range(1,testnum+1):
    r = np.random.rand() # 파이썬 내장함수 사용(0~1사이)
    #R[i] <= 1/2 
    if r <= 1/2: 
        m = m + 1
    if i % 1000 == 0:
        per = m / i *100
        print([i,per])


### 변형
for i in range(1,testnum+1):
    r = np.random.rand()
    '''#(-2,2)사이에서 랜덤한 수 만들기
    (2-(-2))*np.random.rand()-2'''

    '''#(a,b) 사이의 랜덤한 수 (0,b-a)
    (b-a)*r+a'''

    '''# 0~n 자연수  (0,n+1)
    round((n+1)*r) -> 반올림해서 정수로 만듦'''

    '''#15~40 자연수 (0, 25)
    25*r+15'''