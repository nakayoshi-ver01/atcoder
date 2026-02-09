# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
# s=list(input())
# grid=[list(input()) for _ in range(h)]
ans_set=set()
if n%2==1:
    print(a[-1])
else:
    p=a[0]+a[-1]
    for i in range(n//2):
        if p!=a[i]+a[-1-i]:
            break
    else:
        ans_set.add(p)
    
    t=a[-1]
    cur=n-1
    while a[cur]==t and cur>=0:
        cur-=1
    if cur%2==1:
        for i in range((cur+1)//2):
            if t!=a[i]+a[cur-i]:
                break
        else:
            ans_set.add(t)
    ans_list=list(ans_set)
    ans_list.sort()
    print(*ans_list)
