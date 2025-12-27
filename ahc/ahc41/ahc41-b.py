from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(f.read())
with open('ahc41-1.txt','r') as f:
    
    d=map(int,f.read().split())
    print(d)
    n,m,h=map(int,f.read().split())
    a=list(map(int,f.read().split()))
    # s=list(f.read())
    # grid=[list(f.read()) for _ in range(h)]
    edges=defaultdict(set)

    for _ in range(m):
        u,v=map(int,f.read().split())
        edges[u].add(v)
        edges[v].add(u)

    for _ in range(n):
        hrhreg=list(map(int,f.read().split()))


    #　葉を調べる
    height=[-1 for _ in range(n)]

    waiting_line=deque()
    waiting_line.append((0,0))
    while waiting_line:
        now=waiting_line.popleft()
        height[now[0]]=now[1]
        for edge in edges[now[0]]:
            if height[edge]==-1:
                waiting_line.append((edge,now[1]+1))


    #　直径を調べる
    height_two=[-1 for _ in range(n)]

    farest=height.index(max(height))
    waiting_line.append((farest,0))
    while waiting_line:
        now=waiting_line.popleft()
        height_two[now[0]]=now[1]
        for edge in edges[now[0]]:
            if height_two[edge]==-1:
                waiting_line.append((edge,now[1]+1))


    diameter=max(height_two)
    center=diameter//2
    # 中心を探す
    cand_center=[]
    if diameter%2==0:
        for i in range(n):
            if height_two[i]==center:
                cand_center.append(i)
    else:
        for i in range(n):
            if height_two[i]==center or height_two[i]==center+1:
                cand_center.append(i)


    ans=0
    tree=[-1 for _ in range(n)]
    for i in cand_center:
        height_three=[-1 for _ in range(n)]
        result=0
        waiting_line.append((i,0))
        tmp_tree=[-2 for _ in range(n)]
        tmp_tree[i]=-1
        while waiting_line:
            now=waiting_line.popleft()
            height_three[now[0]]=now[1]%11
            result+=((now[1]%11)+1)*a[now[0]]
            height_two[now[0]]=now[1]
            for edge in edges[now[0]]:
                if tmp_tree[edge]==-2:
                    waiting_line.append((edge,now[1]+1))
                if now[1]%11!=10:
                    tmp_tree[edge]=now[0]
                else:
                    tmp_tree[edge]=-1
        parents=set(tmp_tree)
        for point in range(n):
            if tmp_tree[point]==-1 and point not in parents:
                print(point)
                max_height=-1
                max_point=0
                for j in edges[point]:
                    if max_height<height_three[j]<10:
                        max_height=height_three[j]
                        max_point=j
                if max_height>=0:
                    tmp_tree[point]=max_point
                    ans+=(max_height)*a[point]
                    height_three[point]=max_height+1
                    parents.add(max_point)
                else:
                    continue

        if ans<result:
            ans=result
            tree=tmp_tree[::]
            print(i,'i')
        print(i,"/////////////////////////")

    print(*tree)