from collections import deque,defaultdict
import random

def list_can_hands(grid_holder,grid_level,pos,i):
    global n
    attack=set()
    move=set()
    move.add(pos)
    new=set()
    state=deque()
    state.append(pos)
    before=[[True for _ in range(n)]for _ in range(n)]
    while state:
        now=state.popleft()
        if now[0]>0 and before[now[0]-1][now[1]]:
            if grid_holder[now[0]-1][now[1]] not in {-1,i}:
                attack.add((now[0]-1,now[1]))
                if grid_level[now[0]-1][now[1]]==1:
                    new.add((now[0]-1,now[1]))
            elif grid_holder[now[0]-1][now[1]]==-1:
                move.add((now[0]-1,now[1]))
                new.add((now[0]-1,now[1]))
            else:
                move.add((now[0]-1,now[1]))
                state.append((now[0]-1,now[1]))
            before[now[0]-1][now[1]]=False

        if now[0]<n-1 and before[now[0]+1][now[1]]:
            if grid_holder[now[0]+1][now[1]] not in {-1,i}:
                attack.add((now[0]+1,now[1]))
                if grid_level[now[0]+1][now[1]]==1:
                    new.add((now[0]+1,now[1]))
            elif grid_holder[now[0]+1][now[1]]==-1:
                move.add((now[0]+1,now[1]))
                new.add((now[0]+1,now[1]))
            else:
                move.add((now[0]+1,now[1]))
                state.append((now[0]+1,now[1]))
            before[now[0]+1][now[1]]=False
        
        if now[1]>0 and before[now[0]][now[1]-1]:
            if grid_holder[now[0]][now[1]-1] not in {-1,i}:
                attack.add((now[0],now[1]-1))
                if grid_level[now[0]][now[1]-1]==1:
                    new.add((now[0],now[1]-1))
            elif grid_holder[now[0]][now[1]-1]==-1:
                move.add((now[0],now[1]-1))
                new.add((now[0],now[1]-1))
            else:
                move.add((now[0],now[1]-1))
                state.append((now[0],now[1]-1))
            before[now[0]][now[1]-1]=False
        
        if now[1]<n-1 and before[now[0]][now[1]+1]:
            if grid_holder[now[0]][now[1]+1] not in {-1,i}:
                attack.add((now[0],now[1]+1))
                if grid_level[now[0]][now[1]+1]==1:
                    new.add((now[0],now[1]+1))
            elif grid_holder[now[0]][now[1]+1]==-1:
                move.add((now[0],now[1]+1))
                new.add((now[0],now[1]+1))
            else:
                move.add((now[0],now[1]+1))
                state.append((now[0],now[1]+1))
            before[now[0]][now[1]+1]=False
    return attack,move,new
    
def debag_mode_ai_choice(grid_holder,grid_level,i,rand_greed,player):
    global ai_weight
    global grid_point
    global u
    player_set=set(player)
    player_set-={player[i]}
    ai_attack,ai_move,ai_new=list_can_hands(grid_holder,grid_level,player[i],i)
    greedy=(-1,-1)
    max_evaluation=-1
    for hand in ai_attack|ai_move|ai_new-player_set:
        if grid_holder[hand[0]][hand[1]]==-1:
            if max_evaluation<grid_point[hand[0]][hand[1]]*ai_weight[i][0]:
                greedy=(hand[0],hand[1])
                max_evaluation=grid_point[hand[0]][hand[1]]*ai_weight[i][0]
        elif grid_holder[hand[0]][hand[1]]==i and grid_level[hand[0]][hand[1]]==u:
            if max_evaluation<0:
                greedy=(hand[0],hand[1])
                max_evaluation=0
        elif grid_holder[hand[0]][hand[1]]==i and grid_level[hand[0]][hand[1]]!=u:
            if max_evaluation<grid_point[hand[0]][hand[1]]*ai_weight[i][1]:
                greedy=(hand[0],hand[1])
                max_evaluation=grid_point[hand[0]][hand[1]]*ai_weight[i][1]
        elif grid_level[hand[0]][hand[1]]==1:
            if max_evaluation<grid_point[hand[0]][hand[1]]*ai_weight[i][2]:
                greedy=(hand[0],hand[1])
                max_evaluation=grid_point[hand[0]][hand[1]]*ai_weight[i][2]
        elif grid_level[hand[0]][hand[1]]!=1:
            if max_evaluation<grid_point[hand[0]][hand[1]]*ai_weight[i][3]:
                greedy=(hand[0],hand[1])
                max_evaluation=grid_point[hand[0]][hand[1]]*ai_weight[i][3]
    
    if ai_weight[i][4]<rand_greed:
        return greedy
    else:
        return (ai_attack|ai_move|ai_new-player_set).pop()

def debag_mode_player_pos(player_choice,player,grid_holder,grid_level):
    """
    ビジュアライザー用の各マスの状態を更新する関数
    
    :param player_choice: Description
    :param player: Description
    :param grid_holder: Description
    :param grid_level: Description
    """
    global u,m
    player_pos=[(-1,-1) for _ in range(m)]
    next_pos=defaultdict(list)
    for i in range(len(player_choice)):
        next_pos[player_choice[i]].append(i)
    for i in next_pos:
        if len(next_pos[i])==1:
            if grid_holder[i[0]][i[1]]==-1:
                grid_holder[i[0]][i[1]]=next_pos[i][0]
                grid_level[i[0]][i[1]]=1
                player_pos[next_pos[i][0]]=i
            elif grid_holder[i[0]][i[1]]==next_pos[i][0]:
                grid_level[i[0]][i[1]]=min(
                    grid_level[i[0]][i[1]]+1,
                    u
                )
                player_pos[next_pos[i][0]]=i
            else:
                grid_level[i[0]][i[1]]-=1
                if grid_level[i[0]][i[1]]==0:
                    grid_holder[i[0]][i[1]]=next_pos[i][0]
                    grid_level[i[0]][i[1]]=1
                    player_pos[next_pos[i][0]]=i
                else:
                    player_pos[next_pos[i][0]]=player[next_pos[i][0]]
        if len(next_pos[i])>1:
            if grid_holder[i[0]][i[1]] in next_pos[i]:
                for j in next_pos[i]:
                    if j==grid_holder[i[0]][i[1]]:
                        player_pos[j]=i
                    else:
                        player_pos[j]=player[j]
            else:
                for j in next_pos[i]:
                    player_pos[j]=player[j]
    return player_pos,grid_holder,grid_level

def evaluation(pos,grid_holder,grid_level,turn):
    """
    各マスの評価を点数とレベルから計算する関数

    所有者なしのマスは点数のまま
    他者所有のマスは(点数*2)/レベル
    自分所有のマスは点数/(レベル+1)
    自分所有のマスでレベルが最大のマスは0
    目的地までの評価値の総和/目的地までのターン数で評価したい
    """
    global u,t,m
    global grid_point
    attack,move,new=list_can_hands(grid_holder,grid_level,pos,0)
    max_evaluation=-1
    max_evaluation_cell=(-1,-1)
    for i in attack|move|new:
        if grid_holder[i[0]][i[1]]==-1:
            temp_evaluation=grid_point[i[0]][i[1]]
        elif grid_holder[i[0]][i[1]]==0 and grid_level[i[0]][i[1]]==u:
            temp_evaluation=0
        elif grid_holder[i[0]][i[1]]==0 and grid_level[i[0]][i[1]]==1:
            temp_evaluation=grid_point[i[0]][i[1]]*2
        elif grid_holder[i[0]][i[1]]==0 and grid_level[i[0]][i[1]]!=1:
            temp_evaluation=grid_point[i[0]][i[1]]*1.2
        elif grid_holder[i[0]][i[1]]!=0 and grid_level[i[0]][i[1]]==1:
            temp_evaluation=grid_point[i[0]][i[1]]*2
        else:
            temp_evaluation=grid_point[i[0]][i[1]]*(m-1)/m
        if max_evaluation<temp_evaluation:
            max_evaluation=temp_evaluation
            max_evaluation_cell=i
    return max_evaluation_cell

def dicide_next_hand(players,grid_holder,grid_level):
    """
    Docstring for dicide_next_hand
    
    :param player: 人がいるマス
    :param grid_holder: マスの所有者
    :param grid_level: マスのレベル

    とりあえず
    奪えるマス>塗られてないマス>攻撃できるマス>自分のマスの順に選んだ。
    必ずレベルマックスにする戦法とか面白い？
    評価が自分のスコア/相手の中の最大スコアなのでやはり奪えるマスを優先するのがいいのかな
    """
    global grid_point
    
    global u,t,m
    global grid_point
    players_set=set(players[1:])
    attack,move,new=list_can_hands(grid_holder,grid_level,players[0],0)
    max_evaluation=-1
    max_evaluation_cell=(-1,-1)
    for i in (attack|move|new)-players_set:
        if grid_holder[i[0]][i[1]]==-1:
            temp_evaluation=grid_point[i[0]][i[1]]
        elif grid_holder[i[0]][i[1]]==0 and grid_level[i[0]][i[1]]==u:
            temp_evaluation=0
        elif grid_holder[i[0]][i[1]]==0 and grid_level[i[0]][i[1]]!=u:
            temp_evaluation=grid_point[i[0]][i[1]]*(1+0.3*((u-grid_level[i[0]][i[1]])/u))
        elif grid_holder[i[0]][i[1]]!=0 and grid_level[i[0]][i[1]]==1:
            temp_evaluation=grid_point[i[0]][i[1]]*2
        else:
            temp_evaluation=grid_point[i[0]][i[1]]*(m-1)/m
        if max_evaluation<temp_evaluation:
            max_evaluation=temp_evaluation
            max_evaluation_cell=i
    return max_evaluation_cell
    


# 入力
n,m,t,u=map(int,input().split())
grid_point=[list(map(int,input().split())) for _ in range(n)]
player=[tuple(map(int,input().split())) for _ in range(m)]

# debag_mode入力
# ai_weight=[[]]+[list(map(float,input().split())) for _ in range(m-1)]


grid_holder=[[-1 for _ in range(n)] for _ in range(n)]
grid_level=[[0 for _ in range(n)] for _ in range(n)]
player_point=[0 for _ in range(m)]

for i in range(m):
    grid_holder[player[i][0]][player[i][1]]=i
    grid_level[player[i][0]][player[i][1]]=1
    player_point[i]+=grid_point[player[i][0]][player[i][1]]

print(*player[0])
player_choice=[player[0]]

for turn in range(t):
    # 入力
    player_choice=[tuple(map(int,input().split())) for _ in range(m)]
    player=[tuple(map(int,input().split())) for _ in range(m)]
    grid_holder=[list(map(int,input().split())) for _ in range(n)]
    grid_level=[list(map(int,input().split())) for _ in range(n)]
    # デバッグ

    # for i in range(1,m):
    #     rand_greed, _ = map(float,input().split())
    #     player_choice.append(
    #         debag_mode_ai_choice(
    #             grid_holder,
    #             grid_level,
    #             i,
    #             rand_greed,
    #             player
    #         )
    #     )
    # print(player_choice)
    # player,grid_holder,grid_level=debag_mode_player_pos(player_choice,player,grid_holder,grid_level)

    next_hand = dicide_next_hand(player,grid_holder,grid_level)
     
    if turn!=t-1:
        print(*next_hand)
        player_choice=[next_hand]