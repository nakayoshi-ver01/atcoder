# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

dp=[[[[0,0]for _ in range(3)] for _ in range(1024)]for _ in range(len(s)+1)]
dp[0][0][0][0]=1

mod=998244353
for i in range(len(s)):
    for j in range(1024):
        for k in range(3):
            for l in range(10):
                y=(10*k+l)%3
                if j==0 and l==0:
                    z=0
                else:
                    z=j|(2**l)
                if l<int(s[i]):
                    dp[i+1][z][y][1]+=dp[i][j][k][0]
                elif l==int(s[i]):
                    dp[i+1][z][y][0]+=dp[i][j][k][0]
                dp[i+1][z][y][1]+=dp[i][j][k][1]
    
    for j in range(1024):
        for k in range(3):
            for l in range(2):
                dp[i+1][j][k][l]%=mod
    
ans=0
for j in range(1,1024):
    for k in range(3):
        for l in range(2):
            cond=0
            if j.bit_count()==3:
                cond+=1
            if k==0:
                cond+=1
            if j&(2**3)>0:
                cond+=1
            if cond==1:
                ans+=dp[-1][j][k][l]
                ans%=mod
print(ans)