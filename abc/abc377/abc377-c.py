# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
ans=n**2
unplace=set()
for i in range(m):
    a,b=map(int,input().split())
    unplace.add((a,b))
    if a+1<=n and b+2<=n:
        unplace.add((a+1,b+2))
    if a+2<=n and b+1<=n:
        unplace.add((a+2,b+1))
    if 0<a-1 and b+2<=n:
        unplace.add((a-1,b+2))
    if 0<a-2 and b+1<=n:
        unplace.add((a-2,b+1))
    if 0<a-2 and 0<b-1:
        unplace.add((a-2,b-1))
    if 0<a-1 and 0<b-2:
        unplace.add((a-1,b-2))
    if a+1<=n and 0<b-2:
        unplace.add((a+1,b-2))
    if a+2<=n and 0<b-1:
        unplace.add((a+2,b-1))

ans-=len(unplace)
print(ans)