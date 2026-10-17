from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(n)]
# from functools import cmp_to_key, lru_cache

nests=dict()

for i in range(n):
    for j in range(n):
        if grid[i][j].isupper():
            nests[grid[i][j]]=(i,j)
            grid[i][j]='.'

state_grid=defaultdict(deque)
for i in range(n):
    for j in range(n):
        if grid[i][j].islower():
            state_grid[(i,j)].append([grid[i][j],1])
            grid[i][j]='.'

dirs={'D':[1,0],'R':[0,1],'U':[-1,0],'L':[0,-1]}

def calc_cost(pos,slime):
    queue=deque()
    queue.appendleft(('',0,pos))
    min_cost=dict()
    min_cost[pos]=0
    while queue:
        now=queue.popleft()
        if now[2]==nests[slime[0].upper()]:
            return now[1]
        for dir in dirs:
            dh=dirs[dir][0]
            dw=dirs[dir][1]
            if (
                0<=now[2][0]+dh<n and
                0<=now[2][1]+dw<n and
                grid[now[2][0]+dh][now[2][1]+dw]=='.' and
                (now[2][0]+dh,now[2][1]+dw) not in min_cost
            ):
                queue.append((dir,now[1]+1,(now[2][0]+dh,now[2][1]+dw)))
                min_cost[(now[2][0]+dh,now[2][1]+dw)]=now[1]+1

def evaluation(state):
    cost=0
    for i in state:
        for k in range(len(state[i])):
            almost_cost=calc_cost(i,state[i][k])
            if almost_cost==0:
                if k!=len(state[i])-1:
                    # 移動して、上どけて戻るため
                    almost_cost+=1
            cost+=almost_cost
    return cost

first_cost=evaluation(state_grid)

def count_slimes(cell):
    num_of_slimes=0
    for i in cell:
        num_of_slimes+=i[1]
    return num_of_slimes

def same_kind(cell,move):
    if cell and cell[-1][0]==move[0][0]:
        return True
    else:
        return False

def check_color(cell,color):
    for i in cell:
        if i[0]==color:
            return True
    else:
        return False


beam=[]
nexts=[]
dd=0

minimum_cost=first_cost
# 手数、コスト、状態、手順
heapq.heappush(beam,(0,first_cost,[],state_grid))
while minimum_cost:
    while beam:
        now=heapq.heappop(beam)
        cell_state=defaultdict(deque)
        target_color='z'
        for i in now[3]:
            for j in range(len(now[3][i])):
                if j==len(now[3][i])-1 and i==nests[now[3][i][j][0].upper()]:
                    continue
                cell_state[i].append(now[3][i][j][:])
                if now[3][i][j][0]<target_color:
                    target_color=now[3][i][j][0]
        slime_pos=list(cell_state.keys())
        for pos in slime_pos:
            if cell_state[pos] and check_color(cell_state[pos],target_color):
                len_cell=len(cell_state[pos])
                num_slime=count_slimes(cell_state[pos])

                move_slime=0
                slime_temp=deque()
                for i in range(len_cell):
                    slime=cell_state[pos].pop()
                    slime_temp.append(slime)
                    move_slime+=slime[1]
                    for dir in dirs:
                        dh=dirs[dir][0]
                        dw=dirs[dir][1]
                        while (
                            0<=pos[0]+dh<n and
                            0<=pos[1]+dw<n and
                            abs(dh+dw)<=num_slime-move_slime+1 and
                            grid[pos[0]+dh][pos[1]+dw]=='.'
                        ):
                            test_grid=defaultdict(deque)
                            for j in now[3]:
                                for k in now[3][j]:
                                    test_grid[j].append(k[:])
                            for j in range(i+1):
                                test_grid[pos].pop()
                            if count_slimes(test_grid[(pos[0]+dh,pos[1]+dw)])+count_slimes(slime_temp)<=8:
                                if same_kind(test_grid[(pos[0]+dh,pos[1]+dw)],slime_temp):
                                    test_grid[(pos[0]+dh,pos[1]+dw)][-1][1]+=slime_temp[0][1]
                                    for j in range(1,len(slime_temp)):
                                        test_grid[(pos[0]+dh,pos[1]+dw)].append(slime_temp[j])
                                    heapq.heappush(
                                    nexts,
                                    (
                                        now[0]+1,
                                        evaluation(test_grid),
                                        now[2]+[(pos[0],pos[1],num_slime-move_slime,dir,max(abs(dh),abs(dw)))],
                                        test_grid,
                                    ))
                                else:
                                    for j in range(len(slime_temp)):
                                        test_grid[(pos[0]+dh,pos[1]+dw)].append(slime_temp[j])
                                    heapq.heappush(
                                    nexts,
                                    (
                                        now[0]+1,
                                        evaluation(test_grid),
                                        now[2]+[(pos[0],pos[1],num_slime-move_slime,dir,max(abs(dh),abs(dw)))],
                                        test_grid,
                                    ))
                            dh+=dirs[dir][0]
                            dw+=dirs[dir][1]

    for i in range(min(3,len(nexts))):
        cand=heapq.heappop(nexts)
        heapq.heappush(beam,cand)
        minimum_cost=min(cand[1],minimum_cost)
    nexts.clear()


for i in heapq.heappop(beam)[-2]:
    print(*i)