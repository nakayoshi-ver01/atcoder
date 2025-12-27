# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

p=int(n**(1/2))

# 9/1=9
# 9/2=4.5
# 9/3=3
# 9/4=2.25
# 9/5=1.8
# 9/6=1.5
# 9/7=1.1
# 9/8=1.125
# 9/9=1



ans=[0]
for i in range(1,p+2):
    ans.append(n//i)

ans2=[]
for i in range(1,n//(p+1)+1):
    ans2.append(n//i)

answer=0
for i in range(p+1):
    answer+=(ans[i]-ans[i+1])*i
answer+=sum(ans2)
print(answer)