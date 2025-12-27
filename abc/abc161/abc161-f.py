# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

t=n-1

cand=set()

for i in range(1,int(t**(1/2))+1):
    if t%i==0:
        cand.add(i)
        cand.add(t//i)

cand2=set()
for i in range(1,int(n**(1/2))+1):
    if n%i==0:
        cand2.add(i)
        cand2.add(n//i)


for i in cand2:
    if i!=1:
        x=n
        while x>1:
            if x%i==0:
                x=x//i
            else:
                if x>=i:
                    x-=i*(x//i)
                else:
                    x-=i
        if x==1:
            cand.add(i)

print(len(cand)-1)