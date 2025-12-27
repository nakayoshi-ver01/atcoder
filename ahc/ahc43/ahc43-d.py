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

    af_civit=[True for _ in range(m)]
    addresses,civit=mapping_address(n,m)
    sorted_civit=civit[::]
    sorted_civit.sort(key=lambda x:abs(x[0]-x[2])+abs(x[1]-x[3]))
    next_place=SortedList()
    ok=0
    ng=len(sorted_civit)
    center=(ok+ng)//2
    while ok+1<ng:
        tar=sorted_civit[center]
        if (abs(tar[0]-tar[2])+abs(tar[1]-tar[3])-4)*RAIL_COST+STATION_COST*2<=k:
            ok=center
        else:
            ng=center
        center=(ok+ng)//2
    
    for i in range(3):
        next_place.add(
            (
                -2000,
                (
                    sorted_civit[center-i][0],
                    sorted_civit[center-i][1]
                ),
                (
                    abs(sorted_civit[center-i][0]-sorted_civit[center-i][2])+abs(sorted_civit[center-i][1]-sorted_civit[center-i][3]),
                    sorted_civit[center-i][2],
                    sorted_civit[center-i][3],
                    sorted_civit[center-i][4],
                )
            )
        )
        af_civit[sorted_civit[center-i][-1]]=False
    # print(next_place)
    # 目的地が集まってる順に並べる
    hub_tarminal=SortedList()
    for i in range(n):
        for j in range(n):
            hub_tarminal.add([-len(addresses[i][j])]+[(i,j)]+addresses[i][j])
    hub_tarminal=hub_tarminal[:len(hub_tarminal)//4]

    # 一番短い距離を探している
    # for i in range(len(hub_tarminal)):
    #     minimum_dist=hub_tarminal[i][2][0]
    #     if (minimum_dist-2)*RAIL_COST+STATION_COST*2<k:
    #         start_station=hub_tarminal.pop(i)
    #         break
    rails=[[-1 for _ in range(n)] for _ in range(n)]
    earn=0
    ans_log=[]
    total_tarn=0

    stations=set()
    station_group=defaultdict(set)
    
    counter=0
    
    # for i in range(2,len(start_station)):
    #     next_place.add((start_station[i][0],start_station[1],start_station[i]))
    #     af_civit[start_station[i][-1]]=False
    pop_flg=False
    while total_tarn<t:
        goal_flg=True
        # 途中で目的を達成した時のフラグ
        stop_flg=False
        # 途中でくっついた駅たち
        convine_readers=set()
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
        state=[[],[],[],[]]
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
                        planned_site=next_place.pop()
                    else:
                        planned_site=next_place.pop(0)
                else:
                    continue
            else:
                planned_site=next_place.pop()
            
            start=planned_site[1]
            # start=maximum_croud(start,addresses)
            goal=planned_site[2][1:3]
            # goal=maximum_croud(goal,addresses)
            over_flg=False
            # print('before',start,goal)
            # 別駅との接続でコストを減らせるか考える
            for group in virturl_station_group:
                if start in virturl_station_group[group]:
                    start_group=group
                    break
            else:
                virturl_station_group[start].add(start)
                start_group=start

            for group in virturl_station_group:
                if goal in virturl_station_group[group]:
                    goal_group=group
                    break
            else:
                virturl_station_group[goal].add(goal)
                goal_group=goal

            min_dist=10**10
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

            if station_distance(start,stations):
                continue
            elif station_distance(goal,stations):
                continue

            new_root_cost=0
            
            # スタート、ゴールが新駅なら先に作成
            if start not in stations:
                new_root_cost+=STATION_COST
                if not pop_flg:
                    start=list(start)
                    if goal[0]==start[0] and goal[1]>start[1]:
                        start[1]+=2
                    elif goal[0]==start[0] and goal[1]<start[1]:
                        start[1]-=2
                    elif goal[1]==start[1] and goal[0]>start[0]:
                        start[0]+=2
                    elif goal[1]==start[1] and goal[0]<start[0]:
                        start[0]-=2
                    elif goal[0]>start[0] and goal[1]>start[1]:
                        start[0]+=1
                        start[1]+=1
                    elif goal[0]>start[0] and goal[1]<start[1]:
                        start[0]+=1
                        start[1]-=1
                    elif goal[0]<start[0] and goal[1]>start[1]:
                        start[0]-=1
                        start[1]+=1
                    elif goal[0]<start[0] and goal[1]<start[1]:
                        start[0]-=1
                        start[1]-=1
                    start=tuple(start)
                    del virturl_station_group[start_group]
                    start_group=start
                    virturl_station_group[start_group]={start}
                    pop_flg=True
                while k<STATION_COST and total_tarn+tarn<t:
                    log.append([-1])
                    tarn+=1
                    k+=earn
                # print('x',tarn,k)
                if total_tarn+tarn>=t:
                    over_flg=True
                else:
                    tarn+=1
                    log.append((0,start[0],start[1]))
                    virturl_rails[start[0]][start[1]]=0
                    k-=STATION_COST
                    k+=earn
            if goal not in stations:
                goal_flg=False
            # print('a',tarn)
            if start==goal:
                earn+=calc_fee(civit[planned_site[2][-1]])
                continue
            zzz=list()
            first_state=(0,abs(start[0]-goal[0])+abs(start[1]-goal[1]),[],start)
            heapq.heappush(zzz,first_state)
            search_rails=[[virturl_rails[i][j] for j in range(n)] for i in range(n)]
            search_rails[start[0]][start[1]]=False
            while zzz:
                current_state=heapq.heappop(zzz)
                if tuple(current_state[3])==goal:
                    state=current_state
                    break
                elif goal_flg==False and current_state[1]<=2:
                    del virturl_station_group[goal_group]
                    current_state=list(current_state)
                    goal=tuple(current_state[3])
                    goal_group=goal
                    virturl_station_group[goal_group]={goal}
                    current_state[0]+=STATION_COST
                    state=current_state
                    break
                if current_state[3][0]>0 and type(search_rails[current_state[3][0]-1][current_state[3][1]])==int:  
                    if search_rails[current_state[3][0]-1][current_state[3][1]]==0:
                        search_log=current_state[2]+[[current_state[3][0]-1,current_state[3][1]]]
                        current_cost=current_state[0]
                    elif search_rails[current_state[3][0]-1][current_state[3][1]] in {1,2,3,4,5,6}:
                        search_log=current_state[2]+[[current_state[3][0]-1,current_state[3][1]]]
                        current_cost=current_state[0]+STATION_COST
                    elif search_rails[current_state[3][0]-1][current_state[3][1]]==-1:
                        search_log=current_state[2]+[[current_state[3][0]-1,current_state[3][1]]]
                        current_cost=current_state[0]+RAIL_COST
                    next_state=(current_cost,abs(current_state[3][0]-1-goal[0])+abs(current_state[3][1]-goal[1]),search_log,(current_state[3][0]-1,current_state[3][1]))
                    search_rails[current_state[3][0]-1][current_state[3][1]]=False
                    heapq.heappush(zzz,next_state)
                if current_state[3][0]<n-1 and type(search_rails[current_state[3][0]+1][current_state[3][1]])==int:
                    if search_rails[current_state[3][0]+1][current_state[3][1]]==0:
                        search_log=current_state[2]+[[current_state[3][0]+1,current_state[3][1]]]
                        current_cost=current_state[0]
                    elif search_rails[current_state[3][0]+1][current_state[3][1]] in {1,2,3,4,5,6}:
                        search_log=current_state[2]+[[current_state[3][0]+1,current_state[3][1]]]
                        current_cost=current_state[0]+STATION_COST
                    elif search_rails[current_state[3][0]+1][current_state[3][1]]==-1:
                        search_log=current_state[2]+[[current_state[3][0]+1,current_state[3][1]]]
                        current_cost=current_state[0]+RAIL_COST
                    next_state=(current_cost,abs(current_state[3][0]+1-goal[0])+abs(current_state[3][1]-goal[1]),search_log,(current_state[3][0]+1,current_state[3][1]))
                    search_rails[current_state[3][0]+1][current_state[3][1]]=False
                    heapq.heappush(zzz,next_state)
                if current_state[3][1]>0 and type(search_rails[current_state[3][0]][current_state[3][1]-1])==int:
                    if search_rails[current_state[3][0]][current_state[3][1]-1]==0:
                        search_log=current_state[2]+[[current_state[3][0],current_state[3][1]-1]]
                        current_cost=current_state[0]
                    elif search_rails[current_state[3][0]][current_state[3][1]-1] in {1,2,3,4,5,6}:
                        search_log=current_state[2]+[[current_state[3][0],current_state[3][1]-1]]
                        current_cost=current_state[0]+STATION_COST
                    elif search_rails[current_state[3][0]][current_state[3][1]-1]==-1:
                        search_log=current_state[2]+[[current_state[3][0],current_state[3][1]-1]]
                        current_cost=current_state[0]+RAIL_COST
                    next_state=(current_cost,abs(current_state[3][0]-goal[0])+abs(current_state[3][1]-1-goal[1]),search_log,(current_state[3][0],current_state[3][1]-1))
                    search_rails[current_state[3][0]][current_state[3][1]-1]=False
                    heapq.heappush(zzz,next_state)
                if current_state[3][1]<n-1 and type(search_rails[current_state[3][0]][current_state[3][1]+1])==int:
                    if search_rails[current_state[3][0]][current_state[3][1]+1]==0:
                        search_log=current_state[2]+[[current_state[3][0],current_state[3][1]+1]]
                        current_cost=current_state[0]
                    elif search_rails[current_state[3][0]][current_state[3][1]+1] in {1,2,3,4,5,6}:
                        search_log=current_state[2]+[[current_state[3][0],current_state[3][1]+1]]
                        current_cost=current_state[0]+STATION_COST
                    elif search_rails[current_state[3][0]][current_state[3][1]+1]==-1:
                        search_log=current_state[2]+[[current_state[3][0],current_state[3][1]+1]]
                        current_cost=current_state[0]+RAIL_COST
                    next_state=(current_cost,abs(current_state[3][0]-goal[0])+abs(current_state[3][1]+1-goal[1]),search_log,(current_state[3][0],current_state[3][1]+1))
                    search_rails[current_state[3][0]][current_state[3][1]+1]=False
                    heapq.heappush(zzz,next_state)
            # print('b',tarn,k)
            if len(state[2])<2:
                continue
            for i in range(len(state[2])):
                if virturl_rails[state[2][i][0]][state[2][i][1]]==0:
                    target_group=()
                    for group in virturl_station_group:
                        if  (state[2][i][0],state[2][i][1]) in virturl_station_group[group]:
                            target_group=group
                            break
                    if target_group and start_group!=target_group:
                        virturl_station_group[start_group]|=virturl_station_group[target_group]
                        del virturl_station_group[target_group]
                    continue
                elif virturl_rails[state[2][i][0]][state[2][i][1]]==-1 and goal_flg==False and i==len(state[2])-1:
                    while k<STATION_COST and tarn<t-total_tarn:
                        log.append([-1])
                        tarn+=1
                        k+=earn
                    # print(k,earn,start,goal)
                elif virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                    while k<RAIL_COST and tarn<t-total_tarn:
                        log.append([-1])
                        tarn+=1
                        k+=earn
                elif virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                    while k<STATION_COST and tarn<t-total_tarn:
                        log.append([-1])
                        k+=earn
                        tarn+=1
                if tarn>t-total_tarn:
                    over_flg=True
                    break
                if i==0:
                    if start[0]==state[2][i][0] and start[1]==state[2][i][1]+1:
                        if state[2][i][0]==state[2][i+1][0] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((1,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=1
                        elif state[2][i][0]==state[2][i+1][0] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][0]==state[2][i+1][0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((5,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=5
                        elif state[2][i][0]==state[2][i+1][0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][0]==state[2][i+1][0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((6,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=6
                        elif state[2][i][0]==state[2][i+1][0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                    elif start[0]==state[2][i][0] and start[1]==state[2][i][1]-1:
                        if state[2][i][0]==state[2][i+1][0] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((1,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=1
                        elif state[2][i][0]==state[2][i+1][0] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][0]==state[2][i+1][0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((4,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=4
                        elif state[2][i][0]==state[2][i+1][0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][0]==state[2][i+1][0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((3,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=3
                        elif state[2][i][0]==state[2][i+1][0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                    elif start[0]==state[2][i][0]-1 and start[1]==state[2][i][1]:
                        if state[2][i][1]==state[2][i+1][1] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((2,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=2
                        elif state[2][i][1]==state[2][i+1][1] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][1]==state[2][i+1][1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((4,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=4
                        elif state[2][i][1]==state[2][i+1][1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][1]==state[2][i+1][1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((5,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=5
                        elif state[2][i][1]==state[2][i+1][1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                    elif start[0]==state[2][i][0]+1 and start[1]==state[2][i][1]:
                        if state[2][i][1]==state[2][i+1][1] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((2,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=2
                        elif state[2][i][1]==state[2][i+1][1] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][1]==state[2][i+1][1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((3,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=3
                        elif state[2][i][1]==state[2][i+1][1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][1]==state[2][i+1][1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((6,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=6
                        elif state[2][i][1]==state[2][i+1][1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                elif i==len(state[2])-1:
                    if goal_flg:
                        if state[2][i-1][0]==state[2][i][0] and state[2][i-1][1]==state[2][i][1]+1:
                            if state[2][i][0]==goal[0] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((1,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=1
                            elif state[2][i][0]==goal[0] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                            elif state[2][i][0]==goal[0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((5,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=5
                            elif state[2][i][0]==goal[0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                            elif state[2][i][0]==goal[0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((6,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=6
                            elif state[2][i][0]==goal[0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i-1][0]==state[2][i][0] and state[2][i-1][1]==state[2][i][1]-1:
                            if state[2][i][0]==goal[0] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((1,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=1
                            elif state[2][i][0]==goal[0] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                            elif state[2][i][0]==goal[0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((4,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=4
                            elif state[2][i][0]==goal[0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                            elif state[2][i][0]==goal[0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((3,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=3
                            elif state[2][i][0]==goal[0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i-1][0]==state[2][i][0]-1 and state[2][i-1][1]==state[2][i][1]:
                            if state[2][i][1]==goal[1] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((2,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=2
                            elif state[2][i][1]==goal[1] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                            elif state[2][i][1]==goal[1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((4,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=4
                            elif state[2][i][1]==goal[1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                            elif state[2][i][1]==goal[1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((5,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=5
                            elif state[2][i][1]==goal[1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i-1][0]==state[2][i][0]+1 and state[2][i-1][1]==state[2][i][1]:
                            if state[2][i][1]==goal[1] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((2,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=2
                            elif state[2][i][1]==goal[1] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                            elif state[2][i][1]==goal[1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((3,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=3
                            elif state[2][i][1]==goal[1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                            elif state[2][i][1]==goal[1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                                log.append((6,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=6
                            elif state[2][i][1]==goal[1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                                log.append((0,state[2][i][0],state[2][i][1]))
                                virturl_rails[state[2][i][0]][state[2][i][1]]=0
                    else:
                        log.append((0,state[2][i][0],state[2][i][1]))
                        virturl_rails[state[2][i][0]][state[2][i][1]]=0
                else:
                    if state[2][i-1][0]==state[2][i][0] and state[2][i-1][1]==state[2][i][1]+1:
                        if state[2][i][0]==state[2][i+1][0] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((1,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=1
                        elif state[2][i][0]==state[2][i+1][0] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][0]==state[2][i+1][0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((5,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=5
                        elif state[2][i][0]==state[2][i+1][0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][0]==state[2][i+1][0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((6,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=6
                        elif state[2][i][0]==state[2][i+1][0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                    elif state[2][i-1][0]==state[2][i][0] and state[2][i-1][1]==state[2][i][1]-1:
                        if state[2][i][0]==state[2][i+1][0] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((1,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=1
                        elif state[2][i][0]==state[2][i+1][0] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][0]==state[2][i+1][0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((4,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=4
                        elif state[2][i][0]==state[2][i+1][0]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][0]==state[2][i+1][0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((3,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=3
                        elif state[2][i][0]==state[2][i+1][0]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                    elif state[2][i-1][0]==state[2][i][0]-1 and state[2][i-1][1]==state[2][i][1]:
                        if state[2][i][1]==state[2][i+1][1] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((2,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=2
                        elif state[2][i][1]==state[2][i+1][1] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][1]==state[2][i+1][1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((4,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=4
                        elif state[2][i][1]==state[2][i+1][1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][1]==state[2][i+1][1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((5,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=5
                        elif state[2][i][1]==state[2][i+1][1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                    elif state[2][i-1][0]==state[2][i][0]+1 and state[2][i-1][1]==state[2][i][1]:
                        if state[2][i][1]==state[2][i+1][1] and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((2,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=2
                        elif state[2][i][1]==state[2][i+1][1] and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][1]==state[2][i+1][1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((3,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=3
                        elif state[2][i][1]==state[2][i+1][1]+1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                        elif state[2][i][1]==state[2][i+1][1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]==-1:
                            log.append((6,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=6
                        elif state[2][i][1]==state[2][i+1][1]-1 and virturl_rails[state[2][i][0]][state[2][i][1]]!=-1:
                            log.append((0,state[2][i][0],state[2][i][1]))
                            virturl_rails[state[2][i][0]][state[2][i][1]]=0
                if log[-1][0]==0:
                    k-=STATION_COST
                    new_root_cost+=STATION_COST
                else:
                    k-=RAIL_COST
                    new_root_cost+=RAIL_COST
                k+=earn
                tarn+=1
            # print(state)
            # print('after',start,goal,new_root_cost,total_tarn,tarn,k)
            # print(start,goal,tarn,total_tarn)
            if tarn+total_tarn>t:
                over_flg=True
            if (t-total_tarn-tarn)*calc_fee(civit[planned_site[2][-1]])>new_root_cost and not over_flg:
                # print(start,goal,total_tarn,tarn,len(log),log)
                # print(k,start,goal)
                total_tarn+=tarn
                # print(civit[planned_site[2][-1]])
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
                for convine_reader in convine_readers:
                    if start_group!=convine_reader:
                        for convine_pos in virturl_station_group[convine_reader]:
                            virturl_station_group[start_group]|=virturl_station_group[convine_pos]
                    if goal_group!=convine_reader:
                        for convine_pos in virturl_station_group[convine_reader]:
                            virturl_station_group[goal_group]|=virturl_station_group[convine_pos]
                # print(convine_readers,start_group,goal_group)
                # print(virturl_station_group)
                if start_group!=goal_group:
                    for goal_pos in virturl_station_group[goal_group]:
                        virturl_station_group[start_group]|=virturl_station_group[goal_pos]
                    for goal_pos in virturl_station_group[goal_group]:
                        del virturl_station_group[goal_pos]
                # print(virturl_station_group)
                # print(virturl_station_group[start_group])
                # print(virturl_station_group[goal_group])
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
                # print(k,new_root_cost)
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
        civit.append((a,b,c,d,i))

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
        if 1<=abs(target_station[0]-station[0])+abs(target_station[1]-station[1])<=4 :
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






z=solve()
for i in z:
    print(*i)

