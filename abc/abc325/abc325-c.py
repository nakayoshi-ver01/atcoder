from collections import defaultdict,deque
edge=defaultdict(set)#辺を管理
n,m=map(int,input().split())#ノード数,辺数取得(ここら辺は問題によりけり)
sha=set()
for i in range(n):
    s=list(input())
    for j in range(m):
        if s[j]=='#':
            sha.add((i,j))

count=0
que=deque()
while sha:#探索場所移動テンプレ
    if not que:
        k=sha.pop()
        que.append(k)
        count+=1
    else:
        x=que.popleft()
        if (x[0]+1,x[1]) in sha:
            sha.remove((x[0]+1,x[1]))
            que.append((x[0]+1,x[1]))
        if (x[0]-1,x[1]) in sha:
            sha.remove((x[0]-1,x[1]))
            que.append((x[0]-1,x[1]))
        if (x[0],x[1]+1) in sha:
            sha.remove((x[0],x[1]+1))
            que.append((x[0],x[1]+1))
        if (x[0],x[1]-1) in sha:
            sha.remove((x[0],x[1]-1))
            que.append((x[0],x[1]-1))
        if (x[0]+1,x[1]+1) in sha:
            sha.remove((x[0]+1,x[1]+1))
            que.append((x[0]+1,x[1]+1))
        if (x[0]-1,x[1]-1) in sha:
            sha.remove((x[0]-1,x[1]-1))
            que.append((x[0]-1,x[1]-1))
        if (x[0]+1,x[1]-1) in sha:
            sha.remove((x[0]+1,x[1]-1))
            que.append((x[0]+1,x[1]-1))
        if (x[0]-1,x[1]+1) in sha:
            sha.remove((x[0]-1,x[1]+1))
            que.append((x[0]-1,x[1]+1))
print(count)
