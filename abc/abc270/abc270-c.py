from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import math
# import bisect
# import heapq
# n=int(input())
n,x,y=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

edge=defaultdict(set)
for _ in range(n-1):
    u,v=map(int,input().split())
    edge[u].add(v)
    edge[v].add(u)

af=[True for _ in range(n+1)]

state=deque()

state.append(x)

af[x]=False
while state[-1]!=y:
    for i in edge[state[-1]]:
        if af[i]:
            edge[state[-1]].remove(i)
            af[i]=False
            state.append(i)
            break
    else:
        state.pop()

print(*state)