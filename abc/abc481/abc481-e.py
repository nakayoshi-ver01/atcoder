# 事前準備したモジュールは以下のサイトに公開済み
# https://atcoder.jp/contests/abc100/submissions/80089964

# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
from functools import cmp_to_key

def cmp_func(pa,pb):
    if pa[0]*pb[1]-pa[1]*pb[0]>0:
        return -1
    else:
        return 1


for _ in range(t):
    n=int(input())
    pos_side=[]
    neg_side=[]
    for i in range(n):
        x,y=map(int,input().split())
        if x>0:
            pos_side.append((x,y))
        elif x<0:
            neg_side.append((x,y))
        else:
            if y>0:
                pos_side.append((x,y))
            else:
                neg_side.append((x,y))
    pos_side.sort(key=cmp_to_key(cmp_func))
    neg_side.sort(key=cmp_to_key(cmp_func))

    cycle=[]
    for i in pos_side:
        cycle.append(i)
    for i in neg_side:
        cycle.append(i)
    
    cur=0
    ans=0
    for i in range(n):
        while cur<i+n:
            if cycle[i][0]*cycle[cur%n][1]-cycle[i][1]*cycle[cur%n][0]<0:
                break
            cur+=1
        ans=max(ans,cur-i)
    print(ans)