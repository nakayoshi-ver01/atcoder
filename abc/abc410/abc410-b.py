from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
x=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

boxes=defaultdict(int)

ans=[]
for i in range(q):
    if x[i]>=1:
        boxes[x[i]]+=1
        ans.append(x[i])
    else:
        call=10**10
        val=10**10
        for j in range(1,n+1):
            if val>boxes[j]:
                call=j
                val=boxes[j]
        boxes[call]+=1
        ans.append(call)

print(*ans)