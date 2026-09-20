from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

finals=defaultdict(set)
count=0
for i in range(m):
    match=list(map(int,input().split()))
    if match[0] not in finals[match[1]]:
        finals[match[1]].add(match[0])
        finals[match[0]].add(match[1])
        count+=1

final_count=[]
for i in range(1,n+1):
    final_count.append((len(finals[i]),i))

final_count.sort()

ans=0
for player in range(len(final_count)):
    x=bisect.bisect_left(final_count,(count-final_count[player][0],0))
    cur=max(x,player+1)
    for i in range(max(x,player+1),n):
        if final_count[i][1] in finals[final_count[player][1]]:
            if count==final_count[i][0]+final_count[player][0]-1:
                ans+=1
        else:
            if count==final_count[i][0]+final_count[player][0]:
                ans+=1
        if final_count[i][0]!=count-final_count[player][0]:
            break
        cur+=1
    if cur!=n:
        ans+=n-cur-1

print(ans)