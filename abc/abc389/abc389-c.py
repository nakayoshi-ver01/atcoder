from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
q=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

line=list()
cur=0
poped=0

for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        if line:
            line.append(line[-1]+query[1])
        else:
            line.append(query[1])
    if query[0]==2:
        snake=line[cur]-poped
        poped+=snake
        cur+=1
    if query[0]==3:
        # print('ans')
        if query[1]!=1:
            print(line[query[1]-2+cur]-poped)
        else:
            print(0)
#     print('pop',poped)
# print(line)