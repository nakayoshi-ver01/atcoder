# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
from functools import cmp_to_key

def cmp(a, b):
    # a を前に置くべきなら負、b を前なら正
    x = a + b
    y = b + a
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

new_order=list()
cand_a=list()
cand_b=list()

for i in range(n):
    s=input()
    new_order.append((len(s),s))

new_order.sort(reverse=True)

for i in range(k):
    cand_a.append(new_order[i][1])

for i in range(k-1):
    cand_b.append(new_order[i][1])

cand_int=-1
cd=''
for i in range(k-1,n):
    if cand_int<int(new_order[i][1]):
        cand_int=int(new_order[i][1])
        cd=new_order[i][1]

cand_b.append(cd)


cand_a.sort(key=cmp_to_key(cmp))
cand_b.sort(key=cmp_to_key(cmp))

ans_a = ''.join(cand_a)
ans_b = ''.join(cand_b)

def norm(s):
    t = s.lstrip('0')
    return t if t else '0'

a = norm(ans_a)
b = norm(ans_b)
if len(a) != len(b):
    print(a if len(a) > len(b) else b)
else:
    print(a if a >= b else b)

