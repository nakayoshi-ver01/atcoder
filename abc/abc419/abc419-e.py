# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m,l=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

dp=[[10**10 for _ in range(m)] for _ in range(n-l+1)]

first_states=[sum(a[:l])%m]
dp[0][first_states[-1]]=0
for i in range(l,n):
    first_state=first_states[-1]
    first_state-=a[i-l]
    first_state+=a[i]
    first_state%=m
    first_states.append(first_state)
    dp[i-l+1][first_state]=0

print(first_states)
print(dp)

for i in range(n):
    for j in range(max(0,i-l+1),min(i+1,n-l+1)):
        for k in range(1,m):
            move=10**10
            for r in range(max(0,i-l+1),min(i+1,n-l+1)):
                move=min(move,dp[r][(first_states[r]+k)%m],dp[r][first_states[r]]+k)
            print(move)
            for r in range(max(0,i-l+1),min(i+1,n-l+1)):
                dp[r][(first_states[r]+k)%m]=move
    print(dp)