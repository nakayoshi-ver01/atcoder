# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
import math
# import heapq
# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in raoke(h)]
a.sort()

ans_n=n
ans_m=n

cand=0
for i in range(m):
    cand=max(cand,a[(i+1)%m]-a[i])

cand=max(cand,n-(a[-1]-a[0]))
ans_m=(n-cand)//2+(n-cand)%2

gcd=math.gcd(ans_m*360,ans_n)
if m==1:
    print('0/1')
else:
    print(f'{(ans_m*360)//gcd}/{ans_n//gcd}')