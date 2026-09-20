# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

def recur(n,w):
    if n==-1:
        return 0
    else:
        for i in reversed(range(n)):
            if baggage[i][0]<=w-baggage[n][0]:
                cand=i
                break
        else:
            cand=-1
        # 使わない 
        cand1=acc[n][1]
        # 使う
        cand2=baggage[n][1]+recur(cand,w-baggage[n][0])
        return max(cand1,cand2)

for _ in range(t):
    n,w=map(int,input().split())
    baggage=[list(map(int,input().split())) for _ in range(n)]

    acc=[(0,0)]
    for i in range(n):
        acc.append((acc[-1][0]+baggage[i][0],acc[-1][1]+baggage[i][1]))
    # print(baggage)
    # print(acc)
    ans=recur(n-1,w)
    print(ans)