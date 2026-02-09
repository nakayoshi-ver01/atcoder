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

positive_angles = defaultdict(list)
rev_angles = []

y_positive = set()
y_negative = set()

negative_angles = defaultdict(list)
rev_negative_angles = []

for i in range(n):
    monster=list(map(int,input().split()))
    if monster[0] > 0:
        positive_angles[Fraction(monster[1],monster[0])].append(i)
        rev_angles.append(('pos',Fraction(monster[1],monster[0])))
    elif monster[0] < 0:
        negative_angles[Fraction(monster[1],monster[0])].append(i)
        rev_angles.append(('neg',Fraction(monster[1],monster[0])))
    elif monster[1] > 0:
        y_positive.add(i)
        rev_angles.append('y_pos')
    else:
        y_negative.add(i)
        rev_angles.append('y_neg')

positive_keys=list(positive_angles.keys())
negative_keys=list(negative_angles.keys())

positive_keys.sort(reverse=True)
negative_keys.sort(reverse=True)

# print(positive_keys)
# print(negative_keys)

angle_rank=defaultdict(int)

count=0
angle_acc=[0]

if y_positive:
    angle_rank['y_pos']=count
    count+=1
    angle_acc.append(angle_acc[-1]+len(y_positive))

for key in positive_keys:
    angle_rank[('pos',key)]=count
    count+=1
    angle_acc.append(angle_acc[-1]+len(positive_angles[key]))

if y_negative:
    angle_rank['y_neg']=count
    count+=1
    angle_acc.append(angle_acc[-1]+len(y_negative))

for key in negative_keys:
    angle_rank[('neg',key)]=count
    count+=1
    angle_acc.append(angle_acc[-1]+len(negative_angles[key]))

# print(angle_rank)

if y_positive:
    angle_acc.append(angle_acc[-1]+len(y_positive))

for key in positive_keys:
    angle_acc.append(angle_acc[-1]+len(positive_angles[key]))

if y_negative:
    angle_acc.append(angle_acc[-1]+len(y_negative))

for key in negative_keys:
    angle_acc.append(angle_acc[-1]+len(negative_angles[key]))

# print(angle_acc)

for _ in range(q):
    a,b=map(int,input().split())
    a-=1
    b-=1
    a_rank = angle_rank[rev_angles[a]]
    b_rank = angle_rank[rev_angles[b]]
    if a_rank <= b_rank:
        print(angle_acc[b_rank+1]-angle_acc[a_rank])
    else:
        print(angle_acc[b_rank+count+1]-angle_acc[a_rank])
