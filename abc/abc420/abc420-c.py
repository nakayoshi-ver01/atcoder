# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

ans=0
for i in range(n):
    ans+=min(a[i],b[i])

for _ in range(q):
    query=list(map(str,input().split()))
    if query[0]=='A':
        abf=a[int(query[1])-1]
        bbf=b[int(query[1])-1]
        q=int(query[2])
        if abf<=bbf<=q:
            ans+=bbf-abf
        elif abf<=q<=bbf:
            ans+=q-abf
        elif bbf<=q<=abf:
            pass
        elif bbf<=abf<=q:
            pass
        elif q<=bbf<=abf:
            ans+=q-bbf
        elif q<=abf<=bbf:
            ans+=q-abf
        a[int(query[1])-1]=q
    elif query[0]=='B':
        abf=a[int(query[1])-1]
        bbf=b[int(query[1])-1]
        q=int(query[2])
        if abf<=bbf<=q:
            pass
        elif abf<=q<=bbf:
            pass
        elif bbf<=q<=abf:
            ans+=q-bbf
        elif bbf<=abf<=q:
            ans+=abf-bbf
        elif q<=bbf<=abf:
            ans+=q-bbf
        elif q<=abf<=bbf:
            ans+=q-abf
        b[int(query[1])-1]=q
    print(ans)