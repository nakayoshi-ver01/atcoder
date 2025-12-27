from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
import heapq
# n=int(input())
n,m,h=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

# good_pattern = [
#     score,
#     parents,
#     height
#     af,
# ]

edges=defaultdict(list)

values=[(a[i],i) for i in range(n)]
values.sort()
dots=[]
for _ in range(m):
    u,v=map(int,input().split())
    edges[u].append((a[v],v))
    edges[v].append((a[u],u))

for _ in range(n):
    f=tuple(map(int,input().split()))
    dots.append(f)


def beamsearch(good_pattern,procedure):
    global a
    width=1
    tmp_result=list()
    for _ in range(min(len(good_pattern),width)):
        target=heapq.heappop(good_pattern)
        waiting_line=deque()
        score=target[0]
        parents=target[1]
        height=target[2]
        af=target[3]
        if af[procedure]:
            heapq.heappush(tmp_result,target)
            continue
        waiting_line=deque()
        waiting_line.append((procedure,0))
        af[procedure]=True
        while waiting_line:
            now=waiting_line.popleft()
            height[now[0]]=now[1]
            score-=now[1]*a[now[0]]
            if now[1]<10:
                edges[now[0]].sort()
                for edge in edges[now[0]]:
                    if not af[edge[1]]:
                        af[edge[1]]=True
                        waiting_line.append((edge[1],now[1]+1))
                        parents[edge[1]]=now[0]
        heapq.heappush(tmp_result,(score,parents,height,af))
    topk=[heapq.heappop(tmp_result) for _ in range(min(len(tmp_result),width))]
    return topk
score=0
parents=[-1 for _ in range(n)]
height=[-1 for _ in range(n)]
af=[False for _ in range(n)]
good_pattern=[]
heapq.heappush(good_pattern,[score,parents,height,af])
for i in range(n):
    good_pattern=beamsearch(good_pattern,values[i][1])

most=heapq.heappop(good_pattern)
print(*most[1])
