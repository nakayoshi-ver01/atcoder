from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq

DIR=((1,0),(-1,0),(0,1),(0,-1))

# 最寄りの公園角へのチェビシェフ距離（開始点選び用）
def cheb_to_corner(x,y):
    return min(
        max(x,y),
        max(x,n-1-y),
        max(n-1-x,y),
        max(n-1-x,n-1-y),
    )

# 最寄り角から見た「公園の内側」方向 (+1/-1, +1/-1)
def inward_dirs(sx,sy):
    cands=[
        (max(sx,sy),1,1),                 # (0,0) → +x +y
        (max(sx,n-1-sy),1,-1),            # (0,n-1) → +x -y
        (max(n-1-sx,sy),-1,1),            # (n-1,0) → -x +y
        (max(n-1-sx,n-1-sy),-1,-1),       # (n-1,n-1) → -x -y
    ]
    cands.sort()
    return cands[0][1],cands[0][2]

# 現領域への隣接数が多いフロンティアを優先して成長（コンパクト寄り）
def gather(sx,sy,p):
    if grid[sx][sy]=='#' or occupied[sx][sy]>=0:
        return None
    sx_dir,sy_dir=inward_dirs(sx,sy)

    def pen(x,y):
        px=0 if (x-sx)*sx_dir>=0 else 1
        py=0 if (y-sy)*sy_dir>=0 else 1
        return px+py

    region={(sx,sy)}
    cells=[(sx,sy)]
    frontier={}  # (x,y) -> 現領域との隣接数

    def touch(x,y):
        for dx,dy in DIR:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]=='.' and occupied[nx][ny]<0 and (nx,ny) not in region:
                frontier[nx,ny]=frontier.get((nx,ny),0)+1

    touch(sx,sy)
    while len(cells)<p:
        if not frontier:
            return None
        best=None
        best_key=None
        for (x,y),adj in frontier.items():
            key=(-adj,pen(x,y),max(abs(x-sx),abs(y-sy)),abs(x-sx)+abs(y-sy),x,y)
            if best_key is None or key<best_key:
                best_key=key
                best=(x,y)
        x,y=best
        del frontier[x,y]
        region.add((x,y))
        cells.append((x,y))
        touch(x,y)
    return cells

# 周dの各辺で、両端から辺上の最初の空きを種にする（辺あたり最大2）
def ring_seeds(d):
    lo,hi=d,n-1-d
    if lo>hi:
        return []
    if lo==hi:
        if grid[lo][lo]=='.' and occupied[lo][lo]<0:
            return [(lo,lo)]
        return []

    seeds=[]
    seen=set()

    def add(x,y):
        if (x,y) not in seen and grid[x][y]=='.' and occupied[x][y]<0:
            seen.add((x,y))
            seeds.append((x,y))

    def first_free_on_edge(points):
        for x,y in points:
            if grid[x][y]=='.' and occupied[x][y]<0:
                return (x,y)
        return None

    # 上辺: (lo,lo)→(lo,hi) と逆
    top=[(lo,y) for y in range(lo,hi+1)]
    bottom=[(hi,y) for y in range(lo,hi+1)]
    left=[(x,lo) for x in range(lo,hi+1)]
    right=[(x,hi) for x in range(lo,hi+1)]

    for edge in (top,bottom,left,right):
        a=first_free_on_edge(edge)
        b=first_free_on_edge(edge[::-1])
        if a is not None:
            add(*a)
        if b is not None:
            add(*b)

    # 角に近い順
    seeds.sort(key=lambda ij:cheb_to_corner(ij[0],ij[1]))
    return seeds

# 空きのある周上の角寄り種 → ダメなら5マス内側の周、…
def try_place(p):
    for d in range(0,(n+1)//2,5):
        for sx,sy in ring_seeds(d):
            cells=gather(sx,sy,p)
            if cells is not None:
                return cells
    return None

# n=int(input())
n,m,r=input().split()
n,m,r=int(n),int(m),float(r)
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(n)]

occupied=[[-1]*n for _ in range(n)]
active={}  # gid -> (T, cells)

for _ in range(m):
    i,S,T,P,V=map(int,input().split())
    # 退去済みを解放
    for gid in [gid for gid,(t,_) in active.items() if t<S]:
        _,cells=active.pop(gid)
        for x,y in cells:
            occupied[x][y]=-1

    # 移動なし
    print(0,flush=True)

    cells=try_place(P)
    if cells is None:
        print('No',flush=True)
    else:
        print('Yes')
        for x,y in cells:
            print(x,y)
            occupied[x][y]=i
        sys.stdout.flush()
        active[i]=(T,cells)
