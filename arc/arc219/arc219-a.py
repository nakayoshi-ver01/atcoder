# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
a=[]
for i in range(n):
    a.append(input())
ans=''
bf=[True for i in range(n)]
for i in range(m):
    z_count=0
    o_count=0
    for j in range(n):
        if bf[j]:
            if a[j][i]=='0':
                z_count+=1
            else:
                o_count+=1
    if z_count>=o_count:
        ans+='0'
        for j in range(n):
            if a[j][i]=='0':
                bf[j]=False
    else:
        ans+='1'
        for j in range(n):
            if a[j][i]=='1':
                bf[j]=False

if all(not bf[i] for i in range(n)):
    print('Yes')
    print(ans)
else:
    print('No')
