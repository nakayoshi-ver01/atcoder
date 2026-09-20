from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

counter=[0 for i in range(m+1)]

for i in range(n):
    counter[a[i]]+=1

num_of_number=defaultdict(list)
for i in range(1,m+1):
    num_of_number[counter[i]].append(i)
print(num_of_number)
counter_keys=list(num_of_number.keys())

max_try=max(counter_keys)

try_num=[0]
try_num_next=[0]
for i in range(max_try+1):
    try_num.append(try_num[-1]+len(num_of_number[i]))
    try_num_next.append(try_num_next[-1]+try_num[-1])

print(try_num)
print(try_num_next)
q=int(input())
for _ in range(q):
    x=int(input())
