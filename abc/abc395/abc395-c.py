from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
num_dict=defaultdict(list)
for i in range(n):
    num_dict[a[i]].append(i)

ans=10**10

for i in num_dict:
    if len(num_dict[i])>=2:
        for j in range(len(num_dict[i])-1):
            ans=min(ans,num_dict[i][j+1]-num_dict[i][j]+1)

if ans==10**10:
    print(-1)
else:
    print(ans)