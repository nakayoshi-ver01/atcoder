# from collections import defaultdict,deque
# import math
# import sys

# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
p='wbwbwwbwbwbw'
p=list(p)
p*=20
k=[[0,0]]
flg=0
for i in range(len(p)):
    if p[i]=='w':
        k.append([k[-1][0]+1,k[-1][1]])
    else:
        k.append([k[-1][0],k[-1][1]+1])
for i in range(len(k)):
    for j in range(i,len(k)):
        if [k[j][0]-k[i][0],k[j][1]-k[i][1]]==[n,m]:
            print('Yes')
            flg=1
            break
    if flg==1:
        break
else:
    print('No')