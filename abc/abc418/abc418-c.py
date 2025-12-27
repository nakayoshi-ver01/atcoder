# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

total=sum(a)

kind_of_value=[0 for _ in range(10**6+1)]
for i in range(n):
    kind_of_value[a[i]]+=1

acc_value=[0]
acc_kind=[0]
for i in range(1,10**6+1):
    acc_value.append(acc_value[-1]+(n-acc_kind[-1]))
    acc_kind.append(acc_kind[-1]+kind_of_value[i])

# print(kind_of_value)
# print(acc_value)
# print(acc_kind)


for _ in range(q):
    question=int(input())
    if acc_value[question-1]+1<=total:
        print(acc_value[question-1]+1)
    else:
        print(-1)