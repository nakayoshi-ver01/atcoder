from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

def rec(i,af):
    for tar in week_edge[i]:
        if tar not in af:
            ans=rec(tar,af|{i})
        else:
            return True
        
        if ans:
            break
    else:
        ans=False
    return ans

for _ in range(t):
    n,m=map(int,input().split())
    
    root=defaultdict(set)
    for i in range(n):
        root[i].add(i)
    for i in range(m):
        u,v=map(int,input().split())
        root[u-1].add(v-1)
        root[v-1].add(u-1)
    w=int(input())
    holidays=[list(input()) for _ in range(n)]
    start=set()
    for i in range(n):
        if holidays[i][0]=='o':
            start.add(i)
    week_edge=defaultdict(set)
    # O(nw)
    for i in start:
        state=deque()
        state.append((i,0))
        af_set={(i,0)}
        while state:
            now=state.popleft()
            if now[1]==w:
                week_edge[i].add(now[0])
            else:
                for j in root[now[0]]:
                    if holidays[j][(now[1]+1)%w]=='o' and ((j,now[1]+1) not in af_set):
                        state.append((j,now[1]+1))
                        af_set.add((j,now[1]+1))
    flg=False
    cand=list(week_edge.keys())
    for i in cand:
        af={i}
        ans=rec(i,af)
        if ans:
            print('Yes')
            break
    else:
        print('No')
