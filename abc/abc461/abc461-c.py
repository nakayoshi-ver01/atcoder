from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

juels=defaultdict(list)
juelmax=defaultdict(int)

for i in range(n):
    juel=list(map(int,input().split()))
    if juelmax[juel[0]]<juel[1]:
        juels[juel[0]].append(juelmax[juel[0]])
        juelmax[juel[0]]=juel[1]
    else:
        juels[juel[0]].append(juel[1])
cand=[]
for color in juelmax:
    cand.append(juelmax[color])

cand.sort()

ans=0
for _ in range(m):
    ans+=cand.pop()
    k-=1
for color in juels:
    cand+=juels[color][1:]

cand.sort()

if k!=0:
    print(ans+sum(cand[-k:]))
else:
    print(ans)