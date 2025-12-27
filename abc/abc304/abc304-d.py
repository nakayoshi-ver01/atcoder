from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
w,h=map(int,input().split())
n=int(input())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

strawberries=[]
for i in range(n):
    strawberry=list(map(int,input().split()))
    strawberry.append(i)
    strawberries.append(strawberry)

strawberries.sort()
a=int(input())
yaxis=list(map(int,input().split()))
yaxis.append(w)
b=int(input())
xaxis=list(map(int,input().split()))
xaxis.append(h)

check=[[-1,-1] for _ in range(n)]

ncur=0
ycur=0
while ncur<n:
    if ycur==a:
        check[strawberries[ncur][2]][0]=ycur
        ncur+=1
    else:
        if strawberries[ncur][0]<yaxis[ycur]:
            check[strawberries[ncur][2]][0]=ycur
            ncur+=1
        else:
            ycur+=1

ncur=0
xcur=0
strawberries.sort(key=lambda x:x[1])

while ncur<n:
    if xcur==b:
        check[strawberries[ncur][2]][1]=xcur
        ncur+=1
    else:
        if strawberries[ncur][1]<xaxis[xcur]:
            check[strawberries[ncur][2]][1]=xcur
            ncur+=1
        else:
            xcur+=1

counter=defaultdict(int)

for i in range(n):
    counter[tuple(check[i])]+=1
if len(counter)<(a+1)*(b+1):
    print(0,max(counter.values()))    
else:
    print(min(counter.values()),max(counter.values()))