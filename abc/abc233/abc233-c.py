# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,x=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

boxes=list()
for _ in range(n):
    l,*box=map(int,input().split())
    boxes.append(box)


def dfs(i,now):
    global boxes
    global x
    if i==n-1:
        ans=0
        for j in range(len(boxes[i])):
            if now*boxes[i][j]==x:
                ans+=1
        return ans
    else:
        ans=0
        for j in range(len(boxes[i])):
            if now*boxes[i][j]<=x:
                ans+=dfs(i+1,now*boxes[i][j])
        return ans
print(dfs(0,1))