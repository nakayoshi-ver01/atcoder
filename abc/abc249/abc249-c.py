from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
words=[list(input()) for _ in range(n)]

ans=0
for i in range(1,2**n):
    char=defaultdict(int)
    x=i
    cur=0
    while x>0:
        if x%2==1:
            for j in words[cur]:
                char[j]+=1
        x//=2
        cur+=1
    tmp=0
    for j in char:
        if char[j]==k:
            tmp+=1
    ans=max(ans,tmp)

print(ans)