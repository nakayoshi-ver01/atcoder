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


ans=0
cur_l=1
cur_r=2
count=0
while cur_l<n+1 and cur_r<n+1:
    print('?',cur_l,cur_r)
    count+=1
    x=input()
    # x='No'
    if x=='Yes':
        cur_r+=1
    else:
        ans+=cur_r-cur_l-1
        cur_l+=1
        if cur_l==cur_r:
            cur_r+=1
for i in range(cur_l,n):
    ans+=n-i


# for i in range(1,n):
#     ok=max(i,ok)
#     ng=n+1
#     center=(ok+ng)//2
#     while ok+1<ng:
#         count+=1
#         print('?',i,center)
#         x='No'
#         if x=='Yes':
#             ok=center
#         else:
#             ng=center
#         center=(ok+ng)//2
#     ans+=ok-i
#     print(i,count)
print('!',ans)
