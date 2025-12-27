# from collections import defaultdict,deque
# import sys
# import math
# import bisect
import heapq
q=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())

plant=list()
waiting=0
for _ in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        heapq.heappush(plant,waiting)
    elif a[0]==2:
        waiting+=a[1]
    elif a[0]==3:
        if plant:
            ans=0
            l=heapq.heappop(plant)
            while waiting-l>=a[1] and plant:
                ans+=1
                l=heapq.heappop(plant)
            if waiting-l<a[1]:
                heapq.heappush(plant,l)
            else:
                ans+=1
            print(ans)
        else:
            print(0)