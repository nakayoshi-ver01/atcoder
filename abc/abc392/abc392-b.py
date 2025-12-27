# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
ok=[True for _ in range(n)]

for i in a:
    ok[i-1]=False

ans=[]
for i in range(n):
    if ok[i]:
        ans.append(i+1)

print(len(ans))
print(*ans)