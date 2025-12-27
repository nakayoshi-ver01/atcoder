# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
query=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

a=[0 for _ in range(n+2)]

ans=0

for i in query:
    
    if a[i]==0:
        if a[i-1]==1 and a[i+1]==1:
            ans-=1
        elif a[i-1]==1 and a[i+1]==0:
            pass
        elif a[i-1]==0 and a[i+1]==1:
            pass
        elif a[i-1]==0 and a[i+1]==0:
            ans+=1
    if a[i]==1:
        if a[i-1]==1 and a[i+1]==1:
            ans+=1
        elif a[i-1]==1 and a[i+1]==0:
            pass
        elif a[i-1]==0 and a[i+1]==1:
            pass
        elif a[i-1]==0 and a[i+1]==0:
            ans-=1
    a[i]+=1
    a[i]%=2
    print(ans)