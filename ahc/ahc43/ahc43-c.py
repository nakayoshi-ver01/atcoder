from collections import defaultdict,deque
from sortedcontainers import SortedList, SortedSet
import random
# import sys
# import math
# import bisect
import heapq

class HubTarminal():
    # hub_turminal=[
    #     [
    #         範囲内の個数
    #         場所
    #         ADDRESS
    #         ADDRESS
    #         :
    #         :
    #     ]
    # ]
    pass

class ADDRESS():
    # (
    #     駅予定地との距離
    #     x軸の位置
    #     y軸の位置
    #     id
    # )
    pass


class PLANNEDSITE():
    # (
    #     距離,
    #     現在地,
    #     目的地(ADDRESS),
    # )
    pass


def solve():
    '''
    解く関数
    '''

    STATION_COST=5000
    RAIL_COST=100
    CHECK_LIMIT=300

    # 広さ、人数、資金、ターン数
    n,m,k,t=map(int,input().split())

    addresses,civit=mapping_address(n,m)

    # 目的地が集まってる順に並べる
    hub_tarminal=SortedList()
    for i in range(n):
        for j in range(n):
            hub_tarminal.add([-len(addresses[i][j])]+[(i,j)]+addresses[i][j])
    

    
    for i in range(len(hub_tarminal)):
        minimum_dist=hub_tarminal[i][2][0]
        if (minimum_dist-2)*RAIL_COST+STATION_COST*2<k:
            start_station=hub_tarminal.pop(i)
            break
    rails=[[-1 for _ in range(n)] for _ in range(n)]
    earn=0
    ans_log=[]
    total_tarn=0

    stations=set()
    station_group=defaultdict(set)
    
    counter=0
    next_place=SortedList()
    af_civit=[True for _ in range(m)]
    for i in range(2,len(start_station)):
        next_place.add((start_station[i][0],start_station[1],start_station[i]))
        af_civit[start_station[i][-1]]=False
    while total_tarn<t:
        # 計算用地図
        virturl_rails=[[rails[i][j] for j in range(n)] for i in range(n)]
        # 計算用路線図
        virturl_station_group=defaultdict(set)
        for key in station_group:
            for value in station_group[key]:
                virturl_station_group[key].add(value)
        
        # 接続メモ
        log=[]
        tarn=0
        new_stations=set()
        
        if (hub_tarminal or next_place):
            # 予定地決定
            if not next_place:
                test=hub_tarminal.pop(0)
                for i in range(2,len(test)):
                    if af_civit[test[i][-1]]:
                        next_place.add((test[i][0],test[1],test[i]))
                        af_civit[test[i][-1]]=False
                if next_place:
                    if stations:
                        planned_site=next_place.pop(len(next_place)//2)
                    else:
                        planned_site=next_place.pop(0)
                else:
                    continue
            else:
                planned_site=next_place.pop(len(next_place)//2)

            start=planned_site[1]
            # start=maximum_croud(start,addresses)
            goal=planned_site[2][1:3]
            # goal=maximum_croud(goal,addresses)
            over_flg=False
            stflg=True
            glflg=True
            start_group=start
            goal_group=goal
            # 別駅との接続でコストを減らせるか考える
            for group in virturl_station_group:
                if start in virturl_station_group[group]:
                    start_group=group
                    break
            else:
                stflg=False

            for group in virturl_station_group:
                if goal in virturl_station_group[group]:
                    goal_group=group
                    break
            else:
                glflg=False

            min_dist=10**10
            if stflg and glflg:
                st=()
                gl=()
                for st_cand in virturl_station_group[start_group]:
                    for gl_cand in virturl_station_group[goal_group]:
                        if abs(st_cand[0]-gl_cand[0])+abs(st_cand[1]-gl_cand[1])<min_dist:
                            min_dist=abs(st_cand[0]-gl_cand[0])+abs(st_cand[1]-gl_cand[1])
                            st=st_cand
                            gl=gl_cand
                start=st
                goal=gl
            else:
                # ここにsearch_nearest_railを作る
                if stations:
                    start,goal,start_group,goal_group=search_nearest_rail(
                        start,
                        goal,
                        virturl_rails,
                        virturl_station_group,
                        start_group,
                        goal_group
                    )
                    if not virturl_station_group[start_group]:
                        virturl_station_group[start_group].add(start)
                        start_group=start
                    if not virturl_station_group[goal_group]:
                        virturl_station_group[goal_group].add(goal)
                        goal_group=goal
                else:
                    # 最初の一路線
                    virturl_station_group[start].add(start)
                    start_group=start
                    virturl_station_group[goal].add(goal)
                    goal_group=goal


            new_root_cost=0
            

            if station_distance(start,stations):
                continue
            elif station_distance(goal,stations):
                continue

            # スタート、ゴールが新駅なら先に作成
            if start not in stations:
                new_root_cost+=STATION_COST
                while k<STATION_COST and total_tarn+tarn<t:
                    log.append([-1])
                    tarn+=1
                    k+=earn
                if total_tarn+tarn>=t:
                    over_flg=True
                else:
                    tarn+=1
                    log.append((0,start[0],start[1]))
                    virturl_rails[start[0]][start[1]]=0
                    k-=STATION_COST
                    k+=earn
            if start!=goal:
                if goal not in stations:
                    new_root_cost+=STATION_COST
                    while k<STATION_COST and total_tarn+tarn<t:
                        log.append([-1])
                        tarn+=1
                        k+=earn
                    if total_tarn+tarn>=t:
                        over_flg=True
                    else:
                        tarn+=1
                        log.append((0,goal[0],goal[1]))
                        virturl_rails[goal[0]][goal[1]]=0
                        k-=STATION_COST
                        k+=earn
            # 位置関係ごとに線路を作る
            if start[0]==goal[0]:
                (
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost,
                )=vartical_move(
                    min(start[1],goal[1])+1,
                    max(start[1],goal[1]),
                    start[0],
                    1,
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost,
                )
            elif start[1]==goal[1]:
                (
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost
                )=horizonal_move(
                    min(start[0],goal[0])+1,
                    max(start[0],goal[0]),
                    start[1],
                    2,
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost,
                )
            elif (start[0]-goal[0])*(start[1]-goal[1])>0:
                (
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost,
                )=vartical_move(
                    min(start[1],goal[1])+1,
                    max(start[1],goal[1]),
                    min(start[0],goal[0]),
                    1,
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost,
                )
                if virturl_rails[min(start[0],goal[0])][max(start[1],goal[1])]==-1:
                    while k<RAIL_COST and total_tarn+tarn<t:
                        log.append([-1])
                        tarn+=1
                        k+=earn
                    if total_tarn+tarn>=t:
                        over_flg=True
                    k-=RAIL_COST
                    new_root_cost+=RAIL_COST
                    tarn+=1
                    virturl_rails[min(start[0],goal[0])][max(start[1],goal[1])]=3
                    log.append((3,min(start[0],goal[0]),max(start[1],goal[1])))
                    k+=earn
                elif virturl_rails[min(start[0],goal[0])][max(start[1],goal[1])] not in {0,3}:
                    convine_reader=search_station_group(
                        virturl_rails,
                        virturl_station_group,
                        (min(start[0],goal[0]),max(start[1],goal[1]))
                    )
                    for convine_station in virturl_station_group[convine_reader]:
                        virturl_station_group[start_group]|=virturl_station_group[convine_station]
                        del virturl_station_group[convine_station]
                    
                    while k<STATION_COST and total_tarn+tarn<t:
                        log.append([-1])
                        tarn+=1
                        k+=earn
                    if total_tarn+tarn>=t:
                        over_flg=True
                    k-=STATION_COST
                    new_root_cost+=STATION_COST
                    tarn+=1
                    virturl_rails[min(start[0],goal[0])][max(start[1],goal[1])]=0
                    new_stations.add((min(start[0],goal[0]),max(start[1],goal[1])))
                    log.append((0,min(start[0],goal[0]),max(start[1],goal[1])))
                    k+=earn
                (
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost
                )=horizonal_move(
                    min(start[0],goal[0])+1,
                    max(start[0],goal[0]),
                    max(start[1],goal[1]),
                    2,
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost,
                )
            elif (start[0]-goal[0])*(start[1]-goal[1])<0:
                (
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost,
                )=vartical_move(
                    min(start[1],goal[1])+1,
                    max(start[1],goal[1]),
                    min(start[0],goal[0]),
                    1,
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost,
                )
                if virturl_rails[min(start[0],goal[0])][min(start[1],goal[1])]==-1:
                    while k<RAIL_COST and total_tarn+tarn<t:
                        log.append([-1])
                        tarn+=1
                        k+=earn
                    if total_tarn+tarn>=t:
                        over_flg=True
                    k-=RAIL_COST
                    new_root_cost+=RAIL_COST
                    tarn+=1
                    virturl_rails[min(start[0],goal[0])][min(start[1],goal[1])]=6
                    log.append((6,min(start[0],goal[0]),min(start[1],goal[1])))
                    k+=earn
                elif virturl_rails[min(start[0],goal[0])][min(start[1],goal[1])] not in {0,6}:
                    convine_reader=search_station_group(
                        virturl_rails,
                        virturl_station_group,
                        (min(start[0],goal[0]),min(start[1],goal[1]))
                    )
                    for convine_station in virturl_station_group[convine_reader]:
                        virturl_station_group[start_group]|=virturl_station_group[convine_station]
                        del virturl_station_group[convine_station]
                    while k<STATION_COST and total_tarn+tarn<t:
                        log.append([-1])
                        tarn+=1
                        k+=earn
                    if total_tarn+tarn>=t:
                        over_flg=True
                    k-=STATION_COST
                    new_root_cost+=STATION_COST
                    tarn+=1
                    virturl_rails[min(start[0],goal[0])][min(start[1],goal[1])]=0
                    new_stations.add((min(start[0],goal[0]),min(start[1],goal[1])))
                    log.append((0,min(start[0],goal[0]),min(start[1],goal[1])))
                    k+=earn
                
                (
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost
                )=horizonal_move(
                    min(start[0],goal[0])+1,
                    max(start[0],goal[0]),
                    min(start[1],goal[1]),
                    2,
                    start,
                    goal,
                    virturl_rails,
                    total_tarn,
                    tarn,
                    log,
                    earn,
                    over_flg,
                    virturl_station_group,
                    start_group,
                    new_stations,
                    k,
                    new_root_cost,
                )
            if (t-total_tarn-tarn)*calc_fee(civit[planned_site[2][-1]])>new_root_cost and not over_flg:
                total_tarn+=tarn
                earn+=calc_fee(civit[planned_site[2][-1]])
                new_stations.add(start)
                new_stations.add(goal)
                rails=[[virturl_rails[i][j] for j in range(n)] for i in range(n)]
                for new_station in new_stations:
                    for destination in addresses[new_station[0]][new_station[1]]:
                        if af_civit[destination[-1]]:
                            next_place.add((destination[0],new_station,destination))
                            af_civit[destination[-1]]=False
                stations|=new_stations
                for new_station in new_stations:
                    virturl_station_group[start_group].add(new_station)
                if start_group!=goal_group:
                    for goal_pos in virturl_station_group[goal_group]:
                        virturl_station_group[start_group]|=virturl_station_group[goal_pos]
                        del virturl_station_group[goal_pos]
                station_group=defaultdict(set)
                for key in virturl_station_group:
                    for value in virturl_station_group[key]:
                        station_group[key].add(value)
                # print('virturl',virturl_station_group)
                # print('real',station_group)
                ans_log+=log
            else:
                # print('b',start,goal)
                k-=earn*(len(log))
                k+=new_root_cost
            counter+=1
        else:
            # ターン稼ぎ
            ans_log.append([-1])
            total_tarn+=1
            k+=earn
            if total_tarn+tarn>=t:
                return ans_log

def mapping_address(n,m):
    walk=2

    place=[[[] for _ in range(n)] for _ in range(n)]
    civit=list()
    for i in range(m):
        a,b,c,d=map(int,input().split())
        place[a][b].append((c,d,i))
        civit.append((a,b,c,d))

    grid=[[[] for _ in range(n)] for _ in range(n)]

    for h in range(n):
        for w in range(n):
            for j in range(-walk,walk+1):
                for k in range(-(walk-abs(j)),(walk-abs(j))+1):
                    if 0<=(h+j)<n and 0<=(w+k)<n:
                        for l in place[h+j][w+k]:
                            grid[h][w].append((abs(h-l[0])+abs(w-l[1]),l[0],l[1],l[2]))
            grid[h][w].sort()
    return grid,civit

def search_station_group(grid,station_group,pos):
    '''
    args
    grid:線路の様子
    station_group:駅グループの辞書

    return
    station_groupのキー

    '''
    current=list(pos)
    if grid[current[0]][current[1]]==0:
        for reader in station_group:
            if pos in station_group[reader]:
                return reader
    elif grid[current[0]][current[1]] in {1,5,6}:
        dir=[0,1]
    elif grid[current[0]][current[1]] in {2,3}:
        dir=[1,0]
    elif grid[current[0]][current[1]] in {4}:
        dir=[-1,0]
    while grid[current[0]][current[1]] != 0:
        current[0]+=dir[0]
        current[1]+=dir[1]
        if grid[current[0]][current[1]] in {3,5}:
            dir[0],dir[1]=dir[1],dir[0]
        elif grid[current[0]][current[1]] in {4,6}:
            dir[0],dir[1]=-dir[1],-dir[0]
    current=tuple(current)
    for reader in station_group:
        if current in station_group[reader]:
            return reader

def calc_fee(target_civit):
    return abs(target_civit[0]-target_civit[2])+abs(target_civit[1]-target_civit[3])


def station_distance(target_station,stations):
    '''
    近すぎる駅がないか検索あったら駅建設中止(交差するところは例外)
    '''
    for station in stations:
        if 1<=abs(target_station[0]-station[0])+abs(target_station[1]-station[1])<=3 :
            return True
    else:
        return False


def maximum_croud(place,grid):
    '''
    家の近くで最も目的地が多くなる場所を探す
    '''
    walk=2
    n=50
    max_place=0
    max_position=place
    for j in range(-walk,walk+1):
        for k in range(-(walk-abs(j)),(walk-abs(j))+1):
            if 0<=(place[0]+j)<n and 0<=(place[1]+k)<n:
                if len(grid[place[0]+j][place[1]+k])>max_place:
                    max_position=(place[0]+j,place[1]+k)
                    max_place=len(grid[place[0]+j][place[1]+k])    
    return max_position



def vartical_move(
        start_pos,
        goal_pos,
        height,
        rail_type,
        start,
        goal,
        virturl_rails,
        total_tarn,
        tarn,
        log,
        earn,
        over_flg,
        virturl_station_group,
        start_group,
        new_stations,
        k,
        new_root_cost,
    ):
    RAIL_COST=100
    STATION_COST=5000
    t=800

    for i in range(start_pos,goal_pos):
        if virturl_rails[height][i]==-1:
            while k<RAIL_COST and total_tarn+tarn<t:
                log.append([-1])
                tarn+=1
                k+=earn
            if total_tarn+tarn>=t:
                over_flg=True
            k-=RAIL_COST
            new_root_cost+=RAIL_COST
            tarn+=1
            virturl_rails[height][i]=1
            log.append((1,height,i))
            k+=earn
        elif virturl_rails[height][i] not in {0,rail_type}:
            convine_reader=search_station_group(
                virturl_rails,
                virturl_station_group,
                (height,i)
            )
            for convine_station in virturl_station_group[convine_reader]:
                virturl_station_group[start_group]|=virturl_station_group[convine_station]
                del virturl_station_group[convine_station]
            while k<STATION_COST and total_tarn+tarn<t:
                log.append([-1])
                tarn+=1
                k+=earn
            if total_tarn+tarn>=t:
                over_flg=True
            k-=STATION_COST
            new_root_cost+=STATION_COST
            tarn+=1
            virturl_rails[height][i]=0
            new_stations.add((height,i))
            log.append((0,height,i))
            k+=earn
    
    return (
        start,
        goal,
        virturl_rails,
        total_tarn,
        tarn,
        log,
        earn,
        over_flg,
        virturl_station_group,
        start_group,
        new_stations,
        k,
        new_root_cost
    )


def horizonal_move(
        start_pos,
        goal_pos,
        col,
        rail_type,
        start,
        goal,
        virturl_rails,
        total_tarn,
        tarn,
        log,
        earn,
        over_flg,
        virturl_station_group,
        start_group,
        new_stations,
        k,
        new_root_cost,
    ):
    RAIL_COST=100
    STATION_COST=5000
    t=800

    for i in range(start_pos,goal_pos):
        if virturl_rails[i][col]==-1:
            while k<RAIL_COST and total_tarn+tarn<t:
                log.append([-1])
                tarn+=1
                k+=earn
            if total_tarn+tarn>=t:
                over_flg=True
            k-=RAIL_COST
            new_root_cost+=RAIL_COST
            tarn+=1
            virturl_rails[i][col]=rail_type
            log.append((rail_type,i,col))
            k+=earn
        elif virturl_rails[i][col] not in {0,rail_type}:
            convine_reader=search_station_group(
                virturl_rails,
                virturl_station_group,
                (i,col)
            )
            for convine_station in virturl_station_group[convine_reader]:
                virturl_station_group[start_group]|=virturl_station_group[convine_station]
                del virturl_station_group[convine_station]

            while k<STATION_COST and total_tarn+tarn<t:
                log.append([-1])
                tarn+=1
                k+=earn
            if total_tarn+tarn>=t:
                over_flg=True
            k-=STATION_COST
            new_root_cost+=STATION_COST
            tarn+=1
            virturl_rails[i][col]=0
            new_stations.add((i,col))
            log.append((0,i,col))
            k+=earn

    return (
        start,
        goal,
        virturl_rails,
        total_tarn,
        tarn,
        log,
        earn,
        over_flg,
        virturl_station_group,
        start_group,
        new_stations,
        k,
        new_root_cost
    )

def search_nearest_rail(
        start,
        goal,
        grid,
        station_group,
        start_group,
        target_group
    ):
    
    dist=1
    n=50
    flg=False
    st_group=start_group
    gl_group=target_group
    while 1:
        for j in range(-dist,dist+1):
            for k in range(-(dist-abs(j)),(dist-abs(j))+1):
                if 0<=(start[0]+j)<n and 0<=(start[1]+k)<n:
                    if dist<=2:
                        if grid[start[0]+j][start[1]+k]==0:
                            start=(start[0]+j,start[1]+k)
                            st_group=search_station_group(grid,station_group,start)
                            gl_group=target_group
                            if target_group==st_group:
                                goal=(start[0]+j,start[1]+k)
                                gl_group=st_group
                            return start,goal,st_group,gl_group
                        elif grid[start[0]+j][start[1]+k]!=-1:
                            flg=True
                            start=(start[0]+j,start[1]+k)
                            st_group=search_station_group(grid,station_group,start)
                            if target_group==st_group:
                                goal=(start[0]+j,start[1]+k)
                                gl_group=st_group
                    else:
                        if grid[start[0]+j][start[1]+k]==0:
                            if target_group==search_station_group(grid,station_group,(start[0]+j,start[1]+k)):
                                gl_group=target_group
                                goal=(start[0]+j,start[1]+k)
                                return start,goal,st_group,gl_group
                        elif grid[start[0]+j][start[1]+k]!=-1:
                            flg=True
                            if target_group==search_station_group(grid,station_group,(start[0]+j,start[1]+k)):
                                gl_group=target_group
                                goal=(start[0]+j,start[1]+k)
        if dist==2:
            return start,goal,st_group,gl_group
        dist+=1
            



z=solve()

for i in z:
    print(*i)

