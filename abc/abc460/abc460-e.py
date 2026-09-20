# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
MOD=998244353
for _ in range(t):
    ans=0
    n,m=map(int,input().split())
    for i in range(1,len(str(n))):
        x=m//math.gcd(m,10**i-1)
        if x<=n:
            ans+=(n//x)*(10**i-10**(i-1))
        ans%=MOD
    
    x=m//math.gcd(m,10**len(str(n))-1)
    if x<=n:
        ans+=(n//x)*(n-10**(len(str(n))-1)+1)
    ans%=MOD
    print(ans)