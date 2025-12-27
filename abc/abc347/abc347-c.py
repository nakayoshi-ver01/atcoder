from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,a,b=map(int,input().split())
d=list(map(int,input().split()))
# s=list(input())
p=defaultdict(int)
for i in d:
    p[i%(a+b)]=1

x=list(p.keys())
x.sort()
if x[-1]-x[0]<a:
    print('Yes')
else:
    for i in range(len(x)-1):
        if x[i]+a+b-x[i+1]<a:
            print('Yes')
            break
    else:
        print('No')