from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq

DIR=((1,0),(-1,0),(0,1),(0,-1))

# cells: P個の(x,y)。C = 4√P / L（Lは領域外・公園外との境界長）
def compactness(cells):
    s=set(map(tuple,cells))
    p=len(s)
    L=0
    for x,y in s:
        for dx,dy in DIR:
            if (x+dx,y+dy) not in s:
                L+=1
    return 4*(p**0.5)/L

# ⌊√P⌋×⌊√P⌋ と、縦半分横2倍・その逆を各1回
def rect_sizes(p):
    s=max(1,int(p**0.5))
    sizes=[]
    seen=set()
    for h,w in ((s,s),(s//2,s*2),(s*2,s//2)):
        if h>=1 and w>=1 and h<=n and w<=n and h*w<=p and (h,w) not in seen:
            seen.add((h,w))
            sizes.append((h,w))
    return sizes

# 空きマス二次元累積和（. かつ未使用 = 1）
pref=None
def build_pref():
    global pref
    pref=[[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        row=pref[i+1]
        prow=pref[i]
        gi=grid[i]
        oi=occupied[i]
        for j in range(n):
            v=1 if gi[j]=='.' and oi[j]<0 else 0
            row[j+1]=row[j]+prow[j+1]-prow[j]+v

def rect_ok(i,j,h,w):
    i2,j2=i+h,j+w
    s=pref[i2][j2]-pref[i][j2]-pref[i2][j]+pref[i][j]
    return s==h*w

def make_rect(i,j,h,w):
    return [(x,y) for x in range(i,i+h) for y in range(j,j+w)]

# 長方形を核にして、足りない分を周囲BFSで足す
def expand_bfs(base,need):
    if need==0:
        return list(base)
    q=deque()
    seen=set(base)
    for x,y in base:
        for dx,dy in DIR:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and (nx,ny) not in seen:
                if grid[nx][ny]=='.' and occupied[nx][ny]<0:
                    seen.add((nx,ny))
                    q.append((nx,ny))
    extra=[]
    while q and len(extra)<need:
        x,y=q.popleft()
        extra.append((x,y))
        for dx,dy in DIR:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and (nx,ny) not in seen:
                if grid[nx][ny]=='.' and occupied[nx][ny]<0:
                    seen.add((nx,ny))
                    q.append((nx,ny))
    if len(extra)<need:
        return None
    return list(base)+extra

# 大きな長方形＋余りBFS。全域探索
def try_place(p):
    build_pref()
    for h,w in rect_sizes(p):
        need=p-h*w
        for i in range(n-h+1):
            for j in range(n-w+1):
                if not rect_ok(i,j,h,w):
                    continue
                cells=expand_bfs(make_rect(i,j,h,w),need)
                if cells is not None:
                    return cells
    return None

# 同上・(cx,cy)近傍のみ
def try_place_near(p,cx,cy,rad):
    build_pref()
    for h,w in rect_sizes(p):
        need=p-h*w
        i0=max(0,cx-rad)
        i1=min(n-h,cx+rad)
        j0=max(0,cy-rad)
        j1=min(n-w,cy+rad)
        if i0>i1 or j0>j1:
            continue
        for i in range(i0,i1+1):
            for j in range(j0,j1+1):
                if not rect_ok(i,j,h,w):
                    continue
                cells=expand_bfs(make_rect(i,j,h,w),need)
                if cells is not None:
                    return cells
    return None

# 救済: どかした場所の近傍だけに新規・移動先を探す（なるべく動かさない）
def try_rescue(i,P):
    cands=sorted(active.items(),key=lambda kv:(len(kv[1][1]),kv[1][2]))
    for j,(t,old_cells,v,pj) in cands[:5]:
        for x,y in old_cells:
            occupied[x][y]=-1
        cx=sum(x for x,y in old_cells)//pj
        cy=sum(y for x,y in old_cells)//pj
        rad_in=max(int(P**0.5)*2,3)
        incoming=try_place_near(P,cx,cy,rad_in)
        if incoming is None:
            for x,y in old_cells:
                occupied[x][y]=j
            continue
        for x,y in incoming:
            occupied[x][y]=i
        rad_j=max(int(pj**0.5)*2,3)
        new_j=try_place_near(pj,cx,cy,rad_j)
        if new_j is None:
            for x,y in incoming:
                occupied[x][y]=-1
            for x,y in old_cells:
                occupied[x][y]=j
            continue
        for x,y in new_j:
            occupied[x][y]=j
        active[j]=(t,new_j,v,pj)
        return incoming,[(j,new_j)]
    return None,[]

# n=int(input())
n,m,r=input().split()
n,m,r=int(n),int(m),float(r)
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(n)]

occupied=[[-1]*n for _ in range(n)]
active={}  # gid -> (T, cells, V, P)

for _ in range(m):
    i,S,T,P,V=map(int,input().split())
    # 退去済みを解放
    for gid in [gid for gid,(t,_,_,_) in active.items() if t<S]:
        _,cells,_,_=active.pop(gid)
        for x,y in cells:
            occupied[x][y]=-1

    cells=try_place(P)
    moves=[]
    if cells is None:
        cells,moves=try_rescue(i,P)

    print(len(moves),flush=True)
    for j,new_cells in moves:
        print(j)
        for x,y in new_cells:
            print(x,y)
        sys.stdout.flush()

    if cells is None:
        print('No',flush=True)
    else:
        print('Yes')
        for x,y in cells:
            print(x,y)
            occupied[x][y]=i
        sys.stdout.flush()
        active[i]=(T,cells,V,P)
