from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq

DIR=((1,0),(-1,0),(0,1),(0,-1))
PARCEL_MAX=150

# 隣接優先＋開始点チェビシェフ。同距離は軸寄り（manh小）
def gather_compact(p,allowed,sx,sy):
    if p<=0 or (sx,sy) not in allowed or occupied[sx][sy]>=0:
        return None
    region={(sx,sy)}
    cells=[(sx,sy)]
    frontier={}
    hq=[]

    def push(x,y):
        a=frontier[x,y]
        cheb=max(abs(x-sx),abs(y-sy))
        manh=abs(x-sx)+abs(y-sy)
        heapq.heappush(hq,(-a,cheb,manh,x,y))

    def touch(x,y):
        for dx,dy in DIR:
            nx,ny=x+dx,y+dy
            if (nx,ny) in allowed and (nx,ny) not in region and occupied[nx][ny]<0:
                frontier[nx,ny]=frontier.get((nx,ny),0)+1
                push(nx,ny)

    touch(sx,sy)
    while len(cells)<p:
        best=None
        while hq:
            nega,cheb,manh,x,y=heapq.heappop(hq)
            if (x,y) not in frontier or (x,y) in region or occupied[x][y]>=0:
                continue
            if frontier[x,y]!=-nega:
                continue
            if max(abs(x-sx),abs(y-sy))!=cheb or abs(x-sx)+abs(y-sy)!=manh:
                continue
            best=(x,y)
            break
        if best is None:
            return None
        x,y=best
        del frontier[x,y]
        region.add((x,y))
        cells.append((x,y))
        touch(x,y)
    return cells

def gather_by_order(p,order):
    if len(order)<p:
        return None
    allowed={(x,y) for x,y in order if occupied[x][y]<0}
    if len(allowed)<p:
        return None
    sx,sy=min(allowed)
    return gather_compact(p,allowed,sx,sy)

# 長方形内の未割当空き芝生マス数
def grass_count_in_rect(r0,r1,c0,c1,covered):
    cnt=0
    for i in range(r0,r1+1):
        for j in range(c0,c1+1):
            if not covered[i][j] and grid[i][j]=='.' and occupied[i][j]<0:
                cnt+=1
    return cnt

def grass_on_row(i,c0,c1,covered):
    cnt=0
    for j in range(c0,c1+1):
        if not covered[i][j] and grid[i][j]=='.' and occupied[i][j]<0:
            cnt+=1
    return cnt

def grass_on_col(j,r0,r1,covered):
    cnt=0
    for i in range(r0,r1+1):
        if not covered[i][j] and grid[i][j]=='.' and occupied[i][j]<0:
            cnt+=1
    return cnt

# 左上から、空き芝生が150を超えない範囲で下または右へ伸ばす
def grow_rectangle(sr,sc,covered):
    r0=r1=sr
    c0=c1=sc
    cur=grass_count_in_rect(r0,r1,c0,c1,covered)
    while True:
        best=None  # (new_cnt, aspect_pen, 'd'|'r')
        if r1+1<n:
            nxt=cur+grass_on_row(r1+1,c0,c1,covered)
            if nxt<=PARCEL_MAX and nxt>cur:
                best=(nxt,abs((r1+1-r0+1)-(c1-c0+1)),'d')
        if c1+1<n:
            nxt=cur+grass_on_col(c1+1,r0,r1,covered)
            if nxt<=PARCEL_MAX and nxt>cur:
                cand=(nxt,abs((r1-r0+1)-(c1+1-c0+1)),'r')
                if best is None or cand[0]>best[0] or (cand[0]==best[0] and cand[1]<best[1]):
                    best=cand
        if best is None:
            break
        cur=best[0]
        if best[2]=='d':
            r1+=1
        else:
            c1+=1
    return r0,r1,c0,c1

# 長方形内の空き連結成分を区画リストに（万一150超なら横帯で再分割）
def orders_in_rect(r0,r1,c0,c1,allow=None):
    seen=[[False]*n for _ in range(n)]
    orders=[]
    for i in range(r0,r1+1):
        for j in range(c0,c1+1):
            if allow is not None and (i,j) not in allow:
                continue
            if grid[i][j]!='.' or occupied[i][j]>=0 or seen[i][j]:
                continue
            q=deque([(i,j)])
            seen[i][j]=True
            cc=[]
            while q:
                x,y=q.popleft()
                cc.append((x,y))
                for dx,dy in DIR:
                    nx,ny=x+dx,y+dy
                    if r0<=nx<=r1 and c0<=ny<=c1 and not seen[nx][ny]:
                        if allow is not None and (nx,ny) not in allow:
                            continue
                        if grid[nx][ny]=='.' and occupied[nx][ny]<0:
                            seen[nx][ny]=True
                            q.append((nx,ny))
            if len(cc)>PARCEL_MAX:
                orders.extend(split_cc_strips(cc))
            else:
                orders.append(cc)
    return orders

def split_cc_strips(cc_cells):
    remaining=set(cc_cells)
    out=[]
    h0=max(1,int(PARCEL_MAX**0.5))
    while remaining:
        sx,sy=min(remaining)
        chunk=[]
        for h in (h0,h0*2,n):
            q=deque([(sx,sy)])
            seen={(sx,sy)}
            chunk=[]
            while q and len(chunk)<PARCEL_MAX:
                x,y=q.popleft()
                chunk.append((x,y))
                for dx,dy in DIR:
                    nxt=(x+dx,y+dy)
                    if nxt in remaining and nxt not in seen:
                        nx,ny=nxt
                        if sx<=nx<sx+h:
                            seen.add(nxt)
                            q.append(nxt)
            if chunk:
                break
        if not chunk:
            chunk=[(sx,sy)]
        out.append(chunk)
        for c in chunk:
            remaining.discard(c)
    return out

# 長方形成長で公園（または指定マス）を区切る
def partition_by_rectangles(seed_cells=None):
    covered=[[False]*n for _ in range(n)]
    allow=None
    if seed_cells is not None:
        allow=set(seed_cells)
        for i in range(n):
            for j in range(n):
                if (i,j) not in allow:
                    covered[i][j]=True
    zones=[]
    for i in range(n):
        for j in range(n):
            if covered[i][j]:
                continue
            if grid[i][j]!='.' or occupied[i][j]>=0:
                covered[i][j]=True
                continue
            r0,r1,c0,c1=grow_rectangle(i,j,covered)
            for x in range(r0,r1+1):
                for y in range(c0,c1+1):
                    covered[x][y]=True
            orders=orders_in_rect(r0,r1,c0,c1,allow)
            if orders:
                zones.append(orders)
    return zones

def rebuild_zones():
    return partition_by_rectangles(None)

def rebuild_region_orders(region_cells):
    free=[]
    for x,y in region_cells:
        if grid[x][y]=='.' and occupied[x][y]<0:
            free.append((x,y))
    if not free:
        return []
    zs=partition_by_rectangles(free)
    out=[]
    for orders in zs:
        out.extend(orders)
    return out

def split_cc_from_ends(cc_cells):
    # try_place 失敗時の張り直し用
    return rebuild_region_orders(cc_cells)

# 全域 best-fit。戻り値 (cells, zone_idx)
def try_place(p):
    cands=[]
    for zid,orders in enumerate(zones):
        for oi,order in enumerate(orders):
            rem=len(order)
            if rem>=p:
                cands.append((rem-p,rem,zid,oi))
    cands.sort()
    for waste,rem,zid,oi in cands:
        order=zones[zid][oi]
        if len(order)<p:
            continue
        cells=gather_by_order(p,order)
        if cells is None:
            zones[zid][oi:oi+1]=split_cc_from_ends(order)
            continue
        used=set(cells)
        zones[zid][oi]=[c for c in order if c not in used]
        return cells,zid
    return None,None

def try_place_in_orders(p,orders):
    cands=[]
    for oi,order in enumerate(orders):
        rem=len(order)
        if rem>=p:
            cands.append((rem-p,rem,oi))
    cands.sort()
    for waste,rem,oi in cands:
        order=orders[oi]
        if len(order)<p:
            continue
        cells=gather_by_order(p,order)
        if cells is None:
            orders[oi:oi+1]=split_cc_from_ends(order)
            continue
        used=set(cells)
        orders[oi]=[c for c in order if c not in used]
        return cells
    return None

def order_moves(movers,static_cells):
    pending=list(movers)
    seq=[]
    while pending:
        progressed=False
        for i,(gid,old_s,new_s) in enumerate(pending):
            blocked=set(static_cells)
            for gid2,old2,_ in pending:
                if gid2!=gid:
                    blocked|=old2
            if new_s.isdisjoint(blocked):
                seq.append((gid,new_s))
                pending.pop(i)
                progressed=True
                break
        if not progressed:
            return None
    return seq

def repack_same_zone(zid,freed_cells):
    if not (0<=zid<len(zones)):
        return []

    relocate=[gid for gid,(t,cells,z) in active.items() if z==zid]
    free_only=set()
    for order in zones[zid]:
        free_only.update(order)
    free_only.update(freed_cells)

    if not relocate:
        zones[zid]=rebuild_region_orders(free_only)
        return []

    relocate.sort(key=lambda gid:len(active[gid][1]),reverse=True)
    old_pos={}
    for gid in relocate:
        t,cells,z=active[gid]
        old_pos[gid]=(t,cells)
        for x,y in cells:
            occupied[x][y]=-1

    orders=rebuild_region_orders(free_only)
    placed=[]
    ok=True
    for gid in relocate:
        t,old_cells=old_pos[gid]
        p=len(old_cells)
        cells=try_place_in_orders(p,orders)
        if cells is None:
            ok=False
            break
        for x,y in cells:
            occupied[x][y]=gid
        placed.append((gid,t,old_cells,cells))

    if not ok:
        for gid,t,old_cells,cells in placed:
            for x,y in cells:
                occupied[x][y]=-1
        for gid,(t,old_cells) in old_pos.items():
            for x,y in old_cells:
                occupied[x][y]=gid
            active[gid]=(t,old_cells,zid)
        region=set(free_only)
        for gid,(t,old_cells) in old_pos.items():
            region.update(old_cells)
        zones[zid]=rebuild_region_orders(region)
        return []

    moves=[]
    for gid,t,old_cells,cells in placed:
        active[gid]=(t,cells,zid)
        if set(cells)!=set(old_cells):
            moves.append((gid,cells))
    reg=set(free_only)
    for gid,t,old_cells,cells in placed:
        reg|=set(old_cells)
        reg-=set(cells)
    zones[zid]=rebuild_region_orders(reg)
    return moves

# n=int(input())
n,m,r=input().split()
n,m,r=int(n),int(m),float(r)
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(n)]

occupied=[[-1]*n for _ in range(n)]
active={}
zones=rebuild_zones()

for _ in range(m):
    i,S,T,P,V=map(int,input().split())

    freed_by_zid=defaultdict(list)
    departing=[gid for gid,(t,_,_) in active.items() if t<S]
    for gid in departing:
        _,cells,zid=active.pop(gid)
        freed_by_zid[zid].extend(cells)
        for x,y in cells:
            occupied[x][y]=-1

    pre_move={gid:(t,list(cells),z) for gid,(t,cells,z) in active.items()}

    moves=[]
    for zid,fcells in freed_by_zid.items():
        moves.extend(repack_same_zone(zid,fcells))

    if moves:
        movers=[]
        moving=set()
        for gid,new_cells in moves:
            if gid not in pre_move:
                continue
            old=pre_move[gid][1]
            if set(old)!=set(new_cells):
                movers.append((gid,set(old),set(new_cells)))
                moving.add(gid)
        static=set()
        for gid,(t,cells,z) in pre_move.items():
            if gid not in moving:
                static.update(cells)
        seq=order_moves(movers,static)
        if seq is None:
            for gid,new_cells in moves:
                if gid not in pre_move:
                    continue
                t,old,z=pre_move[gid]
                for x,y in new_cells:
                    if occupied[x][y]==gid:
                        occupied[x][y]=-1
                for x,y in old:
                    occupied[x][y]=gid
                active[gid]=(t,old,z)
            moves=[]
            zones=rebuild_zones()
            for gid,(t,gcells,_) in list(active.items()):
                active[gid]=(t,gcells,-1)
        else:
            moves=[(gid,list(ns)) for gid,ns in seq]

    if freed_by_zid:
        covered=set()
        for orders in zones:
            for order in orders:
                covered.update(order)
        for gid,(t,cells,z) in active.items():
            covered.update(cells)
        extra=[]
        for ii in range(n):
            for jj in range(n):
                if grid[ii][jj]!='.' or occupied[ii][jj]>=0 or (ii,jj) in covered:
                    continue
                extra.append((ii,jj))
        if extra:
            for orders in partition_by_rectangles(extra):
                zones.append(orders)

    print(len(moves),flush=True)
    for j,new_cells in moves:
        print(j)
        for x,y in new_cells:
            print(x,y)
        sys.stdout.flush()

    cells,zid=try_place(P)
    if cells is None:
        zones=rebuild_zones()
        for gid,(t,gcells,_) in list(active.items()):
            active[gid]=(t,gcells,-1)
        cells,zid=try_place(P)

    if cells is None:
        print('No',flush=True)
    else:
        print('Yes')
        for x,y in cells:
            print(x,y)
            occupied[x][y]=i
        sys.stdout.flush()
        active[i]=(T,cells,zid)
