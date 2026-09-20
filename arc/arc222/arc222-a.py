from collections import defaultdict,deque
from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    n,m=map(int,input().split())
    ans=[-1 for _ in range(n)]
    query=defaultdict(int)
    for i in range(m):
        l,r=map(int,input().split())
        query[l-1]=max(r,query[l-1])
    
    
    use_num=[]
    can_use=[True for _ in range(n+1)]
    for i in range(n):
        heapq.heappush(use_num,i+1)
    
    log=-1
    cur=-1
    lk=list(query.keys())
    lk.sort()
    for i in lk:
        if query[i]<=cur:
            continue
        else:
            if log!=-1:
                for j in range(log,min(query[log],i)):
                    if not can_use[ans[j]]:
                        can_use[ans[j]]=True
                        heapq.heappush(use_num,ans[j])
            for j in range(max(cur+1,i),query[i]):
                if ans[j]==-1:
                    ans[j]=heapq.heappop(use_num)
                    can_use[ans[j]]=False
                cur=j
            log=i
    
    for i in range(n):
        if ans[i]==-1:
            ans[i]=1
    print(*ans)