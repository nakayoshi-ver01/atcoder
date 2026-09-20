# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

for _ in range(t):
    n=int(input())
    products=[]
    min_a=10**10
    # 確定でかかる料金
    base=0
    for _ in range(n):
        product=list(map(int,input().split()))
        products.append(product[1]-product[0])
        base+=product[0]
        min_a=min(min_a,product[0])
    products.sort()
    ans=base
    cur=base
    for i in range(1,n+1):
        # bの料金に切り替え
        cur+=products[i-1]
        # 割引が多い方からi件クーポンを使うか否か
        # 足りないクーポンはaが最も小さいものを使う
        ans=min(ans,cur+max(0,2*i-n)*min_a)
    print(ans)