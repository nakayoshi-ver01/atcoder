from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

pos=defaultdict(int)
pos[0]=0
for i in range(n):
    pos[a[i]]+=1

acc_pos=defaultdict(int)

pos_key=list(pos.keys())
pos_key.sort()

for i in range(len(pos_key)):
    if i==0:
        acc_pos[pos_key[i]]=pos[pos_key[i]]
    else:
        acc_pos[pos_key[i]]=pos[pos_key[i]]+acc_pos[pos_key[i-1]]

count=0
remain_point=n-pos[0]
for i in range(1,len(pos_key)):
    if k>=count+remain_point*(pos_key[i]-pos_key[i-1]):
        count+=remain_point*(pos_key[i]-pos_key[i-1])
        remain_point-=pos[pos_key[i]]
    else:
        loop=(k-count)//remain_point
        fix=pos_key[i-1]
        break
else:
    loop=0
    fix=pos_key[-1]


counter=0
for i in range(n):
    counter+=min(a[i],fix)
    a[i]-=min(a[i],fix)

for i in range(n):
    counter+=min(a[i],loop)
    a[i]-=min(a[i],loop)

for i in range(n):
    if counter<k:
        counter+=min(a[i],1)
        a[i]-=min(a[i],1)
    else:
        break

print(*a)