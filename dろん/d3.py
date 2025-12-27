# coding: utf-8
# Your code here!

from collections import defaultdict,deque
import sys
sys.setrecursionlimit(1000000)
N = int(input())
h = [input() for _ in range(N-1)]
v = [input() for _ in range(N)]
d = [list(map(int, input().split())) for _ in range(N)]
minroot=[[str() for _ in range(N)] for _ in range(N)]
testvis=[[False for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
af=set()
flg=0
allflg=1
nextp=tuple()
here=tuple()
for i in range(N):
    for j in range(N):
        af.add((i,j))
edge=defaultdict(defaultdict)
for i in range(N):
    for j in range(N):
        if j>0 and v[i][j-1]=='0':
            edge[(i,j)]['L']=(i,j-1)
        if i>0 and h[i-1][j]=='0':
            edge[(i,j)]['U']=(i-1,j)
        if j<N-1 and v[i][j]=='0':
            edge[(i,j)]['R']=(i,j+1)
        if i<N-1 and h[i][j]=='0':
            edge[(i,j)]['D']=(i+1,j)

#bfsで最短の帰路をメモ
lastp=(0,0)
saitan=deque()
saitan.append((0,0,''))
testvis[0][0]=True
root=defaultdict(set)
root[(0,0)].add((0,0))
while saitan:
    now=saitan.popleft()
    minroot[now[0]][now[1]]+=now[2]
    for i in edge[now[:2]]:
        dir=edge[now[:2]][i]
        if not testvis[dir[0]][dir[1]]:
            minroot[dir[0]][dir[1]]+=minroot[now[0]][now[1]]
            if i=='U':
                saitan.append((dir[0],dir[1],'D'))
                testvis[dir[0]][dir[1]]=True
                root[dir]=root[now[:2]]|{dir}
            elif i=='D':
                saitan.append((dir[0],dir[1],'U'))
                testvis[dir[0]][dir[1]]=True
                root[dir]=root[now[:2]]|{dir}
            elif i=='L':
                saitan.append((dir[0],dir[1],'R'))
                testvis[dir[0]][dir[1]]=True
                root[dir]=root[now[:2]]|{dir}
            elif i=='R':
                saitan.append((dir[0],dir[1],'L'))
                testvis[dir[0]][dir[1]]=True
                root[dir]=root[now[:2]]|{dir}

# 全てのマスを通るまでdfsマスを全て探索したら最短経路で帰る
def dfs(edge, i, j):
    global af
    global lastp
    global nextp
    global flg
    global here
    here=(i,j)
    af-={(i,j)}
    visited[i][j] = True
    ddir=['U','R','L','D']
    for dir in ddir:
        if dir in edge[(i,j)]:
            di, dj = edge[(i,j)][dir][0],edge[(i,j)][dir][1]
            if not visited[di][dj]:
                print(dir, end='')
                dfs(edge,di,dj)
                if af:
                    if flg==0:
                        nextp=here
                        flg=1
                else:
                    if lastp==(0,0):
                        lastp=edge[(i,j)][dir]
                        flg=1
        if flg==1:
            break


def bfs(edge,now,af):
    shortcut=deque()
    shortcut.append((now,''))
    place=((N+1,N+1),'')
    look = [[False for _ in range(N)] for _ in range(N)]
    while place[0] not in af:
        place=shortcut.popleft()
        for i in edge[place[0]]:
            if i=='U' and look[place[0][0]-1][place[0][1]]==False:
                shortcut.append(((place[0][0]-1,place[0][1]),place[1]+'U'))
                look[place[0][0]-1][place[0][1]]=True
            if i=='D' and look[place[0][0]+1][place[0][1]]==False:
                shortcut.append(((place[0][0]+1,place[0][1]),place[1]+'D'))
                look[place[0][0]+1][place[0][1]]=True
            if i=='L' and look[place[0][0]][place[0][1]-1]==False:
                shortcut.append(((place[0][0],place[0][1]-1),place[1]+'L'))
                look[place[0][0]][place[0][1]-1]=True
            if i=='R' and look[place[0][0]][place[0][1]+1]==False:
                shortcut.append(((place[0][0],place[0][1]+1),place[1]+'R'))
                look[place[0][0]][place[0][1]+1]=True
            
    return place

dfs(edge,0,0)
while af:
    flg=0
    place=bfs(edge,here,af)
    print(place[1],end='')
    dfs(edge,place[0][0],place[0][1])
    #print(here,nextp)
    if not af:
        s1=list(minroot[here[0]][here[1]])
        s1.reverse()
        print(''.join(s1))
        #print(nextp,lastp,here,len(s1))
        allflg=0

if allflg==1:
    s1=list(minroot[here[0]][here[1]])
    s1.reverse()
    print(''.join(s1))
    allflg=0
