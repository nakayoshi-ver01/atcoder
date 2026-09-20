from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq

DIR=((1,0),(-1,0),(0,1),(0,-1))

def inward_dirs(sx,sy):
    cands=[
        (max(sx,sy),1,1),
        (max(sx,n-1-sy),1,-1),
        (max(n-1-sx,sy),-1,1),
        (max(n-1-sx,n-1-sy),-1,-1),
    ]
    cands.sort()
    return cands[0][1],cands[0][2]

# 種に隣接する使用中領域の反対方向（無ければ角の内側）
def away_dirs(sx,sy):
    vx=vy=0
    for dx,dy in DIR:
        nx,ny=sx+dx,sy+dy
        if 0<=nx<n and 0<=ny<n and occupied[nx][ny]>=0:
            vx-=dx
            vy-=dy
    if vx==0 and vy==0:
        return inward_dirs(sx,sy)
    ix,iy=inward_dirs(sx,sy)
    sx_dir=0 if vx==0 else (1 if vx>0 else -1)
    sy_dir=0 if vy==0 else (1 if vy>0 else -1)
    if sx_dir==0:
        sx_dir=ix
    if sy_dir==0:
        sy_dir=iy
    return sx_dir,sy_dir

# 反対方向優先＋隣接数優先でコンパクトに伸ばす
def gather(sx,sy,p):
    if grid[sx][sy]=='#' or occupied[sx][sy]>=0:
        return None
    ax,ay=away_dirs(sx,sy)
    region={(sx,sy)}
    cells=[(sx,sy)]
    frontier={}
    hq=[]

    def push(x,y):
        a=frontier[x,y]
        px=0 if (x-sx)*ax>=0 else 1
        py=0 if (y-sy)*ay>=0 else 1
        touch_occ=0
        for dx,dy in DIR:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and occupied[nx][ny]>=0:
                touch_occ=1
                break
        cheb=max(abs(x-sx),abs(y-sy))
        manh=abs(x-sx)+abs(y-sy)
        heapq.heappush(hq,(-a,touch_occ,px+py,cheb,manh,x,y))

    def touch(x,y):
        for dx,dy in DIR:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]=='.' and occupied[nx][ny]<0 and (nx,ny) not in region:
                frontier[nx,ny]=frontier.get((nx,ny),0)+1
                push(nx,ny)

    touch(sx,sy)
    while len(cells)<p:
        best=None
        while hq:
            nega,tocc,pen,cheb,manh,x,y=heapq.heappop(hq)
            if (x,y) not in frontier or (x,y) in region or occupied[x][y]>=0:
                continue
            if frontier[x,y]!=-nega:
                continue
            px=0 if (x-sx)*ax>=0 else 1
            py=0 if (y-sy)*ay>=0 else 1
            touch_occ=0
            for dx,dy in DIR:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and occupied[nx][ny]>=0:
                    touch_occ=1
                    break
            if touch_occ!=tocc or px+py!=pen or max(abs(x-sx),abs(y-sy))!=cheb or abs(x-sx)+abs(y-sy)!=manh:
                push(x,y)
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

# 左上 (0,0) へのチェビシェフが小さい順に、5マス間隔の格子を種にする
def try_place(p):
    seeds=[]
    for i in range(0,n,5):
        for j in range(0,n,5):
            if grid[i][j]=='.' and occupied[i][j]<0:
                seeds.append((max(i,j),i,j))
    seeds.sort()
    for _,sx,sy in seeds:
        cells=gather(sx,sy,p)
        if cells is not None:
            return cells
    return None

# 移動を逐次適用しても重ならない順序。無理なら None
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

# 退去グループより後に設置され、かつ人数が小さいグループを左上へ詰め直す
# 移動時は退去グループの設置IDを優先して振り、余りは新規ID
def repack_smaller_later(dep_infos):
    global install_seq
    # dep_infos: [(install_id, size), ...]
    if not dep_infos:
        return []
    move_ids=set()
    for gid,(t,cells,iid) in active.items():
        sz=len(cells)
        for di,ds in dep_infos:
            if iid>di and sz<ds:
                move_ids.add(gid)
                break
    if not move_ids:
        return []

    freed_ids=sorted(di for di,_ in dep_infos)
    # 設置が早い順に戻す → 左上から埋まり、右下が空きやすい
    relocate=sorted(move_ids,key=lambda g:active[g][2])
    old_pos={}
    for gid in relocate:
        t,cells,iid=active[gid]
        old_pos[gid]=(t,cells,iid)
        for x,y in cells:
            occupied[x][y]=-1

    placed=[]
    ok=True
    for gid in relocate:
        t,old_cells,iid=old_pos[gid]
        cells=try_place(len(old_cells))
        if cells is None:
            ok=False
            break
        for x,y in cells:
            occupied[x][y]=gid
        placed.append((gid,t,old_cells,iid,cells))

    if not ok:
        for gid,t,old_cells,iid,cells in placed:
            for x,y in cells:
                occupied[x][y]=-1
        for gid,(t,old_cells,iid) in old_pos.items():
            for x,y in old_cells:
                occupied[x][y]=gid
            active[gid]=(t,old_cells,iid)
        return []

    movers=[]
    fi=0
    for gid,t,old_cells,old_iid,cells in placed:
        if set(cells)!=set(old_cells):
            if fi<len(freed_ids):
                new_iid=freed_ids[fi]
                fi+=1
            else:
                new_iid=install_seq
                install_seq+=1
            active[gid]=(t,cells,new_iid)
            movers.append((gid,set(old_cells),set(cells)))
        else:
            active[gid]=(t,cells,old_iid)
    if active:
        mx=max(iid for _t,_c,iid in active.values())
        install_seq=max(install_seq,mx+1)
    return movers

# n=int(input())
n,m,r=input().split()
n,m,r=int(n),int(m),float(r)
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(n)]

occupied=[[-1]*n for _ in range(n)]
active={}  # gid -> (T, cells, install_id)
install_seq=0

for _ in range(m):
    i,S,T,P,V=map(int,input().split())

    dep_infos=[]
    departing=[gid for gid,(t,_,_) in active.items() if t<S]
    for gid in departing:
        _,cells,iid=active.pop(gid)
        dep_infos.append((iid,len(cells)))
        for x,y in cells:
            occupied[x][y]=-1

    pre_move={gid:(t,list(cells),iid) for gid,(t,cells,iid) in active.items()}
    raw_movers=repack_smaller_later(dep_infos)

    moves=[]
    if raw_movers:
        moving={gid for gid,_,_ in raw_movers}
        static=set()
        for gid,(t,cells,iid) in pre_move.items():
            if gid not in moving:
                static.update(cells)
        seq=order_moves(raw_movers,static)
        if seq is None:
            # 逐次不能なら詰め直しを取消
            for gid,old_s,new_s in raw_movers:
                t,_,iid=pre_move[gid]
                for x,y in new_s:
                    if occupied[x][y]==gid:
                        occupied[x][y]=-1
                for x,y in old_s:
                    occupied[x][y]=gid
                active[gid]=(t,list(old_s),iid)
            moves=[]
        else:
            moves=[(gid,list(ns)) for gid,ns in seq]

    print(len(moves),flush=True)
    for j,new_cells in moves:
        print(j)
        for x,y in new_cells:
            print(x,y)
        sys.stdout.flush()

    cells=try_place(P)
    if cells is None:
        print('No',flush=True)
    else:
        print('Yes')
        for x,y in cells:
            print(x,y)
            occupied[x][y]=i
        sys.stdout.flush()
        active[i]=(T,cells,install_seq)
        install_seq+=1
