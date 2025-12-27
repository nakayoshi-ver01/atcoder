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
    
    af=set()
    counter=0
    commuter_count=0
    next_place=SortedList()
    af_civit=[True for _ in range(m)]
    for i in range(2,len(start_station)):
        next_place.add((start_station[i][0],start_station[1],start_station[i]))
        af_civit[start_station[i][-1]]=False
    while total_tarn<t:
        log_1=[]
        log_2=[]
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
                if start[1]>goal[1]:
                    (
                        virturl_rails_1,
                        tarn_1,
                        log_1,
                        earn_1,
                        over_flg_1,
                        new_stations_1,
                        k_1,
                        new_root_cost_1,
                        stop_flg_1,
                        convine_readers_1
                    )=vartical_move(
                        goal[1]+1,
                        start[1],
                        start[0],
                        1,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        goal_group,
                        start_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    (
                        virturl_rails_2,
                        tarn_2,
                        log_2,
                        earn_2,
                        over_flg_2,
                        new_stations_2,
                        k_2,
                        new_root_cost_2,
                        stop_flg_2,
                        convine_readers_2
                    )=reverse_vartical_move(
                        goal[1]+1,
                        start[1],
                        start[0],
                        1,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        goal_group,
                        start_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                else:
                    (
                        virturl_rails_1,
                        tarn_1,
                        log_1,
                        earn_1,
                        over_flg_1,
                        new_stations_1,
                        k_1,
                        new_root_cost_1,
                        stop_flg_1,
                        convine_readers_1
                    )=vartical_move(
                        start[1]+1,
                        goal[1],
                        start[0],
                        1,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    (
                        virturl_rails_2,
                        tarn_2,
                        log_2,
                        earn_2,
                        over_flg_2,
                        new_stations_2,
                        k_2,
                        new_root_cost_2,
                        stop_flg_2,
                        convine_readers_2
                    )=reverse_vartical_move(
                        start[1]+1,
                        goal[1],
                        start[0],
                        1,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
            elif start[1]==goal[1]:
                if start[0]>goal[0]:
                    (
                        virturl_rails_1,
                        tarn_1,
                        log_1,
                        earn_1,
                        over_flg_1,
                        new_stations_1,
                        k_1,
                        new_root_cost_1,
                        stop_flg_1,
                        convine_readers_1
                    )=horizonal_move(
                        goal[0]+1,
                        start[0],
                        start[1],
                        2,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        goal_group,
                        start_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    (
                        virturl_rails_2,
                        tarn_2,
                        log_2,
                        earn_2,
                        over_flg_2,
                        new_stations_2,
                        k_2,
                        new_root_cost_2,
                        stop_flg_2,
                        convine_readers_2
                    )=reverse_horizonal_move(
                        goal[0]+1,
                        start[0],
                        start[1],
                        2,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        goal_group,
                        start_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                else:
                    (
                        virturl_rails_1,
                        tarn_1,
                        log_1,
                        earn_1,
                        over_flg_1,
                        new_stations_1,
                        k_1,
                        new_root_cost_1,
                        stop_flg_1,
                        convine_readers_1
                    )=horizonal_move(
                        start[0]+1,
                        goal[0],
                        start[1],
                        2,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    (
                        virturl_rails_2,
                        tarn_2,
                        log_2,
                        earn_2,
                        over_flg_2,
                        new_stations_2,
                        k_2,
                        new_root_cost_2,
                        stop_flg_2,
                        convine_readers_2
                    )=reverse_horizonal_move(
                        start[0]+1,
                        goal[0],
                        start[1],
                        2,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
            
            elif (start[0]-goal[0])*(start[1]-goal[1])>0:
                if start[0]<goal[0]:
                    (
                        virturl_rails_1,
                        tarn_1,
                        log_1,
                        earn_1,
                        over_flg_1,
                        new_stations_1,
                        k_1,
                        new_root_cost_1,
                        stop_flg_1,
                        convine_readers_1
                    )=vartical_move(
                        start[1]+1,
                        goal[1],
                        start[0],
                        1,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    if not stop_flg_1:
                        (
                            virturl_rails_1,
                            tarn_1,
                            log_1,
                            k_1,
                            earn_1,
                            new_stations_1,
                            convine_readers_1,
                            over_flg_1,
                            stop_flg_1,
                            new_root_cost_1
                        )=corner_move(
                            virturl_rails_1,
                            (start[0],goal[1]),
                            total_tarn,
                            tarn_1,
                            log_1,
                            k_1,
                            earn_1,
                            new_stations_1,
                            virturl_station_group,
                            convine_readers_1,
                            3,
                            start_group,
                            goal_group,
                            new_root_cost_1
                        )
                        if not stop_flg_1:
                            (
                                virturl_rails_1,
                                tarn_1,
                                log_1,
                                earn_1,
                                over_flg_1,
                                new_stations_1,
                                k_1,
                                new_root_cost_1,
                                stop_flg_1,
                                convine_readers_1
                            )=horizonal_move(
                                start[0]+1,
                                goal[0],
                                goal[1],
                                2,
                                virturl_rails_1,
                                total_tarn,
                                tarn_1,
                                log_1,
                                earn_1,
                                over_flg_1,
                                virturl_station_group,
                                start_group,
                                goal_group,
                                new_stations_1,
                                k_1,
                                new_root_cost_1,
                                convine_readers_1
                            )
                    (
                        virturl_rails_2,
                        tarn_2,
                        log_2,
                        earn_2,
                        over_flg_2,
                        new_stations_2,
                        k_2,
                        new_root_cost_2,
                        stop_flg_2,
                        convine_readers_2
                    )=reverse_horizonal_move(
                        start[0]+1,
                        goal[0],
                        goal[1],
                        2,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    if not stop_flg_2:
                        (
                            virturl_rails_2,
                            tarn_2,
                            log_2,
                            k_2,
                            earn_2,
                            new_stations_2,
                            convine_readers_2,
                            over_flg_2,
                            stop_flg_2,
                            new_root_cost_2
                        )=corner_move(
                            virturl_rails_2,
                            (goal[0],start[1]),
                            total_tarn,
                            tarn_2,
                            log_2,
                            k_2,
                            earn_2,
                            new_stations_2,
                            virturl_station_group,
                            convine_readers_2,
                            3,
                            start_group,
                            goal_group,
                            new_root_cost_2
                        )
                        if not stop_flg_2:
                            (
                                virturl_rails_2,
                                tarn_2,
                                log_2,
                                earn_2,
                                over_flg_2,
                                new_stations_2,
                                k_2,
                                new_root_cost_2,
                                stop_flg_2,
                                convine_readers_2
                            )=reverse_vartical_move(
                                start[1]+1,
                                goal[1],
                                start[0],
                                1,
                                virturl_rails_2,
                                total_tarn,
                                tarn_2,
                                log_2,
                                earn_2,
                                over_flg_2,
                                virturl_station_group,
                                start_group,
                                goal_group,
                                new_stations_2,
                                k_2,
                                new_root_cost_2,
                                convine_readers_2
                            )
                else:
                    (
                        virturl_rails_1,
                        tarn_1,
                        log_1,
                        earn_1,
                        over_flg_1,
                        new_stations_1,
                        k_1,
                        new_root_cost_1,
                        stop_flg_1,
                        convine_readers_1
                    )=vartical_move(
                        goal[1]+1,
                        start[1],
                        goal[0],
                        1,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    if not stop_flg_1:
                        (
                            virturl_rails_1,
                            tarn_1,
                            log_1,
                            k_1,
                            earn_1,
                            new_stations_1,
                            convine_readers_1,
                            over_flg_1,
                            stop_flg_1,
                            new_root_cost_1
                        )=corner_move(
                            virturl_rails_1,
                            (goal[0],start[1]),
                            total_tarn,
                            tarn_1,
                            log_1,
                            k_1,
                            earn_1,
                            new_stations_1,
                            virturl_station_group,
                            convine_readers_1,
                            3,
                            start_group,
                            goal_group,
                            new_root_cost_1
                        )
                        if not stop_flg_1:
                            (
                                virturl_rails_1,
                                tarn_1,
                                log_1,
                                earn_1,
                                over_flg_1,
                                new_stations_1,
                                k_1,
                                new_root_cost_1,
                                stop_flg_1,
                                convine_readers_1
                            )=horizonal_move(
                                goal[0]+1,
                                start[0],
                                start[1],
                                2,
                                virturl_rails_1,
                                total_tarn,
                                tarn_1,
                                log_1,
                                earn_1,
                                over_flg_1,
                                virturl_station_group,
                                start_group,
                                goal_group,
                                new_stations_1,
                                k_1,
                                new_root_cost_1,
                                convine_readers_1
                            )
                    (
                        virturl_rails_2,
                        tarn_2,
                        log_2,
                        earn_2,
                        over_flg_2,
                        new_stations_2,
                        k_2,
                        new_root_cost_2,
                        stop_flg_2,
                        convine_readers_2
                    )=reverse_horizonal_move(
                        goal[0]+1,
                        start[0],
                        start[1],
                        2,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    if not stop_flg_2:
                        (
                            virturl_rails_2,
                            tarn_2,
                            log_2,
                            k_2,
                            earn_2,
                            new_stations_2,
                            convine_readers_2,
                            over_flg_2,
                            stop_flg_2,
                            new_root_cost_2
                        )=corner_move(
                            virturl_rails_2,
                            (goal[0],start[1]),
                            total_tarn,
                            tarn_2,
                            log_2,
                            k_2,
                            earn_2,
                            new_stations_2,
                            virturl_station_group,
                            convine_readers_2,
                            3,
                            start_group,
                            goal_group,
                            new_root_cost_2
                        )
                        if not stop_flg_2:
                            (
                                virturl_rails_2,
                                tarn_2,
                                log_2,
                                earn_2,
                                over_flg_2,
                                new_stations_2,
                                k_2,
                                new_root_cost_2,
                                stop_flg_2,
                                convine_readers_2
                            )=reverse_vartical_move(
                                goal[1]+1,
                                start[1],
                                goal[0],
                                1,
                                virturl_rails_2,
                                total_tarn,
                                tarn_2,
                                log_2,
                                earn_2,
                                over_flg_2,
                                virturl_station_group,
                                start_group,
                                goal_group,
                                new_stations_2,
                                k_2,
                                new_root_cost_2,
                                convine_readers_2
                            )
            elif (start[0]-goal[0])*(start[1]-goal[1])<0:
                if start[1]>goal[1]:
                    (
                        virturl_rails_1,
                        tarn_1,
                        log_1,
                        earn_1,
                        over_flg_1,
                        new_stations_1,
                        k_1,
                        new_root_cost_1,
                        stop_flg_1,
                        convine_readers_1
                    )=reverse_vartical_move(
                        goal[1]+1,
                        start[1],
                        start[0],
                        1,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    if not stop_flg_1:
                        (
                            virturl_rails_1,
                            tarn_1,
                            log_1,
                            k_1,
                            earn_1,
                            new_stations_1,
                            convine_readers_1,
                            over_flg_1,
                            stop_flg_1,
                            new_root_cost_1
                        )=corner_move(
                            virturl_rails_1,
                            (start[0],goal[1]),
                            total_tarn,
                            tarn_1,
                            log_1,
                            k_1,
                            earn_1,
                            new_stations_1,
                            virturl_station_group,
                            convine_readers_1,
                            6,
                            start_group,
                            goal_group,
                            new_root_cost_1
                        )
                        if stop_flg_1:
                            (
                                virturl_rails_1,
                                tarn_1,
                                log_1,
                                earn_1,
                                over_flg_1,
                                new_stations_1,
                                k_1,
                                new_root_cost_1,
                                stop_flg_1,
                                convine_readers_1
                            )=reverse_horizonal_move(
                                start[0]+1,
                                goal[0],
                                goal[1],
                                2,
                                virturl_rails_1,
                                total_tarn,
                                tarn_1,
                                log_1,
                                earn_1,
                                over_flg_1,
                                virturl_station_group,
                                start_group,
                                goal_group,
                                new_stations_1,
                                k_1,
                                new_root_cost_1,
                                convine_readers_1
                            )
                    (
                        virturl_rails_2,
                        tarn_2,
                        log_2,
                        earn_2,
                        over_flg_2,
                        new_stations_2,
                        k_2,
                        new_root_cost_2,
                        stop_flg_2,
                        convine_readers_2
                    )=reverse_horizonal_move(
                        start[0]+1,
                        goal[0],
                        goal[1],
                        2,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    if not stop_flg_2:
                        (
                            virturl_rails_2,
                            tarn_2,
                            log_2,
                            k_2,
                            earn_2,
                            new_stations_2,
                            convine_readers_2,
                            over_flg_2,
                            stop_flg_2,
                            new_root_cost_2
                        )=corner_move(
                            virturl_rails_2,
                            (start[0],goal[1]),
                            total_tarn,
                            tarn_2,
                            log_2,
                            k_2,
                            earn_2,
                            new_stations_2,
                            virturl_station_group,
                            convine_readers_2,
                            6,
                            start_group,
                            goal_group,
                            new_root_cost_2
                        )
                        if stop_flg_2:
                            (
                                virturl_rails_2,
                                tarn_2,
                                log_2,
                                earn_2,
                                over_flg_2,
                                new_stations_2,
                                k_2,
                                new_root_cost_2,
                                stop_flg_2,
                                convine_readers_2
                            )=vartical_move(
                                goal[1]+1,
                                start[1],
                                start[0],
                                1,
                                virturl_rails_2,
                                total_tarn,
                                tarn_2,
                                log_2,
                                earn_2,
                                over_flg_2,
                                virturl_station_group,
                                start_group,
                                goal_group,
                                new_stations_2,
                                k_2,
                                new_root_cost_2,
                                convine_readers_2
                            )
                else:
                    (
                        virturl_rails_1,
                        tarn_1,
                        log_1,
                        earn_1,
                        over_flg_1,
                        new_stations_1,
                        k_1,
                        new_root_cost_1,
                        stop_flg_1,
                        convine_readers_1
                    )=reverse_vartical_move(
                        start[1]+1,
                        goal[1],
                        goal[0],
                        1,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    if not stop_flg_1:
                        (
                            virturl_rails_1,
                            tarn_1,
                            log_1,
                            k_1,
                            earn_1,
                            new_stations_1,
                            convine_readers_1,
                            over_flg_1,
                            stop_flg_1,
                            new_root_cost_1
                        )=corner_move(
                            virturl_rails_1,
                            (goal[0],start[1]),
                            total_tarn,
                            tarn_1,
                            log_1,
                            k_1,
                            earn_1,
                            new_stations_1,
                            virturl_station_group,
                            convine_readers_1,
                            6,
                            start_group,
                            goal_group,
                            new_root_cost_1
                        )
                        if stop_flg_1:
                            (
                                virturl_rails_1,
                                tarn_1,
                                log_1,
                                earn_1,
                                over_flg_1,
                                new_stations_1,
                                k_1,
                                new_root_cost_1,
                                stop_flg_1,
                                convine_readers_1
                            )=reverse_horizonal_move(
                                goal[0]+1,
                                start[0],
                                start[1],
                                2,
                                virturl_rails_1,
                                total_tarn,
                                tarn_1,
                                log_1,
                                earn_1,
                                over_flg_1,
                                virturl_station_group,
                                start_group,
                                goal_group,
                                new_stations_1,
                                k_1,
                                new_root_cost_1,
                                convine_readers_1
                            )
                    (
                        virturl_rails_2,
                        tarn_2,
                        log_2,
                        earn_2,
                        over_flg_2,
                        new_stations_2,
                        k_2,
                        new_root_cost_2,
                        stop_flg_2,
                        convine_readers_2
                    )=reverse_horizonal_move(
                        goal[0]+1,
                        start[0],
                        start[1],
                        2,
                        virturl_rails,
                        total_tarn,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        virturl_station_group,
                        start_group,
                        goal_group,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )
                    if not stop_flg_2:
                        (
                            virturl_rails_2,
                            tarn_2,
                            log_2,
                            k_2,
                            earn_2,
                            new_stations_2,
                            convine_readers_2,
                            over_flg_2,
                            stop_flg_2,
                            new_root_cost_2
                        )=corner_move(
                            virturl_rails_2,
                            (goal[0],start[1]),
                            total_tarn,
                            tarn_2,
                            log_2,
                            k_2,
                            earn_2,
                            new_stations_2,
                            virturl_station_group,
                            convine_readers_2,
                            6,
                            start_group,
                            goal_group,
                            new_root_cost_2
                        )
                        if stop_flg_2:
                            (
                                virturl_rails_2,
                                tarn_2,
                                log_2,
                                earn_2,
                                over_flg_2,
                                new_stations_2,
                                k_2,
                                new_root_cost_2,
                                stop_flg_2,
                                convine_readers_2
                            )=vartical_move(
                                start[1]+1,
                                goal[1],
                                goal[0],
                                1,
                                virturl_rails_2,
                                total_tarn,
                                tarn_2,
                                log_2,
                                earn_2,
                                over_flg_2,
                                virturl_station_group,
                                start_group,
                                goal_group,
                                new_stations_2,
                                k_2,
                                new_root_cost_2,
                                convine_readers_2
                            )
                
            if log_1:
                if len(log_1)<len(log_2):
                    (
                        virturl_rails,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )=(
                        virturl_rails_1,
                        tarn_1,
                        log_1,
                        earn_1,
                        over_flg_1,
                        new_stations_1,
                        k_1,
                        new_root_cost_1,
                        convine_readers_1
                    )
                else:
                    (
                        virturl_rails,
                        tarn,
                        log,
                        earn,
                        over_flg,
                        new_stations,
                        k,
                        new_root_cost,
                        convine_readers
                    )=(
                        virturl_rails_2,
                        tarn_2,
                        log_2,
                        earn_2,
                        over_flg_2,
                        new_stations_2,
                        k_2,
                        new_root_cost_2,
                        convine_readers_2
                    )
            if (t-total_tarn-tarn)*calc_fee(civit[planned_site[2][-1]])>new_root_cost and not over_flg:
                print(start,goal,total_tarn,tarn,len(log),log)
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



def vartical_move(
        start_pos,
        goal_pos,
        height,
        rail_type,
        virturl_rails,
        total_tarn,
        tarn,
        log,
        earn,
        over_flg,
        virturl_station_group,
        start_group,
        goal_group,
        new_stations,
        k,
        new_root_cost,
        convine_readers
    ):
    RAIL_COST=100
    STATION_COST=5000
    t=800
    stop_flg=False

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
            convine_reader=search_station_group(
                virturl_rails,
                virturl_station_group,
                (height,i)
            )
            if start_group!=convine_reader and goal_group==convine_reader:
                stop_flg=True
                break
            if start_group==convine_reader and goal_group!=convine_reader:
                stop_flg=True
                break
        elif virturl_rails[height][i]==0:
            convine_reader=search_station_group(
                virturl_rails,
                virturl_station_group,
                (height,i)
            )
            convine_readers.add(convine_reader)
            if start_group!=convine_reader and goal_group==convine_reader:
                stop_flg=True
                break
            if start_group==convine_reader and goal_group!=convine_reader:
                stop_flg=True
                break
    return (
        virturl_rails,
        tarn,
        log,
        earn,
        over_flg,
        new_stations,
        k,
        new_root_cost,
        stop_flg,
        convine_readers
    )

def reverse_vartical_move(
        start_pos,
        goal_pos,
        height,
        rail_type,
        virturl_rails,
        total_tarn,
        tarn,
        log,
        earn,
        over_flg,
        virturl_station_group,
        start_group,
        goal_group,
        new_stations,
        k,
        new_root_cost,
        convine_readers
    ):
    RAIL_COST=100
    STATION_COST=5000
    t=800
    stop_flg=False

    for i in reversed(range(start_pos,goal_pos)):
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
            convine_reader=search_station_group(
                virturl_rails,
                virturl_station_group,
                (height,i)
            )
            if start_group!=convine_reader and goal_group==convine_reader:
                stop_flg=True
                break
            if start_group==convine_reader and goal_group!=convine_reader:
                stop_flg=True
                break
        elif virturl_rails[height][i]==0:
            convine_reader=search_station_group(
                virturl_rails,
                virturl_station_group,
                (height,i)
            )
            convine_readers.add(convine_reader)
            if start_group!=convine_reader and goal_group==convine_reader:
                stop_flg=True
                break
            if start_group==convine_reader and goal_group!=convine_reader:
                stop_flg=True
                break
    return (
        virturl_rails,
        tarn,
        log,
        earn,
        over_flg,
        new_stations,
        k,
        new_root_cost,
        stop_flg,
        convine_readers
    )


def horizonal_move(
        start_pos,
        goal_pos,
        col,
        rail_type,
        virturl_rails,
        total_tarn,
        tarn,
        log,
        earn,
        over_flg,
        virturl_station_group,
        start_group,
        goal_group,
        new_stations,
        k,
        new_root_cost,
        convine_readers
    ):
    RAIL_COST=100
    STATION_COST=5000
    t=800
    stop_flg=False

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
            convine_reader=search_station_group(
                virturl_rails,
                virturl_station_group,
                (i,col)
            )
            convine_readers.add(convine_reader)
            if start_group!=convine_reader and goal_group==convine_reader:
                stop_flg=True
                break
            if start_group==convine_reader and goal_group!=convine_reader:
                stop_flg=True
                break

        if virturl_rails[i][col]==0:
            convine_reader=search_station_group(
                virturl_rails,
                virturl_station_group,
                (i,col)
            )
            convine_readers.add(convine_reader)
            if start_group!=convine_reader and goal_group==convine_reader:
                stop_flg=True
                break
            if start_group==convine_reader and goal_group!=convine_reader:
                stop_flg=True
                break


    return (
        virturl_rails,
        tarn,
        log,
        earn,
        over_flg,
        new_stations,
        k,
        new_root_cost,
        stop_flg,
        convine_readers
    )

def reverse_horizonal_move(
        start_pos,
        goal_pos,
        col,
        rail_type,
        virturl_rails,
        total_tarn,
        tarn,
        log,
        earn,
        over_flg,
        virturl_station_group,
        start_group,
        goal_group,
        new_stations,
        k,
        new_root_cost,
        convine_readers
    ):
    RAIL_COST=100
    STATION_COST=5000
    t=800
    stop_flg=False

    for i in reversed(range(start_pos,goal_pos)):
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
            convine_reader=search_station_group(
                virturl_rails,
                virturl_station_group,
                (i,col)
            )
            convine_readers.add(convine_reader)
            if start_group!=convine_reader and goal_group==convine_reader:
                stop_flg=True
                break
            if start_group==convine_reader and goal_group!=convine_reader:
                stop_flg=True
                break
        elif virturl_rails[i][col]==0:
            convine_reader=search_station_group(
                virturl_rails,
                virturl_station_group,
                (i,col)
            )
            convine_readers.add(convine_reader)
            if start_group!=convine_reader and goal_group==convine_reader:
                stop_flg=True
                break
            if start_group==convine_reader and goal_group!=convine_reader:
                stop_flg=True
                break


    return (
        virturl_rails,
        tarn,
        log,
        earn,
        over_flg,
        new_stations,
        k,
        new_root_cost,
        stop_flg,
        convine_readers
    )

def corner_move(
    virturl_rails,
    corner_pos,
    total_tarn,
    tarn,
    log,
    k,
    earn,
    new_stations,
    virturl_station_group,
    convine_readers,
    rail_type,
    start_group,
    goal_group,
    new_root_cost
):
    RAIL_COST=100
    STATION_COST=5000
    t=800
    over_flg=False
    stop_flg=False
    if virturl_rails[corner_pos[0]][corner_pos[1]]==-1:
        while k<RAIL_COST and total_tarn+tarn<t:
            log.append([-1])
            tarn+=1
            k+=earn
        if total_tarn+tarn>=t:
            over_flg=True
        k-=RAIL_COST
        new_root_cost+=RAIL_COST
        tarn+=1
        virturl_rails[corner_pos[0]][corner_pos[1]]=rail_type
        log.append((rail_type,corner_pos[0],corner_pos[1]))
        k+=earn
    elif virturl_rails[corner_pos[0]][corner_pos[1]] not in {0,rail_type}:
        while k<STATION_COST and total_tarn+tarn<t:
            log.append([-1])
            tarn+=1
            k+=earn
        if total_tarn+tarn>=t:
            over_flg=True
        k-=STATION_COST
        new_root_cost+=STATION_COST
        tarn+=1
        virturl_rails[corner_pos[0]][corner_pos[1]]=0
        new_stations.add((corner_pos[0],corner_pos[1]))
        log.append((0,corner_pos[0],corner_pos[1]))
        k+=earn
        convine_reader=search_station_group(
            virturl_rails,
            virturl_station_group,
            corner_pos
        )
        convine_readers.add(convine_reader)
        if start_group!=convine_reader and goal_group==convine_reader:
            stop_flg=True
        if start_group==convine_reader and goal_group!=convine_reader:
            stop_flg=True 
        if total_tarn+tarn>=t:
            over_flg=True
    elif virturl_rails[corner_pos[0]][corner_pos[1]]==0:
        convine_reader=search_station_group(
            virturl_rails,
            virturl_station_group,
            corner_pos
        )
        convine_readers.add(convine_reader)
        if start_group!=convine_reader and goal_group==convine_reader:
            stop_flg=True
        if start_group==convine_reader and goal_group!=convine_reader:
            stop_flg=True
    return (
        virturl_rails,
        tarn,
        log,
        k,
        earn,
        new_stations,
        convine_readers,
        over_flg,
        stop_flg,
        new_root_cost
    )


z=solve()
for i in z:
    print(*i)

