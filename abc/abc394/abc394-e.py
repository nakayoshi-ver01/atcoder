from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

edge=defaultdict(set)
for i in range(n-1):
    u,v=map(int,input().split())
    edge[u].add(v)
    edge[v].add(u)

num_edge=[0]
num_edge_key=set()
for i in range(1,n+1):
    num_edge.append(len(edge[i]))
    if len(edge[i])>=4:
        num_edge_key.add(i)

ans=0
dp=[-1 for _ in range(n+1)]
end=set()
def rec(n,af):
    global edge
    global dp
    global end
    global k
    if n!=k and len(edge[n])<4:
        dp[n]=1
        return 1
    sample=list()
    for i in edge[n]:
        if dp[i]==-1 and (i not in af):
            af.add(i)
            end.add(i)
            sample.append(rec(i,af))
            af.remove(i)
        elif dp[i]!=-1:
            sample.append(dp[i])
    sample.sort()
    if len(edge[n])<4:
        if sample and sample[0]!=1:
            dp[n]=sample[0]+1
        else:
            dp[n]=1
    else:
        dp[n]=sum(sample[:4])+1
    return dp[n]

before={i+1 for i in range(n)}
while before:
    k=before.pop()
    bbb=rec(k,{k})
    end.add(k)
    before-=end

g=max(dp)


if g>1:
    print(g)
else:
    print(-1)