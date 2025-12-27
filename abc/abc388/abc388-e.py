# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
a.append(0)
# s=list(input())
# grid=[list(input()) for _ in range(h)]
before=[True for _ in range(n)]
left=0
right=n//2+1
ans=(left+right)//2

# while left+1<right:
#     k=ans
#     result=0
#     cur=n//2+1
#     while cur<n:
#         if a[i]*2>a[cur]:


mark=(n+1)//2
cur=mark
ans=0
for i in range(mark):
    while cur<n:
        if a[i]*2>a[cur] or (not before[cur]):
            cur+=1
        else:
            break
    if a[i]*2<=a[cur] and before[cur]:
        before[cur]=False
        ans+=1
print(ans)