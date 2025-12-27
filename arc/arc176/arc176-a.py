from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
mod=defaultdict(set)

origin=set()
ans=set()
nmods=set()
for _ in range(m):
    a,b=map(int,input().split())
    origin.add((a,b))
    if not mod[(a+b)%n]:
        nmods.add((a+b)%n)
    mod[(a+b)%n].add((a,b))

enough=0
while len(nmods)<m:
    if enough not in nmods:
        nmods.add(enough)
    enough+=1

for i in nmods:
    for j in range(1,n+1):
        x=(i-j)%n
        if x<=0:
            x+=n
        if (j,x) not in origin:
            ans.add((j,x))

print(len(ans|origin))
for i in ans|origin:
    print(*i)
# a=list(map(int,input().split()))
# s=list(input())