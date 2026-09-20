# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
w=list(map(int,input().split()))
c=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

w.sort(reverse=True)
c.sort(reverse=True)
def split(trucks,i):
    global w
    global c
    global n
    global m
    flg=False
    ans='No'
    print(trucks)
    if i==n:
        return 'Yes'
    
    for j in range(len(trucks)):
        if trucks[j]+w[i]<=c[j]:
            trucks[j]+=w[i]
            ans=split(trucks,i+1)
            trucks[j]-=w[i]
            flg=True
        if ans=='Yes':
            return ans
    
    if len(trucks)<m and w[i]<=c[j+1]:
        trucks.append(w[i])
        ans=split(trucks,i+1)
        del trucks[-1]
        if ans=='Yes':
            return ans
    else:
        return 'No'
    return ans
print(split([0],0))
