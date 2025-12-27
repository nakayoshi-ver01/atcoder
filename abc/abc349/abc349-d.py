# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
l,r=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())

if l!=0:
    now=l
    count=0
    box=list()
    while now<r:
        x=now
        d=0
        while x%2==0:
            x//=2
            d+=1
        for i in reversed(range(d+1)):
            if now+2**i<=r:
                box.append((now,now+2**i))
                now=now+2**i
                break
else:
    l=1
    while l*2<r:

        l*=2
    now=l
    count=0
    box=list()
    while now<r:
        x=now
        d=0
        while x%2==0:
            x//=2
            d+=1
        for i in reversed(range(d+1)):
            if now+2**i<=r:
                box.append((now,now+2**i))
                now=now+2**i
                break
print(len(box))
for i in box:
    print(*i)