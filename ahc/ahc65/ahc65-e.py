from collections import deque
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
end=n**2

def rotate(a,rail,rotate_dist,rotate_dir):
    state=deque()
    for i in rail:
        state.append(a[i[0]][i[1]])
    state.rotate(rotate_dir * rotate_dist)
    for i in range(len(rail)):
        a[rail[i][0]][rail[i][1]]=state[i]
    return a

rails=[]
rail=[]
for i in range(n):
    rail.append((i,n//2-1))
for i in reversed(range(n)):
    rail.append((i,n//2))
rails.append(rail)

for i in range(n//2):
    rail=[]
    for j in range(n//2):
        rail.append((i*2,j))
    for j in reversed(range(n//2)):
        rail.append((i*2+1,j))
    rails.append(rail)

for i in range(n//2):
    rail=[]
    for j in range(n//2,n):
        rail.append((i*2,j))
    for j in reversed(range(n//2,n)):
        rail.append((i*2+1,j))
    rails.append(rail)

print(len(rails))
for i in rails:
    print(len(i),end=' ')
    for j in i:
        print(*j,end=' ')
    print()

target=0
log=[]
next_state=[[a[i][j] for j in range(n)] for i in range(n)]
while 1:
    # 中央に最小の数字を集める
    for i in range(n//2):
        # 左側
        box_count=0
        min_box_num=n**2
        min_box_pos=(-1,-1)
        for j in rails[i+1]:
            if target <= next_state[j[0]][j[1]] < target + 20:
                box_count += 1
                if next_state[j[0]][j[1]] < min_box_num:
                    min_box_num = next_state[j[0]][j[1]]
                    min_box_pos = j
        if next_state[i*2][n//2-1]!=min_box_num and next_state[i*2+1][n//2-1]!=min_box_num and box_count>0:
            # もし余っているboxがあり、最小のものが中央レーン上にない場合、最小のboxを対象のレーンから中央レーンへboxを移動させる。
            rotate_dist=n//2-1-min_box_pos[1]
            if min_box_pos[0]%2==0:
                rotate_dir=1
            else:
                rotate_dir=-1
            for i in range(rotate_dist):
                log.append((min_box_pos[0]//2+1,rotate_dir))
                next_state=rotate(next_state,rails[min_box_pos[0]//2+1],1,rotate_dir)

    for i in range(n//2):
        # 右側
        box_count=0
        min_box_num=n**2
        min_box_pos=(-1,-1)
        for j in rails[i+1+10]:
            if target <= next_state[j[0]][j[1]] < target + 20:
                box_count += 1
                if next_state[j[0]][j[1]] < min_box_num:
                    min_box_num = next_state[j[0]][j[1]]
                    min_box_pos = j
        if next_state[i*2][n//2]!=min_box_num and next_state[i*2+1][n//2]!=min_box_num and box_count>0:
            # もし余っているboxがあり、最小のものが中央レーン上にない場合、最小のboxを対象のレーンから中央レーンへboxを移動させる。
            rotate_dist=min_box_pos[1]-n//2
            if min_box_pos[0]%2==0:
                rotate_dir=-1
            else:
                rotate_dir=1
            for i in range(rotate_dist):
                log.append((min_box_pos[0]//2+1+10,rotate_dir))
                next_state=rotate(next_state,rails[min_box_pos[0]//2+1+10],1,rotate_dir)
    
    while 1:
        next_box=(-1,-1)
        for i in range(n):
            for j in range(n):
                if next_state[i][j]==target:
                    next_box=(i,j)
                    break
            if next_box!=(-1,-1):
                break
        
        if next_box[1]<n//2-1 or n//2<next_box[1]:
            break
        
        if next_box[1]<=n//2-1:
            # 左側
            # 目標boxを0行目へと押し上げる
            for i in range(next_box[0]):
                log.append((0,-1))
                next_state=rotate(next_state,rails[0],1,-1)

            log.append((0,-1))
            next_state=rotate(next_state,rails[0],1,-1)
        else:
            # 右側
            # 目標boxを0行目へと押し上げる
            for i in range(next_box[0]):
                log.append((0,1))
                next_state=rotate(next_state,rails[0],1,1)

        target+=1

        if target==end:
            break
    
    if target==end:
        break

print(len(log))
for i in log:
    print(*i)