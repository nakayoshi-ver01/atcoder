from collections import deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
n=int(input())
# n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
# s=list(input())

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

    
def evaluation(hand,target):
    total_score=0

    for i in range(n):
        for j in range(n):
            if a[i][j]==target:
                bonus=-10**5
            else:
                bonus=1
            score=-10**10
            if hand[0]=='V':
                if hand[1]<=i<hand[1]+hand[3]//2 and hand[2]<=j<=hand[2]+hand[4]:
                    score=abs((i+(hand[3]//2))*n+j-a[i][j])
                elif hand[1]+hand[3]//2<=i<hand[1]+hand[3] and hand[2]<=j<=hand[2]+hand[4]:
                    score=abs((i-(hand[3]//2))*n+j-a[i][j])
                else:
                    score=abs((i*n+j-a[i][j]))
            elif hand[0]=='H':
                if hand[1]<=i<=hand[1]+hand[3] and hand[2]<=j<hand[2]+hand[4]//2:
                    score=abs(i*n+(j+(hand[4]//2))-a[i][j])
                elif hand[1]<=i<=hand[1]+hand[3] and hand[2]+hand[4]//2<=j<hand[2]+hand[4]:
                    score=abs(i*n+(j-(hand[4]//2))-a[i][j])
                else:
                    score=abs((i*n+j-a[i][j]))
            if score==0:
                total_score-=10**3
            else:
                total_score+=score*bonus
    return -total_score


def swap(hand):
    if hand[0]=='V':
        tmp=[a[hand[1]+i][hand[2]:hand[2]+hand[4]] for i in range(hand[3]//2)]
        for i in range(hand[3]//2):
            for j in range(hand[4]):
                a[hand[1]+i][hand[2]+j]=a[hand[1]+(hand[3]//2)+i][hand[2]+j]
        for i in range(hand[3]//2):
            a[hand[1]+(hand[3]//2)+i][hand[2]:hand[2]+hand[4]]=tmp[i][:]
    if hand[0]=='H':
        tmp=[a[hand[1]+i][hand[2]:hand[2]+(hand[4]//2)] for i in range(hand[3])]
        for i in range(hand[3]):
            for j in range(hand[4]//2):
                a[hand[1]+i][hand[2]+j]=a[hand[1]+i][hand[2]+(hand[4]//2)+j]
        for i in range(hand[3]):
            a[hand[1]+i][hand[2]+(hand[4]//2):hand[2]+hand[4]]=tmp[i][:]

def wall_check(i,j,k,l):
    if (
        v_wall_check[i+k][j+l-1]-v_wall_check[i][j+l-1]-v_wall_check[i+k][j]+v_wall_check[i][j]==0 and 
        h_wall_check[i+k-1][j+l]-h_wall_check[i+k-1][j]-h_wall_check[i][j+l]+h_wall_check[i][j]==0
    ):
            return True
        
    else:
        return False

cand=set()

for i in range(n):
    for j in range(n):
        for k in range(1,n-i+1):
            for l in range(1,n-j+1):
                if wall_check(i,j,k,l):
                    if k%2==0:
                        cand.add(('V',i,j,k,l))
                    if l%2==0:
                        cand.add(('H',i,j,k,l))

moves_from_corner=[[[] for _ in range(n)] for _ in range(n)]

for hand in sorted(cand):
    _,r,c,h,w=hand
    corners={(r,c),(r+h-1,c),(r,c+w-1),(r+h-1,c+w-1)}
    for i,j in corners:
        moves_from_corner[i][j].append(hand)

for i in range(n):
    for j in range(n):
        moves_from_corner[i][j].sort(
            key=lambda hand:hand[3]*hand[4],
            reverse=True
        )


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


def rectangle_sum(prefix,r,c,h,w):
    return (
        prefix[r+h][c+w]-prefix[r][c+w]
        -prefix[r+h][c]+prefix[r][c]
    )


def bfs(start,goal,removed_prefix):
    que=deque([start])
    prev={start:None}
    prev_hand={}

    while que:
        now=que.popleft()
        if now==goal:
            break

        i,j=now
        for hand in moves_from_corner[i][j]:
            _,r,c,h,w=hand
            # 既に確定してグラフから削除したマスを含む操作は行わない。
            if rectangle_sum(removed_prefix,r,c,h,w)>0:
                continue

            nxt=moved_position(i,j,hand)
            if nxt in prev:
                continue
            prev[nxt]=now
            prev_hand[nxt]=hand
            que.append(nxt)

    if goal not in prev:
        return None

    path=[]
    now=goal
    while now!=start:
        path.append(prev_hand[now])
        now=prev[now]
    path.reverse()
    return path


def bfs_from_region(wanted_region,region,goal,removed_prefix):
    que=deque()
    prev={}
    prev_hand={}

    for i in range(n):
        for j in range(n):
            card=a[i][j]
            if active[i][j] and region[card//n][card%n]==wanted_region:
                pos=(i,j)
                que.append(pos)
                prev[pos]=None

    while que:
        now=que.popleft()
        if now==goal:
            break

        i,j=now
        for hand in moves_from_corner[i][j]:
            _,r,c,h,w=hand
            if rectangle_sum(removed_prefix,r,c,h,w)>0:
                continue

            nxt=moved_position(i,j,hand)
            if nxt in prev:
                continue
            prev[nxt]=now
            prev_hand[nxt]=hand
            que.append(nxt)

    if goal not in prev:
        return None

    path=[]
    now=goal
    while prev[now] is not None:
        path.append(prev_hand[now])
        now=prev[now]
    path.reverse()
    return path


answer=[]

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


def make_rectangle_partition():
    region=[[-1]*n for _ in range(n)]
    region_count=0

    for r in range(n):
        for c in range(n):
            if region[r][c]!=-1:
                continue

            best_h=best_w=1
            best_area=1
            for h in range(1,n-r+1):
                for w in range(1,n-c+1):
                    if h*w<=best_area or not wall_check(r,c,h,w):
                        continue
                    if any(
                        region[i][j]!=-1
                        for i in range(r,r+h)
                        for j in range(c,c+w)
                    ):
                        continue
                    best_h,best_w=h,w
                    best_area=h*w

            for i in range(r,r+best_h):
                for j in range(c,c+best_w):
                    region[i][j]=region_count
            region_count+=1

    return region


def initialize_active_graph():
    new_active=[[True]*n for _ in range(n)]
    new_degree=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_degree[i][j]=sum(1 for _ in neighbors(i,j))
    return new_active,new_degree


def gather_cards_into_regions(region):
    global active,degree

    active,degree=initialize_active_graph()

    for _ in range(n*n):
        articulation=articulation_points()
        _,goal_i,goal_j=min(
            (degree[i][j],i,j)
            for i in range(n)
            for j in range(n)
            if active[i][j] and (i,j) not in articulation
        )
        wanted_region=region[goal_i][goal_j]

        removed_prefix=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                removed_prefix[i+1][j+1]=(
                    removed_prefix[i][j+1]+removed_prefix[i+1][j]
                    -removed_prefix[i][j]+(not active[i][j])
                )

        path=bfs_from_region(
            wanted_region,
            region,
            (goal_i,goal_j),
            removed_prefix
        )

        if path is None:
            return

        for hand in path:
            swap(hand)
            answer.append(hand)

        active[goal_i][goal_j]=False
        for next_i,next_j in neighbors(goal_i,goal_j):
            if active[next_i][next_j]:
                degree[next_i][next_j]-=1


region=make_rectangle_partition()
gather_cards_into_regions(region)

region_count=max(max(row) for row in region)+1

for region_id in range(region_count):
    active=[
        [region[i][j]==region_id for j in range(n)]
        for i in range(n)
    ]
    degree=[[0]*n for _ in range(n)]
    region_size=sum(sum(row) for row in active)

    for i in range(n):
        for j in range(n):
            if active[i][j]:
                degree[i][j]=sum(
                    active[next_i][next_j]
                    for next_i,next_j in neighbors(i,j)
                )

    for _ in range(region_size):
        articulation=articulation_points()
        _,goal_i,goal_j=min(
            (degree[i][j],i,j)
            for i in range(n)
            for j in range(n)
            if active[i][j] and (i,j) not in articulation
        )

        target=goal_i*n+goal_j
        target_i=target_j=-1
        for i in range(n):
            for j in range(n):
                if a[i][j]==target:
                    target_i,target_j=i,j
                    break
            if target_i!=-1:
                break

        start=(target_i,target_j)
        goal=(goal_i,goal_j)

        removed_prefix=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                removed_prefix[i+1][j+1]=(
                    removed_prefix[i][j+1]+removed_prefix[i+1][j]
                    -removed_prefix[i][j]+(not active[i][j])
                )

        path=bfs(start,goal,removed_prefix)

        if path is None:
            break

        for hand in path:
            swap(hand)
            answer.append(hand)

        active[goal_i][goal_j]=False
        for next_i,next_j in neighbors(goal_i,goal_j):
            if active[next_i][next_j]:
                degree[next_i][next_j]-=1

for hand in answer[:10**5]:
    print(*hand)