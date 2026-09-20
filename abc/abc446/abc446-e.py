# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
m,a,b=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
count=0
ok=set()
ng=set()
for i in range(1,m):
    for j in range(1,m):
        k,l=i,j
        temp=set()
        while ((k,l) not in temp) and ((k,l) not in ok) and ((k,l) not in ng):
            temp.add((k,l))
            k,l=(k*a+l*b)%m,k
            if k==0:
                ng|=temp
                break
            if (k,l) in ok:
                ok|=temp
                break
            elif (k,l) in ng:
                ng|=temp
                break
        else:
            ok|=temp
print(len(ok))