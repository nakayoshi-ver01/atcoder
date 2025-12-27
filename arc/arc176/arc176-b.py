# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
cand=[6,2,4,8]
for _ in range(t):
    n,m,k=map(int,input().split())
    
    if n<m-1:
        print(cand[n%4])
    elif k==m-1:
        print(0)
    else:
        i=0
        while n<=m:
            if i==0:
                n=k+(n-m)
                i=1
            else:
                n=k+(n-m-1)
        print(cand[(k+n-m)%4])
    