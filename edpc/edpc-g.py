from collections import defaultdict
from functools import lru_cache
import sys

sys.setrecursionlimit(10**9)
n,m=map(int,input().split())
# 木作成
edge=defaultdict(set)
no_in={i+1 for i in range(n)}
for _ in range(m):
    x,y=map(int,input().split())
    edge[x].add(y)
    no_in.discard(y)

dp=[-1 for _ in range(n+1)]
@lru_cache
def search(n):
    global dp
    global edge
    if dp[n]!=-1:
        return dp[n]
    f=0
    for i in edge[n]:
        f=max(search(i)+1,f)
    dp[n]=f
    return dp[n]

for i in no_in:
    search(i)
print(max(dp))