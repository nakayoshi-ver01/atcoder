# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
import heapq
# n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
need=list()
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
heapq.heappush(need,(-1*(a[0]*b[0]+c[0]*b[0]+a[0]*c[0]),0,0,0))
count=0
af=set()
while count<k:
    count+=1
    target=heapq.heappop(need)
    if count==k:
        print(target[0]*(-1))
        break
    if target[1]<n-1 and (target[1]+1,target[2],target[3]) not in af:
        next_value=-1*(a[target[1]+1]*b[target[2]]+c[target[3]]*b[target[2]]+a[target[1]+1]*c[target[3]])
        heapq.heappush(need,(next_value,target[1]+1,target[2],target[3]))
        af.add((target[1]+1,target[2],target[3]))
    if target[2]<n-1 and (target[1],target[2]+1,target[3]) not in af:
        next_value=-1*(a[target[1]]*b[target[2]+1]+c[target[3]]*b[target[2]+1]+a[target[1]]*c[target[3]])
        heapq.heappush(need,(next_value,target[1],target[2]+1,target[3]))
        af.add((target[1],target[2]+1,target[3]))
    if target[3]<n-1 and (target[1],target[2],target[3]+1) not in af:
        next_value=-1*(a[target[1]]*b[target[2]]+c[target[3]+1]*b[target[2]]+a[target[1]]*c[target[3]+1])
        heapq.heappush(need,(next_value,target[1],target[2],target[3]+1))
        af.add((target[1],target[2],target[3]+1))

# s=list(input())
# grid=[list(input()) for _ in range(h)]
