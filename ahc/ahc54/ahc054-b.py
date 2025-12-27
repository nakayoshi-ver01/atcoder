from collections import deque
n,ti,tj=map(int,input().split())
grid=[list(input()) for _ in range(n)]
unchecked=[[True for _ in range(n)] for _ in range(n)]
unchecked[0][n//2]=False
state=deque()
grid[ti][tj]='G'

# 目的地の周りに木を生やす
for i in range(-1,2):
    for j in range(-1,2):
        if 0<=ti+i<=n-1 and 0<=tj+j<=n-1:
            if grid[ti+i][tj+j]=='.':
                grid[ti+i][tj+j]='N'

# 進行方向に横3マスの壁を一定間隔で生やす
dire=[(1,0),(-1,0),(0,1),(0,-1)]
state.append((0,(n//2),2,0))
while state:
    now=state.popleft()
    if now[2]==2 and now[3]==0 and now[0]<n-1:
        for i in range(max(now[1]-1,0),min(now[1]+2,n)):
            if grid[now[0]+1][i]=='.' and (now[0]+1,i)!=(ti+1,tj):
                grid[now[0]+1][i]='N'
                unchecked[now[0]+1][i]=False
    if now[2]==2 and now[3]==1 and now[0]>0:
        for i in range(max(now[1]-1,0),min(now[1]+2,n)):
            if grid[now[0]-1][i]=='.' and (now[0]-1,i)!=(ti+1,tj):
                grid[now[0]-1][i]='N'
                unchecked[now[0]-1][i]=False
    if now[2]==2 and now[3]==2 and now[1]<n-1:
        for i in range(max(now[0]-1,0),min(now[0]+2,n)):
            if grid[i][now[1]+1]=='.' and (i,now[1]+1)!=(ti+1,tj):
                grid[i][now[1]+1]='N'
                unchecked[i][now[1]+1]=False
    if now[2]==2 and now[3]==3 and now[1]>0:
        for i in range(max(now[0]-1,0),min(now[0]+2,n)):
            if grid[i][now[1]-1]=='.' and (i,now[1]-1)!=(ti+1,tj):
                grid[i][now[1]-1]='N'
                unchecked[i][now[1]-1]=False
    if now[2]!=2:
        if 0<=now[0]+dire[now[3]][0]<=n-1 and 0<=now[1]+dire[now[3]][1]<=n-1 and unchecked[now[0]+dire[now[3]][0]][now[1]+dire[now[3]][1]]:
            state.append((now[0]+dire[now[3]][0],now[1]+dire[now[3]][1],now[2]+1,now[3]))
            unchecked[now[0]+dire[now[3]][0]][now[1]+dire[now[3]][1]]=False
    else:
        if now[3]==0 or now[3]==1:
            if 0<=now[0]+dire[2][0]<=n-1 and 0<=now[1]+dire[2][1]<=n-1 and unchecked[now[0]+dire[2][0]][now[1]+dire[2][1]]:
                state.append((now[0]+dire[2][0],now[1]+dire[2][1],1,2))
                unchecked[now[0]+dire[2][0]][now[1]+dire[2][1]]=False
            if 0<=now[0]+dire[3][0]<=n-1 and 0<=now[1]+dire[3][1]<=n-1 and unchecked[now[0]+dire[3][0]][now[1]+dire[3][1]]:
                state.append((now[0]+dire[3][0],now[1]+dire[3][1],1,3))
                unchecked[now[0]+dire[3][0]][now[1]+dire[3][1]]=False
        else:
            if 0<=now[0]+dire[0][0]<=n-1 and 0<=now[1]+dire[0][1]<=n-1 and unchecked[now[0]+dire[0][0]][now[1]+dire[0][1]]:
                state.append((now[0]+dire[0][0],now[1]+dire[0][1],1,0))
                unchecked[now[0]+dire[0][0]][now[1]+dire[0][1]]=False
            if 0<=now[0]+dire[1][0]<=n-1 and 0<=now[1]+dire[1][1]<=n-1 and unchecked[now[0]+dire[1][0]][now[1]+dire[1][1]]:
                state.append((now[0]+dire[1][0],now[1]+dire[1][1],1,1))
                unchecked[now[0]+dire[1][0]][now[1]+dire[1][1]]=False


# なるべく木を切らずに遠回りするルートで目的地までの道を作る
zobfs=deque()
start=(0,n//2,'',0)
zobfs.append(start)
zounchecked=[[True for _ in range(n)] for _ in range(n)]

# dire=[(1,0),(-1,0),(0,1),(0,-1)]
dc=['D','U','R','L']
root=''
minimum_break=1000000
while zobfs:
    now=zobfs.popleft()
    if grid[now[0]][now[1]]=='G':
        if minimum_break>=now[3]:
            if len(root)<len(now[2]):
                root=now[2]
                minimum_break=now[3]
        else:
            break
    else:
        for i in range(4):
            if 0<=now[0]+dire[i][0]<=n-1 and 0<=now[1]+dire[i][1]<=n-1 and zounchecked[now[0]+dire[i][0]][now[1]+dire[i][1]]:
                if grid[now[0]+dire[i][0]][now[1]+dire[i][1]]=='N':
                    zobfs.append((now[0]+dire[i][0],now[1]+dire[i][1],now[2]+dc[i],now[3]+1))
                    zounchecked[now[0]+dire[i][0]][now[1]+dire[i][1]]=False
                elif grid[now[0]+dire[i][0]][now[1]+dire[i][1]]=='.':
                    zobfs.appendleft((now[0]+dire[i][0],now[1]+dire[i][1],now[2]+dc[i],now[3]))
                    zounchecked[now[0]+dire[i][0]][now[1]+dire[i][1]]=False
                elif grid[now[0]+dire[i][0]][now[1]+dire[i][1]]=='G':
                    zobfs.appendleft((now[0]+dire[i][0],now[1]+dire[i][1],now[2]+dc[i],now[3]))

now=[0,n//2]
for i in root:
    grid[now[0]][now[1]]='.'
    now[0]+=dire[dc.index(i)][0]
    now[1]+=dire[dc.index(i)][1]
                
# マップの中で行けない空きマスを探す
remain=set()
mapping=[['A' for _ in range(n)] for _ in range(n)]
state=deque()
state.append((0,n//2))
while state:
    now=state.popleft()
    mapping[now[0]][now[1]]='-'
    for d in dire:
        if 0<=now[0]+d[0]<=n-1 and 0<=now[1]+d[1]<=n-1 and mapping[now[0]+d[0]][now[1]+d[1]]=='A':
            if grid[now[0]+d[0]][now[1]+d[1]] in {'.','G'}:
                state.append((now[0]+d[0],now[1]+d[1]))

remain=set()
for i in range(n):
    for j in range(n):
        if mapping[i][j]=='A' and grid[i][j]=='.':
            remain.add((i,j))

# なるべく木を切らずに空きマスへ行く道を作る
while remain:
    next_goal=remain.pop()
    zobfs=deque()
    start=(0,n//2,'',0)
    zobfs.append(start)
    zounchecked=[[True for _ in range(n)] for _ in range(n)]
    root=''
    while zobfs:
        now=zobfs.popleft()
        if (now[0],now[1])==next_goal:
            root=now[2]
            break
        else:
            for i in range(4):
                if 0<=now[0]+dire[i][0]<=n-1 and 0<=now[1]+dire[i][1]<=n-1 and zounchecked[now[0]+dire[i][0]][now[1]+dire[i][1]]:
                    if grid[now[0]+dire[i][0]][now[1]+dire[i][1]]=='N':
                        zobfs.append((now[0]+dire[i][0],now[1]+dire[i][1],now[2]+dc[i],now[3]+1))
                        zounchecked[now[0]+dire[i][0]][now[1]+dire[i][1]]=False
                    elif grid[now[0]+dire[i][0]][now[1]+dire[i][1]]=='.':
                        zobfs.appendleft((now[0]+dire[i][0],now[1]+dire[i][1],now[2]+dc[i],now[3]))
                        zounchecked[now[0]+dire[i][0]][now[1]+dire[i][1]]=False
                    elif grid[now[0]+dire[i][0]][now[1]+dire[i][1]]=='G':
                        zobfs.append((now[0]+dire[i][0],now[1]+dire[i][1],now[2]+dc[i],now[3]+1))
    
    now=[0,n//2]
    for i in root:
        if tuple(now) in remain:
            remain.remove(tuple(now))
        if grid[now[0]][now[1]]!='G':
            grid[now[0]][now[1]]='.'
        now[0]+=dire[dc.index(i)][0]
        now[1]+=dire[dc.index(i)][1]


# 目的地の上下左右4方向から帰れる道のりを開く(その時に1マスだけトレントを帰らせてもよいことにする)
for i in range(4):
    if 0<=ti+dire[i][0]<=n-1 and 0<=tj+dire[i][1]<=n-1 and grid[ti+dire[i][0]][tj+dire[i][1]]!='T':
        grid[ti+dire[i][0]][tj+dire[i][1]]='N'

dire_dist=[-1 for _ in range(4)]
dire_root=['' for _ in range(4)]
for i in range(4):
    if 0<=ti+dire[i][0]<=n-1 and 0<=tj+dire[i][1]<=n-1 and grid[ti+dire[i][0]][tj+dire[i][1]]=='N':
        grid[ti+dire[i][0]][tj+dire[i][1]]='.'
        state=deque()
        state.append((ti+dire[i][0],tj+dire[i][1],1,0,''))
        dis_check=[[True for _ in range(n)] for _ in range(n)]
        while state:
            now=state.popleft()
            if now[:2]==(0,n//2):
                if len(dire_root[i])<len(now[4]):
                    dire_root[i]=now[4]
                    dire_dist[i]=len(now[4])
            for j in range(4):
                if (
                    0<=now[0]+dire[j][0]<=n-1 and 
                    0<=now[1]+dire[j][1]<=n-1 and 
                    dis_check[now[0]+dire[j][0]][now[1]+dire[j][1]]
                ):
                    if grid[now[0]+dire[j][0]][now[1]+dire[j][1]]=='.':
                        state.append((now[0]+dire[j][0],now[1]+dire[j][1],now[2]+1,now[3],now[4]+dc[j]))
                        dis_check[now[0]+dire[j][0]][now[1]+dire[j][1]]=False
                    if grid[now[0]+dire[j][0]][now[1]+dire[j][1]]=='N' and now[3]<1 and abs(now[0]+dire[j][0]-ti)>1 and abs(now[1]+dire[j][1]-tj)>1:
                        state.append((now[0]+dire[j][0],now[1]+dire[j][1],now[2]+1,now[3]+1,now[4]+dc[j]))
                        dis_check[now[0]+dire[j][0]][now[1]+dire[j][1]]=False
        grid[ti+dire[i][0]][tj+dire[i][1]]='N'


for i in range(4):
  if 0<=ti+dire[i][0]<=n-1 and 0<=tj+dire[i][1]<=n-1 and grid[ti+dire[i][0]][tj+dire[i][1]]=='.':
    if dire_dist[i]!=-1:
        grid[ti+dire[i][0]][tj+dire[i][1]]='N'

for j in range(4):
    now=[ti+dire[j][0],tj+dire[j][1]]
    for i in dire_root[j]:
        if grid[now[0]][now[1]]!='G':
            grid[now[0]][now[1]]='.'
        now[0]+=dire[dc.index(i)][0]
        now[1]+=dire[dc.index(i)][1]

# あと一歩でバレる場所(check_prob)を列挙する
check_pos=[set() for _ in range(4)]
brocked=[False for i in range(4)]

for i in range(4):
    if not brocked[i]:
        for j in range(4):
            search_x=ti+dire[i][0]+dire[j][0]
            search_y=tj+dire[i][1]+dire[j][1]
            while (
                0<=search_x<=n-1 and
                0<=search_y<=n-1 and
                grid[search_x][search_y]=='.'
            ):
                check_pos[i].add((search_x,search_y))
                search_x+=dire[j][0]
                search_y+=dire[j][1]
    else:
        brocked[i]=True

check_prob=[set() for _ in range(4)]
for i in range(4):
    for j in check_pos[i]:
        for k in dire:
            check_prob[i].add((j[0]+k[0],j[1]+k[1]))

# dire=[(1,0),(-1,0),(0,1),(0,-1)]
# for i in range(4):
#     print(check_pos[i])
#     print(check_prob[i])

# for i in grid:
#     print(i)

trent=list()
for i in range(n):
    for j in range(n):
        if grid[i][j]=='N':
            trent.append(i)
            trent.append(j)

count=0
check_grid=[['-' for _ in range(n)] for _ in range(n)]
while True:
    pi,pj=map(int,input().split())
    len_view,*view=map(int,input().split())
    if (pi,pj)==(ti,tj):
        break
    if count==0:
        print(len(trent)//2,*trent)
        for i in range(len_view):
            check_grid[view[i*2]][view[i*2+1]]='c'
        count+=1
    else:
        for i in range(4):
            if (
                ((pi,pj) in check_prob[i]) and 
                brocked.count(False)>=2 and 
                (not brocked[i])
            ):
                if check_grid[ti+dire[i][0]][tj+dire[i][1]]=='c':
                    continue
                # ここを封鎖してもたどり着けるかどうかを確認(未実装,幅優先)
                grid[ti+dire[i][0]][tj+dire[i][1]]='N'
                reachable_state=deque()
                reachable_state.append((ti,tj))
                unreached_grid=[[True for _ in range(n)] for _ in range(n)]
                unreached_grid[ti][tj]=False
                while reachable_state:
                    now=reachable_state.popleft()
                    if now==(pi,pj):
                        break
                    for d in dire:
                        if 0<=now[0]+d[0]<=n-1 and 0<=now[1]+d[1]<=n-1 and grid[now[0]+d[0]][now[1]+d[1]]=='.':
                            if unreached_grid[now[0]+d[0]][now[1]+d[1]]:
                                unreached_grid[now[0]+d[0]][now[1]+d[1]]=False
                                reachable_state.append((now[0]+d[0],now[1]+d[1]))
                else:
                    grid[ti+dire[i][0]][tj+dire[i][1]]='.'
                    continue

                print(1,ti+dire[i][0],tj+dire[i][1])
                brocked[i]=True
                break
        else:
            print(0)