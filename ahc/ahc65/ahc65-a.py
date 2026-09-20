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
    rail.append((0,i))
for i in reversed(range(n)):
    rail.append((1,i))
rails.append(rail)

for i in range(n//2):
    rail=[]
    for j in range(n):
        rail.append((j,i*2))
    for j in reversed(range(n)):
        rail.append((j,i*2+1))
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
    next_box=(-1,-1)
    for i in range(n):
        for j in range(n):
            if next_state[i][j]==target:
                next_box=(i,j)
                break
        if next_box!=(-1,-1):
            break
    
    # 各boxを0行目へと押し上げる
    if next_box[0]!=0:
        rotate_dist=next_box[0]
        if next_box[1]%2==0:
            rotate_dir=-1
        else:
            rotate_dir=1
        for i in range(rotate_dist):
            log.append((next_box[1]//2+1,rotate_dir))
        next_state=rotate(next_state,rails[next_box[1]//2+1],rotate_dist,rotate_dir)
    
    # 0行目のboxを中央に持っていく
    if next_box[1]!=n//2:
        rotate_dist=abs(next_box[1]-n//2)
        if next_box[1]<n//2:
            rotate_dir=1
        else:
            rotate_dir=-1
        for i in range(rotate_dist):
            log.append((0,rotate_dir))
        next_state=rotate(next_state,rails[0],rotate_dist,rotate_dir)
    
    target+=1

    if target==end:
        break


print(len(log))
for i in log:
    print(*i)

