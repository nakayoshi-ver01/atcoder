# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
ans=0
l=1
r=2
cond=[(l,r,0)]
for i in range(q):
    h,t=map(str,input().split())
    t=int(t)%n
    for l,r,ans in cond:
        if l<=t<=r:
            if h=='L':
                
            if 
            else:
        
print(ans)
