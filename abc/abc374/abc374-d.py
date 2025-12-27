# from collections import defaultdict,deque
import itertools
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,s,t=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
point=list()
root=[i for i in range(n)]
p = itertools.permutations(root, n)
for i in range(n):
    a=list(map(int,input().split()))
    point.append(((a[0],a[1]),(a[2],a[3])))

ans=10**20
for i in p:
    for j in range(2**n):
        now=(0,0)
        total_len=0
        num=j
        for k in range(n):
            if j%2==0:
                total_len+=((now[0]-point[i[k]][0][0])**2+(now[1]-point[i[k]][0][1])**2)**(1/2)/s
                total_len+=((point[i[k]][1][0]-point[i[k]][0][0])**2+(point[i[k]][1][1]-point[i[k]][0][1])**2)**(1/2)/t
                now=(point[i[k]][1][0],point[i[k]][1][1])
            else:
                total_len+=((now[0]-point[i[k]][1][0])**2+(now[1]-point[i[k]][1][1])**2)**(1/2)/s
                total_len+=((point[i[k]][0][0]-point[i[k]][1][0])**2+(point[i[k]][0][1]-point[i[k]][1][1])**2)**(1/2)/t
                now=(point[i[k]][0][0],point[i[k]][0][1])
            j//=2
        if ans>total_len:
            ans=total_len
print(ans)