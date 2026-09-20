from collections import defaultdict,deque
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
t=int(input())
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    log=defaultdict(int)
    keys=list()
    heapq.heappush(keys,-x)
    log[x]=1
    ans=0
    for i in range(n):
        try_list=deque()
        while keys:
            cand=heapq.heappop(keys)
            if a[i]<=-cand:
                try_list.append(-cand)
            else:
                heapq.heappush(keys,cand)
                break
        while try_list:
            target=try_list.pop()
            if a[i]-1 not in log:
                heapq.heappush(keys,-(a[i]-1))
            if target%a[i] not in log:
                heapq.heappush(keys,-(target%a[i]))
            log[a[i]-1]+=log[target]*(target//a[i])   
            log[target%a[i]]+=log[target]
            del log[target]
    for i in log:
        ans+=log[i]
    print(ans-1)