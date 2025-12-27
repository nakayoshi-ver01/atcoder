# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,c=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())

ans=1
last=a[0]
for i in range(1,n):
    if a[i]-last>=c:
        ans+=1
        last=a[i]
print(ans)