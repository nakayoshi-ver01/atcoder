from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

edge=defaultdict(set)
cent_edge=defaultdict(set)
for i in range(n-1):
    u,v=map(int,input().split())
    edge[u-1].add((i+1,v-1))
    edge[v-1].add((i+1,u-1))
    cent_edge[u-1].add(v-1)
    cent_edge[v-1].add(u-1)

def tree_centroid(g):
    """
    木の重心を 1 つ求める。O(頂点数)

    辞書にある任意の頂点を根に、スタックで部分木サイズを求めたあと、
    size[u] > n//2 の子がある限りその子へ降りる。
    そのような子は高々 1 つで、無くなった頂点が重心。
    重心が 2 個あるときは、根から見て重い側のほうを返す。

    Parameters
    ---------------------
    g : dict[int, set[int]]
        無向木。キーが頂点、値が隣接頂点の集合。
        辺は両方向に入れ、全部の頂点をキーにする。
        例: {1: {2}, 2: {1, 3}, 3: {2}}

    Returns
    ---------------------
    centroid : int
        重心の頂点番号
    """
    n = len(g)
    root = next(iter(g))
    parent = {root: None}
    order = []
    st = [root]
    while st:
        v = st.pop()
        order.append(v)
        for u in g[v]:
            if u not in parent:
                parent[u] = v
                st.append(u)

    size = {v: 1 for v in order}
    for v in reversed(order):
        p = parent[v]
        if p is not None:
            size[p] += size[v]

    v, p = root, None
    half = n // 2
    while True:
        heavy = None
        for u in g[v]:
            if u != p and size[u] > half:
                heavy = u
                break
        if heavy is None:
            return v
        p, v = v, heavy

center=tree_centroid(cent_edge)

ans=[-1 for _ in range(n)]

state=deque()
start=((n*(n-1))//2,center)
state.append(start)
while state:
    now=state.popleft()
    ans[now[1]]=now[0]
    for i in edge[now[1]]:
        if ans[i[1]]==-1:
            state.append((now[0]-i[0],i[1]))

print(*ans)