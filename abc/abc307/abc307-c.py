# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
ha,wa=map(int,input().split())
grid_a=[list(input()) for _ in range(ha)]
hb,wb=map(int,input().split())
grid_b=[list(input()) for _ in range(hb)]
hx,wx=map(int,input().split())
grid_x=[list(input()) for _ in range(hx)]
# a=list(map(int,input().split()))
# s=list(input())

min_r=20
min_c=20
max_ra=0
max_ca=0

a_sharps=set()
for i in range(ha):
    for j in range(wa):
        if grid_a[i][j]=='#':
            a_sharps.add((i,j))
            min_r=min(min_r,i)
            min_c=min(min_c,j)
            max_ra=max(max_ra,i)
            max_ca=max(max_ca,j)

moved_a_sharps=set()
for i in a_sharps:
    moved_a_sharps.add((i[0]-min_r,i[1]-min_c))

# print(moved_a_sharps)

min_r=20
min_c=20
max_rb=0
max_cb=0
b_sharps=set()
for i in range(hb):
    for j in range(wb):
        if grid_b[i][j]=='#':
            b_sharps.add((i,j))
            min_r=min(min_r,i)
            min_c=min(min_c,j)
            max_rb=max(max_rb,i)
            max_cb=max(max_cb,j)

moved_b_sharps=set()
for i in b_sharps:
    moved_b_sharps.add((i[0]-min_r,i[1]-min_c))

# print(moved_b_sharps)


min_r=20
min_c=20
x_sharps=set()
for i in range(hx):
    for j in range(wx):
        if grid_x[i][j]=='#':
            x_sharps.add((i,j))
            min_r=min(min_r,i)
            min_c=min(min_c,j)

moved_x_sharps=set()
for i in x_sharps:
    moved_x_sharps.add((i[0]-min_r,i[1]-min_c))

# print(moved_x_sharps)

flg=False
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                sharps=set()
                for sharp in moved_a_sharps:
                    sharps.add((sharp[0]+i,sharp[1]+j))
                for sharp in moved_b_sharps:
                    sharps.add((sharp[0]+k,sharp[1]+l))
                if sharps==moved_x_sharps:
                    flg=True

print('Yes' if flg else 'No')