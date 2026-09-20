from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq

DIR=((1,0),(-1,0),(0,1),(0,-1))

# 最寄りの公園角へのチェビシェフ距離
def cheb_to_corner(x,y):
    return min(
        max(x,y),
        max(x,n-1-y),
        max(n-1-x,y),
        max(n-1-x,n-1-y),
    )

def inward_dirs(sx,sy):
    cands=[
        (max(sx,sy),1,1),
        (max(sx,n-1-sy),1,-1),
        (max(n-1-sx,sy),-1,1),
        (max(n-1-sx,n-1-sy),-1,-1),
    ]
    cands.sort()
    return cands[0][1],cands[0][2]

# yが [j0,j1] に収まるマスだけで成長（j0 is None なら制限なし）
def gather(sx,sy,p,j0=None,j1=None):
    if grid[sx][sy]=='#' or occupied[sx][sy]>=0:
        return None
    if j0 is not None and not (j0<=sy<=j1):
        return None
    sx_dir,sy_dir=inward_dirs(sx,sy)

    def ok(x,y):
        if not (0<=x<n and 0<=y<n):
            return False
        if j0 is not None and not (j0<=y<=j1):
            return False
        return grid[x][y]=='.' and occupied[x][y]<0

    def pen(x,y):
        px=0 if (x-sx)*sx_dir>=0 else 1
        py=0 if (y-sy)*sy_dir>=0 else 1
        return px+py

    region={(sx,sy)}
    cells=[(sx,sy)]
    adj={}
    hq=[]

    def touch(x,y):
        for dx,dy in DIR:
            nx,ny=x+dx,y+dy
            if ok(nx,ny) and (nx,ny) not in region:
                a=adj.get((nx,ny),0)+1
                adj[nx,ny]=a
                heapq.heappush(hq,(-a,pen(nx,ny),max(abs(nx-sx),abs(ny-sy)),abs(nx-sx)+abs(ny-sy),nx,ny))

    touch(sx,sy)
    while len(cells)<p:
        best=None
        while hq:
            nega,pe,cd,md,x,y=heapq.heappop(hq)
            if (x,y) in region:
                continue
            if adj.get((x,y),0)!=-nega:
                continue
            best=(x,y)
            break
        if best is None:
            return None
        x,y=best
        del adj[x,y]
        region.add((x,y))
        cells.append((x,y))
        touch(x,y)
    return cells

# 芝がなるべく均等になるよう列をK本の連続帯に分割 → [(j0,j1), ...]
def make_strips(k=5):
    col_g=[0]*n
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='.':
                col_g[j]+=1
    pref=[0]
    for g in col_g:
        pref.append(pref[-1]+g)
    total=pref[-1]
    cuts=[0]
    for t in range(1,k):
        goal=total*t//k
        # pref[j] >= goal となる最小 j（jは列数＝右端+1）
        j=cuts[-1]+1
        while j<n and pref[j]<goal:
            j+=1
        if j<=cuts[-1]:
            j=cuts[-1]+1
        if j>=n:
            j=n-1
        cuts.append(j)
    cuts.append(n)
    strips=[]
    for a,b in zip(cuts,cuts[1:]):
        if a>=b:
            b=min(n,a+1)
        strips.append((a,b-1))
    return strips

def strip_free(j0,j1):
    cnt=0
    for i in range(n):
        for j in range(j0,j1+1):
            if grid[i][j]=='.' and occupied[i][j]<0:
                cnt+=1
    return cnt

# 帯内の種: 左上（左端列）から下へ 3 マスごと
SEED_STEP=3
def strip_seeds(j0,j1):
    seeds=[]
    for i in range(0,n,SEED_STEP):
        if grid[i][j0]=='.' and occupied[i][j0]<0:
            seeds.append((i,j0))
    return seeds

def try_place_in_strip(p,j0,j1):
    for sx,sy in strip_seeds(j0,j1):
        cells=gather(sx,sy,p,j0,j1)
        if cells is not None:
            return cells
    return None

# 空きの多い帯から帯内配置 → だめなら同じ種から帯制限なしで再試行
def try_place(p):
    order=sorted(range(len(strips)),key=lambda k:-strip_free(*strips[k]))
    # 1st: 帯内のみ
    for k in order:
        j0,j1=strips[k]
        if strip_free(j0,j1)<p:
            continue
        cells=try_place_in_strip(p,j0,j1)
        if cells is not None:
            return cells
    # 2nd: 各帯の種からスタートし、広げは横断OK
    for k in order:
        j0,j1=strips[k]
        for sx,sy in strip_seeds(j0,j1):
            cells=gather(sx,sy,p,None,None)
            if cells is not None:
                return cells
    return None

# n=int(input())
n,m,r=input().split()
n,m,r=int(n),int(m),float(r)
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(n)]

strips=make_strips(5)

occupied=[[-1]*n for _ in range(n)]
active={}  # gid -> (T, cells)

for _ in range(m):
    i,S,T,P,V=map(int,input().split())
    for gid in [gid for gid,(t,_) in active.items() if t<S]:
        _,cells=active.pop(gid)
        for x,y in cells:
            occupied[x][y]=-1

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
