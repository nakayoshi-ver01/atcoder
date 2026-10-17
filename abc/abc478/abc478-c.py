# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache


front_sort_check=[True,True]  
back_sort_check=[True,True]
for i in range(1,n):
    if front_sort_check[-1] and a[i-1]<=a[i]:
        front_sort_check.append(True)
    else:
        front_sort_check.append(False)
for i in reversed(range(n-1)):
    if back_sort_check[-1] and a[i]<=a[i+1]:
        back_sort_check.append(True)
    else:
        back_sort_check.append(False)
back_sort_check.reverse()
# print(front_sort_check)
# print(back_sort_check)

acc_max=[0]
for i in range(n):
    acc_max.append(max(acc_max[-1],a[i]))
acc_min=[10**10]
for i in range(n):
    acc_min.append(min(acc_min[-1],a[-i-1]))
acc_min.append(0)
acc_min.reverse()
# print(acc_max)
# print(acc_min)

for i in range(1,n-k+2):    
    if (
        acc_max[i-1]<=acc_min[i] and 
        front_sort_check[i-1] and
        acc_max[i+k-1]<=acc_min[i+k] and 
        back_sort_check[i+k]
    ):
        print('Yes')
        break
else:
    print('No')
        
