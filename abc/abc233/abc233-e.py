# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
a=list(map(int,list(input())))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

x=sum(a)
result=x
ans=[0 for i in range(len(a)+10)]
for i in range(len(a)):
    p=x
    dig=0
    while p>0:
        ans[-i-1-dig]+=p%10
        if ans[-i-1-dig]>=10:
            ans[-i-1-dig]-=10
            ans[-i-2-dig]+=1
        dig+=1
        p//=10
    x-=a[-i-1]


flg=False
for i in range(len(ans)):
    if ans[i]!=0 and not flg:
        flg=True
        print(ans[i],end='')
    elif flg:
        print(ans[i],end='')