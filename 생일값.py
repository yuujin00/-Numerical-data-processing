import numpy as np

# 생일문제 
#이론값

num=51

for n in range (1,num):
    p=1
    for k in range (1,n+1):
        p *=(365-k+1)/365
    if n % 5 == 0:
        print('%3d %1.3f' %(n,1-p)) 
        print([n,round((1-p)*100)]) # 페센트로

'''
#시물레이션
res =0

for k in range(0,1000):
    B = np.zeros(n)
    for j in range(0,n):
        B[j] = int(np.ceil(np.random.rand()*365))
    if len(set(B)) < n:
        res += 1
    if n % 5 == 0:
        print([n,round((1-p)*1000)/1000, res/1000]) # 이론, 실험
'''