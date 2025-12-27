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

a=set()

def make_lunlun(n):
    global a
    a.add(int(n))
    if len(n)==10:
        return 0
    else:
        for i in range(max(int(n[-1])-1,0),min(int(n[-1])+2,10)):
            make_lunlun(n+str(i))


for i in range(0,10):
    make_lunlun(str(i))

a_l=[]
for i in a:
    a_l.append(int(i))
a_l.sort()

print(a_l[n])