# from collections import defaultdict,deque
# from sortedcontainers import SortedList,SortedSet
# import sys
# import math
import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
newa=[]
newb=[]
for i in range(n):
    newa.append((a[i],i+1))
for i in range(m):
    newb.append((b[i],i))
newa.sort()
newb.sort()
dishes=[-1 for _ in range(m+1)]
person=10**8
cur=0
if n==1:
    i=0
    while i<m  and newa[0][0]<=newb[-1-i][0] :
        dishes[newb[-1-i][1]]=1
        i+=1
    for i in range(m):
        print(dishes[i])
elif m==1:
    for i in range(n):
        if a[i]>=b[0]:
            print(i+1)
            break
else:
    for i in range(m):
        while cur<n and newa[cur][0]<=newb[i][0]:
            person=min(person,newa[cur][1])
            cur+=1
        if person==10**8:
            dishes[newb[i][1]]=-1
        else:
            dishes[newb[i][1]]=person
    for i in range(m):
        print(dishes[i])
# s=list(input())