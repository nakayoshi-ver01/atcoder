from collections import defaultdict,deque
from fractions import Fraction
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

# 角度ごとにモンスターをまとめる
monster_angles = defaultdict(list)
# 角度の逆引き配列
rev_monster_angles = []
for i in range(n):
    monster=list(map(int,input().split()))
    f = Fraction(monster[1],monster[0])
    monster_angles[math.atan(f)].append(i)
    rev_monster_angles.append(math.atan(f))
monster_keys=list(monster_angles.keys())

monster_keys.sort(reverse=True)
angle_acc=[0]
for key in monster_keys:
    angle_acc.append(angle_acc[-1]+len(monster_angles[key]))

for key in monster_keys:
    angle_acc.append(angle_acc[-1]+len(monster_angles[key]))

# 角度の順番を管理
angle_rank=defaultdict(int)
for i in range(len(monster_keys)):
    angle_rank[monster_keys[i]]=i

print(angle_rank)


for _ in range(q):
    a,b=map(int,input().split())
    a-=1
    b-=1
    a_rank = angle_rank[rev_monster_angles[a]]
    b_rank = angle_rank[rev_monster_angles[b]]
    if a_rank <= b_rank:
        print(angle_acc[b_rank+1]-angle_acc[a_rank])
    else:
        print(angle_acc[b_rank+len(monster_keys)+1]-angle_acc[a_rank])
