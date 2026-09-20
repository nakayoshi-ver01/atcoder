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
section=0
while 1:
    for tmp in range(section*20, section*20 + 20):
        next_box=(-1,-1)
        for i in range(n):
            for j in range(n):
                if next_state[i][j]==tmp:
                    next_box=(i,j)
                    break
            if next_box!=(-1,-1):
                break
 
        
        if next_box[1]<=n//2-1:
            # 左側
            # 目標boxを中央へと集める
            rotate_dist=n//2-1-next_box[1]
            if next_box[0]%2==0:
                rotate_dir=1
            else:
                rotate_dir=-1
            for i in range(rotate_dist):
                # もし近い数字が中央レーン上にあれば、現在動かしているレールからよける。
                while section*20<=next_state[(next_box[0]//2)*2][n//2-1]<section*20+20 or section*20<=next_state[(next_box[0]//2)*2+1][n//2-1]<section*20+20:
                    log.append((0,-1))
                    next_state=rotate(next_state,rails[0],1,-1)
                    if next_state[0][n//2]==target:
                        target+=1
                    
                log.append((next_box[0]//2+1,rotate_dir))
                next_state=rotate(next_state,rails[next_box[0]//2+1],1,rotate_dir)
                if next_state[0][n//2]==target:
                    target+=1
        else:
            # 右側
            # 目標boxを中央へと集める
            rotate_dist=next_box[1]-n//2
            if next_box[0]%2==0:
                rotate_dir=-1
            else:
                rotate_dir=1
            for i in range(rotate_dist):
                log.append((next_box[0]//2+1+10,rotate_dir))
                next_state=rotate(next_state,rails[next_box[0]//2+1+10],1,rotate_dir)
                if next_state[0][n//2]==target:
                    target+=1
                # もし近い数字が中央レーン上にあれば、現在動かしているレールからよける。
                while section*20<=next_state[(next_box[0]//2)*2][n//2]<section*20+20 or section*20<=next_state[(next_box[0]//2)*2+1][n//2]<section*20+20:
                    print(tmp,next_state[(next_box[0]//2)*2][n//2],next_state[(next_box[0]//2)*2+1][n//2])
                    log.append((0,-1))
                    next_state=rotate(next_state,rails[0],1,-1)
                    if next_state[0][n//2]==target:
                        target+=1

    # for i in next_state:
    #     print(i)
    print(len(log))
    for i in log:
        print(*i)
    section+=1  
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
            raise ValueError(next_box,target)
        
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