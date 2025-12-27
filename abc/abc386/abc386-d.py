from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

blackcol=defaultdict(int)
blackrow=defaultdict(int)
whitecol=defaultdict(int)
whiterow=defaultdict(int)

for _ in range(m):
    a=list(map(str,input().split()))
    if a[2]=='B':
        blackrow[int(a[0])]=max(int(a[1]),blackrow[int(a[0])])
        blackcol[int(a[1])]=max(int(a[0]),blackcol[int(a[1])])
    if a[2]=='W':
        if whiterow[int(a[0])]:
            whiterow[int(a[0])]=min(int(a[1]),whiterow[int(a[0])])
        else:
            whiterow[int(a[0])]=int(a[1])
        if whitecol[int(a[1])]:
            whitecol[int(a[1])]=min(int(a[0]),whitecol[int(a[1])])
        else:
            whitecol[int(a[1])]=int(a[0])

flg=0
rowacmax=[0]
colacmax=[0]
rowplace=list(blackrow.keys())
colplace=list(blackcol.keys())
rowplace.sort()
colplace.sort()
for i in reversed(rowplace):
    rowacmax.append(max(rowacmax[-1],blackrow[i]))
for i in reversed(colplace):
    colacmax.append(max(colacmax[-1],blackcol[i]))
rowacmax.reverse()
colacmax.reverse()
# print(rowacmax)
# print(colacmax)
# print(whiterow)
# print(rowplace)
# print(colplace)
flg=0
for i in whiterow:
    num=bisect.bisect_right(rowplace,i)
    if rowacmax[num]>=whiterow[i]:
        flg=1
        break

if flg==0:
    for i in whitecol:
        num=bisect.bisect_right(colplace,i)
        if colacmax[num]>=whitecol[i]:
            flg=1
            break

if flg==0:
    print('Yes')
else:
    print('No')