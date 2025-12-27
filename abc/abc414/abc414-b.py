# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

ans=''
count=0
for _ in range(n):
    c,l=map(str,input().split())
    count+=int(l)
    if count>100:
        print('Too Long')
        break
    else:
        ans+=c*int(l)
else:
    print(ans)