# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

ans=0

for i in range(len(s)):
    flg=True
    for j in range(min(i,len(s)-i-1)+1):
        if s[i-j]!=s[i+j]:
            if flg:
                flg=False
            else:
                break
        ans+=1
for i in range(len(s)-1):
    flg=True

    for j in range(min(i,len(s)-i-2)+1):
        if s[i-j]!=s[i+1+j]:
            if flg:
                flg=False
            else:
                break
        ans+=1
print(ans)