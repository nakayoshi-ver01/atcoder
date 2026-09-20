from collections import deque

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
v_wall=[list(map(int,input())) for _ in range(n)]
h_wall=[list(map(int,input())) for _ in range(n-1)]

v_wall_check=[[0] for _ in range(n+1)]
h_wall_check=[[0] for _ in range(n)]
v_wall_check[0]=[0 for _ in range(n)]
h_wall_check[0]=[0 for _ in range(n+1)]

for i in range(n):
    for j in range(n-1):
        v_wall_check[i+1].append(v_wall[i][j]+v_wall_check[i+1][-1])

for i in range(1,n+1):
    for j in range(n):
        v_wall_check[i][j]+=v_wall_check[i-1][j]

for i in range(n-1):
    for j in range(n):
        h_wall_check[i+1].append(h_wall[i][j]+h_wall_check[i+1][-1])

for i in range(1,n):
    for j in range(n+1):
        h_wall_check[i][j]+=h_wall_check[i-1][j]


def apply_hand(hand):
    direction,r,c,h,w=hand
    if direction=='V':
        half=h//2
        for i in range(half):
            for j in range(w):
                a[r+i][c+j],a[r+half+i][c+j]=(
                    a[r+half+i][c+j],a[r+i][c+j]
                )
    else:
        half=w//2
        for i in range(h):
            for j in range(half):
                a[r+i][c+j],a[r+i][c+half+j]=(
                    a[r+i][c+half+j],a[r+i][c+j]
                )


def wall_check(r,c,h,w):
    return (
        v_wall_check[r+h][c+w-1]
        -v_wall_check[r][c+w-1]
        -v_wall_check[r+h][c]
        +v_wall_check[r][c]==0
        and
        h_wall_check[r+h-1][c+w]
        -h_wall_check[r+h-1][c]
        -h_wall_check[r][c+w]
        +h_wall_check[r][c]==0
    )


cand=[]
for r in range(n):
    for c in range(n):
        # 縦操作は幅1、横操作は高さ1だけを候補にする。
        for h in range(2,n-r+1,2):
            if wall_check(r,c,h,1):
                cand.append(('V',r,c,h,1))
        for w in range(2,n-c+1,2):
            if wall_check(r,c,1,w):
                cand.append(('H',r,c,1,w))

moves_from_corner=[[[] for _ in range(n)] for _ in range(n)]

for hand in cand:
    _,r,c,h,w=hand
    hand_mask=0
    row_mask=(1<<w)-1
    for i in range(r,r+h):
        hand_mask|=row_mask<<(i*n+c)
    entry=(hand,hand_mask)
    corners={(r,c),(r+h-1,c),(r,c+w-1),(r+h-1,c+w-1)}
    for i,j in corners:
        moves_from_corner[i][j].append(entry)


def moved_position(i,j,hand):
    direction,r,c,h,w=hand
    if direction=='V':
        half=h//2
        if i<r+half:
            return i+half,j
        return i-half,j

    half=w//2
    if j<c+half:
        return i,j+half
    return i,j-half


def bfs(start,goal,removed_mask):
    que=deque([start])
    prev={start:None}
    prev_hand={}

    while que:
        now=que.popleft()
        if now==goal:
            break

        i,j=now
        valid_moves=[]
        for hand,hand_mask in moves_from_corner[i][j]:
            if hand_mask&removed_mask:
                continue

            valid_moves.append((hand,hand_mask))
            nxt=moved_position(i,j,hand)
            if nxt in prev:
                continue
            prev[nxt]=now
            prev_hand[nxt]=hand
            que.append(nxt)

        # 一度無効になった候補は、以降のBFSでも無効なので削除する。
        moves_from_corner[i][j]=valid_moves

    if goal not in prev:
        return None

    path=[]
    now=goal
    while now!=start:
        path.append(prev_hand[now])
        now=prev[now]
    path.reverse()
    return path


def neighbors(i,j):
    if i>0 and h_wall[i-1][j]==0:
        yield i-1,j
    if i+1<n and h_wall[i][j]==0:
        yield i+1,j
    if j>0 and v_wall[i][j-1]==0:
        yield i,j-1
    if j+1<n and v_wall[i][j]==0:
        yield i,j+1


def articulation_points():
    order=[[-1]*n for _ in range(n)]
    low=[[0]*n for _ in range(n)]
    timer=0
    result=set()

    def dfs(i,j,parent):
        nonlocal timer
        order[i][j]=low[i][j]=timer
        timer+=1
        children=0

        for next_i,next_j in neighbors(i,j):
            if not active[next_i][next_j]:
                continue
            if order[next_i][next_j]==-1:
                children+=1
                dfs(next_i,next_j,(i,j))
                low[i][j]=min(low[i][j],low[next_i][next_j])
                if parent is not None and low[next_i][next_j]>=order[i][j]:
                    result.add((i,j))
            elif (next_i,next_j)!=parent:
                low[i][j]=min(low[i][j],order[next_i][next_j])

        if parent is None and children>=2:
            result.add((i,j))

    for i in range(n):
        for j in range(n):
            if active[i][j] and order[i][j]==-1:
                dfs(i,j,None)

    return result


active=[[True]*n for _ in range(n)]
degree=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        degree[i][j]=sum(1 for _ in neighbors(i,j))

target_order=[]
for _ in range(n*n):
    articulation=articulation_points()
    _,goal_i,goal_j=min(
        (degree[i][j],i,j)
        for i in range(n)
        for j in range(n)
        if active[i][j] and (i,j) not in articulation
    )
    target_order.append((goal_i,goal_j))
    active[goal_i][goal_j]=False
    for next_i,next_j in neighbors(goal_i,goal_j):
        if active[next_i][next_j]:
            degree[next_i][next_j]-=1

answer=[]
removed_mask=0

for goal_i,goal_j in target_order:
    target=goal_i*n+goal_j
    target_i=target_j=-1
    for i in range(n):
        for j in range(n):
            if a[i][j]==target:
                target_i,target_j=i,j
                break
        if target_i!=-1:
            break

    path=bfs((target_i,target_j),(goal_i,goal_j),removed_mask)
    if path is None:
        break

    for hand in path:
        apply_hand(hand)
        answer.append(hand)

    removed_mask|=1<<(goal_i*n+goal_j)

for hand in answer[:10**5]:
    print(*hand)
