from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq

# cells: P個の(x,y)。C = 4√P / L（Lは領域外・公園外との境界長）
def compactness(cells):
    s=set(map(tuple,cells))
    p=len(s)
    L=0
    for x,y in s:
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            if (x+dx,y+dy) not in s:
                L+=1
    return 4*(p**0.5)/L

# Pマスの軸平行長方形を、正方形に近い順（C降順）で列挙
def rect_shapes(p):
    shapes=[]
    for h in range(1,p+1):
        if p%h==0:
            w=p//h
            shapes.append([(i,j) for i in range(h) for j in range(w)])
    shapes.sort(key=compactness,reverse=True)
    return shapes

rect_cache={}
def get_rect_shapes(p):
    if p not in rect_cache:
        rect_cache[p]=rect_shapes(p)
    return rect_cache[p]

DIR=((1,0),(-1,0),(0,1),(0,-1))

# 長方形をCの高い順に試し、最初に置けるものを返す
def try_rect(p):
    for shape in get_rect_shapes(p):
        mh=max(x for x,y in shape)
        mw=max(y for x,y in shape)
        for i in range(n-mh):
            for j in range(n-mw):
                ok=True
                cells=[]
                for dx,dy in shape:
                    x,y=i+dx,j+dy
                    if grid[x][y]=='#' or occupied[x][y]>=0:
                        ok=False
                        break
                    cells.append((x,y))
                if ok:
                    return cells
    return None

# 中心から未使用芝生をチェビシェフ優先の4連結でPマス集める
def gather_chebyshev(cx,cy,p):
    if grid[cx][cy]=='#' or occupied[cx][cy]>=0:
        return None
    hq=[(0,0,cx,cy)]  # (cheb, manh, x, y)
    seen=set()
    cells=[]
    while hq and len(cells)<p:
        d,m,x,y=heapq.heappop(hq)
        if (x,y) in seen:
            continue
        seen.add((x,y))
        cells.append((x,y))
        for dx,dy in DIR:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]=='.' and occupied[nx][ny]<0 and (nx,ny) not in seen:
                cd=max(abs(nx-cx),abs(ny-cy))
                md=abs(nx-cx)+abs(ny-cy)
                heapq.heappush(hq,(cd,md,nx,ny))
    if len(cells)<p:
        return None
    return cells

# 複数中心から集め、C最大の領域を返す
# まず外周から√P以内を除外し、候補が無ければ余白なしで再探索
def try_chebyshev(p):
    step=max(1,int(p**0.5))
    margin0=int(p**0.5)

    def search(margin):
        best=None
        best_c=-1.0
        lo=margin
        hi=n-margin
        if lo>=hi:
            return None
        for i in range(lo,hi,step):
            for j in range(lo,hi,step):
                if grid[i][j]=='#' or occupied[i][j]>=0:
                    continue
                cells=gather_chebyshev(i,j,p)
                if cells is None:
                    continue
                c=compactness(cells)
                if c>best_c:
                    best_c=c
                    best=cells
                    if best_c>=0.95:
                        return best
        return best

    best=search(margin0)
    if best is not None:
        return best
    return search(0)

# 長方形優先。細い長方形しか無い／無いときはチェビシェフと比較して良い方
def try_place(p):
    best=None
    best_c=-1.0
    cells=try_rect(p)
    if cells is not None:
        best=cells
        best_c=compactness(cells)
        if best_c>=0.9:
            return best
    cells2=try_chebyshev(p)
    if cells2 is not None:
        c2=compactness(cells2)
        if c2>best_c:
            return cells2
    return best

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
