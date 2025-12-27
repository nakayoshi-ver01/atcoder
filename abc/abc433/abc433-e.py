from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    n,m=map(int,input().split())
    num_lis=[[-1,-1] for _ in range(n*m+1)]
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    no_flg=False
    for i in range(n):
        if num_lis[x[i]][0]==-1:
            num_lis[x[i]][0]=i
        else:
            no_flg=True
            break
    for i in range(m):
        if num_lis[y[i]][1]==-1:
            num_lis[y[i]][1]=i
        else:
            no_flg=True
            break
    if no_flg:
        print('No')
        continue
    a=[[-1 for _ in range(m)] for _ in range(n)]
    x_ok =set()
    x_count=defaultdict(int)
    y_ok =set()
    y_count=defaultdict(int)
    cross_ok = set()
    for i in reversed(range(1,n*m+1)):
        if num_lis[i][0]!=-1 and num_lis[i][1]!=-1:
            a[num_lis[i][0]][num_lis[i][1]]=i
            x_ok.add(num_lis[i][0])
            y_ok.add(num_lis[i][1])
            x_count[num_lis[i][0]]+=1
            y_count[num_lis[i][1]]+=1
            if x_count[num_lis[i][0]]>=m:
                x_ok.remove(num_lis[i][0])
            if y_count[num_lis[i][1]]>=n:
                y_ok.remove(num_lis[i][1])
            for x_axis in x_ok:
                if a[x_axis][num_lis[i][1]]==-1:
                    cross_ok.add((x_axis,num_lis[i][1]))
            for y_axis in y_ok:
                if a[num_lis[i][0]][y_axis]==-1:
                    cross_ok.add((num_lis[i][0],y_axis))

        elif num_lis[i][1]!=-1:
            if x_ok:
                k=x_ok.pop()
            else:
                no_flg=True
                break
            a[k][num_lis[i][1]]=i
            y_ok.add(num_lis[i][1])
            x_count[k]+=1
            y_count[num_lis[i][1]]+=1
            if x_count[k]<m:
                x_ok.add(k)
            if y_count[num_lis[i][1]]>=n:
                y_ok.remove(num_lis[i][1])
            for x_axis in x_ok:
                if a[x_axis][num_lis[i][1]]==-1:
                    cross_ok.add((x_axis,num_lis[i][1]))
        elif num_lis[i][0]!=-1:
            if y_ok:
                l=y_ok.pop()
            else:
                no_flg=True
                break            
            a[num_lis[i][0]][l]=i
            x_ok.add(num_lis[i][0])
            x_count[num_lis[i][0]]+=1
            y_count[l]+=1
            if x_count[num_lis[i][0]]>=m:
                x_ok.remove(num_lis[i][0])
            if y_count[l]<n:
                y_ok.add(l)
            for y_axis in y_ok:
                if a[num_lis[i][0]][y_axis]==-1:
                    cross_ok.add((num_lis[i][0],y_axis))
        else:
            if cross_ok:
                rand=cross_ok.pop()
            else:
                no_flg=True
                break
            a[rand[0]][rand[1]]=i
            x_count[rand[0]]+=1
            y_count[rand[1]]+=1
            if x_count[rand[0]]>=m:
                x_ok.remove(rand[0])
            if y_count[rand[1]]>=n:
                y_ok.remove(rand[1])

    if no_flg:
        print('No')
        continue
    else:
        print('Yes')
        for i in a:
            print(*i)    