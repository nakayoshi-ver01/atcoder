from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

btl=defaultdict(int)
ltb=defaultdict(int)
ptb=defaultdict(int)

for i in range(1,n+1):
    btl[i]=i
    ltb[i]=i
    ptb[i]=i

for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        # 鳩がラベルの通りの場所に移動する
        ptb[query[1]]=ltb[query[2]]
    elif query[0]==2:
        # ラベルを付け替える
        ltb[query[1]],ltb[query[2]]=ltb[query[2]],ltb[query[1]]
        btl[ltb[query[1]]],btl[ltb[query[2]]]=btl[ltb[query[2]]],btl[ltb[query[1]]]
    elif query[0]==3:
        # 鳩と同じ巣にあるラベルを出力
        print(btl[ptb[query[1]]])