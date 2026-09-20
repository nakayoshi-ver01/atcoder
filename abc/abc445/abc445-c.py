from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

flg={i for i in range(n)}
group_num=[-1 for _ in range(n)]
loop=[]
loop_sets=[]
state=deque()
state.append(0)
temp=set()
while flg:
    if state:
        now=state.pop()
        if group_num[now]==-1:
            group_num[now]=len(loop)
        else:
            
    else:
        now=flg.pop()
        temp.add(now)