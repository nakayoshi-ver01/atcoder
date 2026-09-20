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
# grid=[list(input()) for _ in range(h)
pow_two=[str(2**i) for i in range(30)]

def dfs(d,n):
    if d!='':
        ans=[int(d)]
    else:
        ans=[]
    for i in range(30):
        if len(d)+len(pow_two[i])<=n:
            ans+=dfs(d+pow_two[i],n)
        else:
            break
    return ans

d=dfs('',10)
d.sort()

dup_less=[d[0]]
for i in range(1,len(d)):
    if d[i]!=dup_less[-1]:
        dup_less.append(d[i])

print(dup_less[n-1])