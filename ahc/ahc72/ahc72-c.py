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



def calc_cost2(state):
    ans=0
    dist_map=dict()
    s=deque()
    for i in nests:
        s.append((i,nests[i],0))
        dist_map[(i,*nests[i])]=0

    while s:
        now=s.popleft()
        for dir in dirs:
            dh=dirs[dir][0]
            dw=dirs[dir][1]
            if (
                0<=now[1][0]+dh<n and
                0<=now[1][1]+dw<n and
                grid[now[1][0]+dh][now[1][1]+dw]=='.' and
                (now[0],now[1][0]+dh,now[1][1]+dw) not in dist_map
            ):
                for i in state[(now[1][0]+dh,now[1][1]+dw)]:
                    if i[0].upper()==now[0]:
                        ans+=now[2]+1
                s.append((now[0],(now[1][0]+dh,now[1][1]+dw),now[2]+1))
                dist_map[(now[0],now[1][0]+dh,now[1][1]+dw)]=now[2]+1
    return ans


    
def evaluation(state):
    '''
    盤面評価
    '''
    return calc_cost2(state)

first_cost=evaluation(state_grid)

def count_slimes(cell):
    '''
    マスのスライム数カウント
    '''
    num_of_slimes=0
    for i in cell:
        num_of_slimes+=i[1]
    return num_of_slimes

def same_kind(cell,move):
    '''
    移動先で同じスライムが連続するか確認
    '''
    if cell and cell[-1][0]==move[-1][0]:
        return True
    else:
        return False

def check_color(cell,color):
    '''
    移動候補のスライムがトップにいるか確認
    '''
    for i in cell:
        if i[0]==color:
            return True
    else:
        return False

def execution(code,state):
    '''
    コマンド実行後の盤面を再現
    '''
    nextstate=defaultdict(deque)
    for i in state:
        for j in state[i]:
            nextstate[i].append(j[:])
    move_slime=deque()
    slime_num=count_slimes(nextstate[(code[0],code[1])])
    while slime_num>code[2]:
        move=nextstate[(code[0],code[1])].pop()
        move_slime.append(move)
        slime_num-=move[1]
    while move_slime:
        jump_to=(code[0]+dirs[code[3]][0]*code[4],code[1]+dirs[code[3]][1]*code[4])
        if nextstate[jump_to] and nextstate[jump_to][-1][0]==move_slime[0][0]:
            nextstate[jump_to][-1][1]+=move_slime.popleft()[1]
        else:
            nextstate[jump_to].append(move_slime.popleft())
    return nextstate

beam=[]
nexts=[]
dd=0

minimum_cost=10**10
# 手数、コスト、状態、手順
heapq.heappush(beam,(0,first_cost,[],state_grid))
while minimum_cost:
    pre_cand=[]
    while beam:
        now=heapq.heappop(beam)
        # test_grid=defaultdict(deque)
        # for j in now[3]:
        #     for k in now[3][j]:
        #         test_grid[j].append(k[:])

        test_grid=defaultdict(deque)
        target_color='z'
        for i in now[3]:
            for j in range(len(now[3][i])):
                if j==len(now[3][i])-1 and i==nests[now[3][i][j][0].upper()]:
                    continue
                test_grid[i].append(now[3][i][j][:])
                if now[3][i][j][0]<target_color:
                    target_color=now[3][i][j][0]
        slime_pos=list(test_grid.keys())
        code_cand=[]
        
        for pos in slime_pos:
            if test_grid[pos] and check_color(test_grid[pos],target_color):
                len_cell=len(test_grid[pos])
                num_slime=count_slimes(test_grid[pos])

                move_slime=0
                slime_temp=deque()
                for i in range(len_cell):
                    move_slime+=test_grid[pos][-i-1][1]
                    for dir in dirs:
                        dh=dirs[dir][0]
                        dw=dirs[dir][1]
                        while (
                            0<=pos[0]+dh<n and
                            0<=pos[1]+dw<n and
                            abs(dh+dw)<=num_slime-move_slime+1 and
                            grid[pos[0]+dh][pos[1]+dw]=='.'
                        ):
                            if count_slimes(test_grid[(pos[0]+dh,pos[1]+dw)])+move_slime<=8:
                                if same_kind(test_grid[(pos[0]+dh,pos[1]+dw)],test_grid[pos]):
                                    # iブロック取り出す
                                    tmp_slime=test_grid[pos].pop()
                                    test_grid[(pos[0]+dh,pos[1]+dw)][-1][1]+=tmp_slime[1]
                                    for j in range(1,i+1):
                                        test_grid[(pos[0]+dh,pos[1]+dw)].append(test_grid[pos].pop())
                                    heapq.heappush(
                                    code_cand,
                                    (
                                        evaluation(test_grid),
                                        (pos[0],pos[1],num_slime-move_slime,dir,max(abs(dh),abs(dw))),
                                    ))
                                    # iブロック戻す
                                    for j in range(1,i+1):
                                        test_grid[pos].append(test_grid[(pos[0]+dh,pos[1]+dw)].pop())
                                    test_grid[(pos[0]+dh,pos[1]+dw)][-1][1]-=tmp_slime[1]
                                    test_grid[pos].append(tmp_slime)
                                else:
                                    # iブロック取り出す
                                    for j in range(i+1):                                    
                                        test_grid[(pos[0]+dh,pos[1]+dw)].append(test_grid[pos].pop())
                                    heapq.heappush(
                                    code_cand,
                                    (
                                        evaluation(test_grid),
                                        (pos[0],pos[1],num_slime-move_slime,dir,max(abs(dh),abs(dw))),
                                    ))
                                    # iブロック戻す
                                    for j in range(i+1):
                                        test_grid[pos].append(test_grid[(pos[0]+dh,pos[1]+dw)].pop())
                            dh+=dirs[dir][0]
                            dw+=dirs[dir][1]
        cand=heapq.heappop(code_cand)
        cand_state=execution(cand[1],test_grid)
        heapq.heappush(
            pre_cand,
            (
                now[0]+1,
                cand[0],
                now[2]+[cand[1]],
                cand_state,
            ))
        minimum_cost=min(cand[0],minimum_cost)    
    cand=heapq.heappop(pre_cand)
    heapq.heappush(
        beam,
        cand
    )
    pre_cand.clear()

p=heapq.heappop(beam)
for i in p[-2]:
    print(*i)