# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
a.sort(reverse=True)


ans=10**20
for i in range(2**n):
    x=0
    y=0
    k=i
    for j in range(n):
        if k%2==0:
            x+=a[j]
        else:
            y+=a[j]
        k//=2
    if ans>max(x,y):
        ans=max(x,y)
print(ans)