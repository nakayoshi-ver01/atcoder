# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())

ans=0
for i in range(n-2):
    if s[i]=='#' and s[i+1]=='.' and s[i+2]=='#':
        ans+=1
print(ans)