# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
move=[0 for _ in range(n)]
ans=[0 for _ in range(n)]
flg=0
for i in range(n):
    flg+=move[i]
    if a[i]+i-(n-i-1)-flg<0:
        target=a[i]+i-(n-i-1)-flg
        move[target]+=1
    ans[i]=max(0,a[i]+i-(n-i-1)-flg)
print(*ans)