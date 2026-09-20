from collections import deque
import heapq

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
v_wall=[list(map(int,input())) for _ in range(n)]
h_wall=[list(map(int,input())) for _ in range(n-1)]

v_sum=[[0] for _ in range(n+1)]
h_sum=[[0] for _ in range(n)]
v_sum[0]=[0]*n
h_sum[0]=[0]*(n+1)

for i in range(n):
    for j in range(n-1):
        v_sum[i+1].append(v_sum[i+1][-1]+v_wall[i][j])
for i in range(1,n+1):
    for j in range(n):
        v_sum[i][j]+=v_sum[i-1][j]

for i in range(n-1):
    for j in range(n):
        h_sum[i+1].append(h_sum[i+1][-1]+h_wall[i][j])
for i in range(1,n):
    for j in range(n+1):
        h_sum[i][j]+=h_sum[i-1][j]


def wall_check(r,c,h,w):
    return (
        v_sum[r+h][c+w-1]-v_sum[r][c+w-1]
        -v_sum[r+h][c]+v_sum[r][c]==0
        and
        h_sum[r+h-1][c+w]-h_sum[r+h-1][c]
        -h_sum[r][c+w]+h_sum[r][c]==0
    )


def moved_position(i,j,hand):
    direction,r,c,h,w=hand
    if direction=='V':
        half=h//2
        return (i+half,j) if i<r+half else (i-half,j)
    half=w//2
    return (i,j+half) if j<c+half else (i,j-half)


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


# 各角・各移動先ごとに、面積最大の有効候補を取り出すヒープ。
move_heaps=[[{} for _ in range(n)] for _ in range(n)]

for r in range(n):
    for c in range(n):
        for h in range(1,n-r+1):
            for w in range(1,n-c+1):
                if not wall_check(r,c,h,w):
                    continue
                hands=[]
                if h%2==0:
                    hands.append(('V',r,c,h,w))
                if w%2==0:
                    hands.append(('H',r,c,h,w))

                for hand in hands:
                    hand_mask=0
                    row_mask=(1<<w)-1
                    for i in range(r,r+h):
                        hand_mask|=row_mask<<(i*n+c)
                    corners={
                        (r,c),(r+h-1,c),
                        (r,c+w-1),(r+h-1,c+w-1)
                    }
                    for i,j in corners:
                        nxt=moved_position(i,j,hand)
                        heap=move_heaps[i][j].setdefault(nxt,[])
                        heapq.heappush(
                            heap,
                            (-h*w,hand,hand_mask)
                        )


def bfs(start,goal,removed_mask):
    que=deque([start])
    prev={start:None}
    prev_hand={}

    while que:
        now=que.popleft()
        if now==goal:
            break

        i,j=now
        for nxt,heap in move_heaps[i][j].items():
            while heap and heap[0][2]&removed_mask:
                heapq.heappop(heap)
            if not heap or nxt in prev:
                continue
            prev[nxt]=now
            prev_hand[nxt]=heap[0][1]
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


def neighbors(i,j):
    if i>0 and h_wall[i-1][j]==0:
        yield i-1,j
    if i+1<n and h_wall[i][j]==0:
        yield i+1,j
    if j>0 and v_wall[i][j-1]==0:
        yield i,j-1
    if j+1<n and v_wall[i][j]==0:
        yield i,j+1


bfs_order=[]
que=deque([(0,0)])
seen=[[False]*n for _ in range(n)]
seen[0][0]=True

while que:
    i,j=que.popleft()
    bfs_order.append((i,j))
    for next_i,next_j in neighbors(i,j):
        if seen[next_i][next_j]:
            continue
        seen[next_i][next_j]=True
        que.append((next_i,next_j))

# BFS木の葉側から処理し、根 (0, 0) を最後に残す。
target_order=bfs_order[::-1]

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
