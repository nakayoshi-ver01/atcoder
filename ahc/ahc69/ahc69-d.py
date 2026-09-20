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

# 現領域への隣接数が多いフロンティアを優先して成長（ヒープ＋遅延削除）
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
    adj={}  # (x,y) -> 現領域との隣接数
    hq=[]   # (-adj, pen, cheb, manh, x, y)

    def touch(x,y):
        for dx,dy in DIR:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]=='.' and occupied[nx][ny]<0 and (nx,ny) not in region:
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
                continue  # 古いエントリ
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

    seeds.sort(key=lambda ij:cheb_to_corner(ij[0],ij[1]))
    return seeds

# 空きのある周上の角寄り種 → ダメなら10マス内側の周、…
def try_place(p):
    for d in range(0,(n+1)//2,10):
        for sx,sy in ring_seeds(d):
            cells=gather(sx,sy,p)
            if cells is not None:
                return cells
    return None

# 重心近傍の種から再配置（移動用）
def try_place_near(p,cx,cy,rad):
    seeds=[]
    for i in range(max(0,cx-rad),min(n,cx+rad+1)):
        for j in range(max(0,cy-rad),min(n,cy+rad+1)):
            if grid[i][j]=='.' and occupied[i][j]<0:
                seeds.append((abs(i-cx)+abs(j-cy),cheb_to_corner(i,j),i,j))
    seeds.sort()
    for _,__,sx,sy in seeds[:3]:
        cells=gather(sx,sy,p)
        if cells is not None:
            return cells
    return None

# 配置失敗時のみ: グループを空けて新規を置き、どかした側は重心近傍で再配置
TOUCH_TH=4
def try_rescue(i,P):
    if not active:
        return None,[]
    cands=[]
    for j,(t,cells,v,pj) in active.items():
        touch=0
        for x,y in cells:
            for dx,dy in DIR:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]=='.' and occupied[nx][ny]<0:
                    touch+=1
        if touch>=TOUCH_TH:
            cands.append((v,-touch,pj,j))  # 低V優先、同程度なら接辺が多い方
    cands.sort()

    for _,__,pj,j in cands[:4]:
        t,old_cells,v,_=active[j]
        for x,y in old_cells:
            occupied[x][y]=-1
        incoming=try_place(P)
        if incoming is None:
            for x,y in old_cells:
                occupied[x][y]=j
            continue
        for x,y in incoming:
            occupied[x][y]=i
        cx=sum(x for x,y in old_cells)//pj
        cy=sum(y for x,y in old_cells)//pj
        rad=max(int(pj**0.5)*2,5)
        new_j=try_place_near(pj,cx,cy,rad)
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

def free_count():
    cnt=0
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='.' and occupied[i][j]<0:
                cnt+=1
    return cnt

# これまでのVの分位点以上か（序盤は常にTrue）
def v_high_enough(v,q):
    if len(v_hist)<30:
        return True
    s=sorted(v_hist)
    return v>=s[int((len(s)-1)*q)]

# n=int(input())
n,m,r=input().split()
n,m,r=int(n),int(m),float(r)
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(n)]

occupied=[[-1]*n for _ in range(n)]
active={}  # gid -> (T, cells, V, P)
v_hist=[]

for _ in range(m):
    i,S,T,P,V=map(int,input().split())
    v_hist.append(V)
    # 退去済みを解放
    for gid in [gid for gid,(t,_,_,_) in active.items() if t<S]:
        _,cells,_,_=active.pop(gid)
        for x,y in cells:
            occupied[x][y]=-1

    fc=free_count()
    cells=None
    moves=[]
    # 事前判定: 空きが 2P 未満なら try_place を省略
    if fc>=2*P:
        cells=try_place(P)
        if cells is not None:
            # 低Vかつ空きが少ないなら断って将来の高V用に残す
            if not v_high_enough(V,0.35) and fc<max(300,P*8):
                cells=None

    if cells is None:
        # 高Vだけ救済
        if v_high_enough(V,0.5):
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
