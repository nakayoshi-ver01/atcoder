# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    a=list(map(int,input().split()))
    x1=2*a[0]-2*a[2]
    x2=a[0]**2-a[2]**2+a[1]**2-a[3]**2
    x3=2*a[1]-2*a[3]
    x4=2*a[4]-2*a[6]
    x5=a[4]**2-a[6]**2+a[5]**2-a[7]**2
    x6=2*a[5]-2*a[7]
    k1=math.gcd(x1,x3)
    k2=math.gcd(x4,x6)
    x1//=k1
    x2/=k1
    x3//=k1
    x4//=k2
    x5/=k2
    x6//=k2
    if x1<0 or (x1==0 and x3<0):
        x1*=-1
        x2*=-1
        x3*=-1
    if x4<0 or (x4==0 and x6<0):
        x4*=-1
        x5*=-1
        x6*=-1
    if (x1,x3)!=(x4,x6):
        print('Yes')
    elif x2==x5:
        print('Yes')
    else:
        print('No')