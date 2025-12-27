# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
h,w,d=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# マス目
grid=[list(input()) for _ in range(h)]

# 床の場所を記録
floor=list()
for i in range(h):
    for j in range(w):
        if grid[i][j]=='.':
            floor.append((i,j))

ans=0
# 1番目の加湿器
for i in range(len(floor)):
    # 2番目の加湿器
    for j in range(i+1,len(floor)):
        count=0
        one=floor[i]
        two=floor[j]
        # 全床の加湿器との距離を調べる
        for k in range(len(floor)):
            three=floor[k]
            if abs(three[0]-one[0])+abs(three[1]-one[1])<=d or abs(three[0]-two[0])+abs(three[1]-two[1])<=d:
                count+=1
        # 床面積の最大値の管理
        ans=max(count,ans)
print(ans)