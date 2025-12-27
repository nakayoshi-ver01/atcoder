# from collections import defaultdict,deque
from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]
one=list()
for i in range(n):
    if s[i]=='1':
        one.append(i)



if len(one)%2==1:
    pivot=len(one)//2
    ans=0
    for i in range(pivot):
        ans+=one[pivot]-one[i]-(pivot-i)
    for i in range(pivot+1,len(one)):
        ans+=one[i]-one[pivot]-(i-pivot)
    print(ans)
else:
    lpivot=len(one)//2-1
    lans=0
    rpivot=len(one)//2
    rans=0
    for i in range(lpivot):
        lans+=one[lpivot]-one[i]-(lpivot-i)
    for i in range(lpivot+1,len(one)):
        lans+=one[i]-one[lpivot]-(i-lpivot)
    for i in range(rpivot):
        rans+=one[rpivot]-one[i]-(rpivot-i)
    for i in range(rpivot+1,len(one)):
        rans+=one[i]-one[rpivot]-(i-rpivot)
    print(min(lans,rans))