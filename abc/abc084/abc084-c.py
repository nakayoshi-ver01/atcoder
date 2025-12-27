# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
ans=[0 for i in range(n)]
schedule=[]
for i in range(n-1):
    a=list(map(int,input().split()))
    schedule.append(a)

for i in range(n-1):
    time=0
    for j in range(i,n-1):
        if time<=schedule[j][1]:
            time=schedule[j][1]
            time+=schedule[j][0]
        else:
            if time%schedule[j][2]==0:
                pass
            else:
                time=(time//schedule[j][2]+1)*schedule[j][2]
            time+=schedule[j][0]
    ans[i]=time
for i in ans:
    print(i)