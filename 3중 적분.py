import numpy as np
import matplotlib.pyplot as plt

# 3중 적분
'''
n = 50000
num_A = 0 # 전체 점의 개수
num_D = 0 # 영역안의 점의 개수

#x,y,z 박스 안의 점 찍기
while num_A < n:
    x = np.random.rand() 
    y = np.random.rand()
    z = np.random.rand()
    num_A += 1
    
    if x**2 + np.sin(y) <= z and x-z+np.exp(y) <=1:
        num_D += 1
    if num_A % 1000 == 0:
        print([num_A,num_D,num_D/num_A])
'''

n = 50000
num_A = 0 # 전체 점의 개수
num_D = 0 # 영역안의 점의 개수

#x,y,z 박스 안의 점 찍기
while num_A < n:
    x = 2*np.random.rand()-1 
    y = 2*np.random.rand()-1
    z = 2*np.random.rand()
    num_A += 1
    
    if np.sqrt(x**2 + y**2) <= z and x**2 + y**2 + (z-1)**2 <=1:
        num_D += 1
    if num_A % 1000 == 0:
        print([num_A,num_D,8*num_D/num_A])