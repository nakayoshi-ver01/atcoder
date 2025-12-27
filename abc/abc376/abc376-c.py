# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
# s=list(input())
flg=0
point=-1
for i in range(1,n):
    if flg==0:
        if a[-i]>b[-i]:
            flg+=1
            point=i
    if flg==1:
        flg+=1
        point=a[-i]
    if flg==2:
        if a[-i-1]>b[-i]:
            flg+=1
            point=i
    if flg==3:
        print(-1)
        break
else:
    if point==-1:
        print(a[0])
    else:
        print(point)