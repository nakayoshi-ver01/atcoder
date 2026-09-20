from collections import defaultdict
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,d=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

log=defaultdict(set)

for i in range(n):
    s,t=map(int,input().split())
    if t-s>=d:
        log[s].add(i+1)
        log[t+1].add(-(i+1))
        
person=set()
for i in log[0]:
    if i>0:
        person.add(i)

ans=(len(person)*(len(person)-1))//2

times=tuple(log.keys())
end_time=max(times)
for i in range(end_time+1-d):
    for j in log[i]:
        if j>0:
            person.add(j)
    for j in log[i+d]:
        if j<0:
            person.discard(-j)
    ans+=(len(person)*(len(person)-1))//2

print(ans)