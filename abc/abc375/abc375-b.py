# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
import copy
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
ans=0
now=[0,0]
for i in range(n):
    a=list(map(int,input().split()))
    ans+=((now[0]-a[0])**2+(now[1]-a[1])**2)**(1/2)
    now=copy.deepcopy(a)
ans+=(now[0]**2+now[1]**2)**(1/2)
print(ans)