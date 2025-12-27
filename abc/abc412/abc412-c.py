# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    n=int(input())
    first,*a,last=map(int,input().split())
    a.sort()
    b=[0 for _ in range(n)]
    for i in range(n-2):
        b[i+1]=a[i]
    b[0]=first
    b[-1]=last
    k=[first]
    cur=1
    cand=10**10
    while cur<n:
        if k[-1]*2>=b[cur]:
            cand=cur
            cur+=1
        else:
            if cand==10**10:
                print(-1)
                break
            else:
                if b[cand]*2>=b[cur]:
                    k.append(b[cand])
                else:
                    print(-1)
                    break
    else:
        if k[-1]*2>=b[-1]:
            k.append(b[-1])
            print(len(k))
        else:
            print(-1)