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

person=[]
young=10**10
st=0
for i in range(n):
    a=list(map(str,input().split()))
    if young>int(a[1]):
        young=int(a[1])
        st=i
    person.append(a)

for i in range(n):
    print(person[(i+st)%n][0])