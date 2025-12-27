# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())

ost=[]
est=[]
box=[]
for i in range(n//2):
    if a[2*i]==a[2*i+1]:
        box.append(a[2*i])
    else:
        if box:
            ost.append(box)
            box=[]
if box:
    ost.append(box)
    box=[]

for i in range((n-1)//2):
    if a[1+2*i]==a[2*i+2]:
        box.append(a[1+2*i])
    else:
        if box:
            est.append(box)
            box=[]
if box:
    est.append(box)
    box=[]


ans=0
for i in range(len(ost)):
    check=set()
    cur=0
    for j in range(len(ost[i])):
        while ost[i][j] in check:
            check.remove(ost[i][cur])
            cur+=1
        check.add(ost[i][j])
        ans=max(j-cur+1,ans)

for i in range(len(est)):
    check=set()
    cur=0
    for j in range(len(est[i])):
        while est[i][j] in check:
            check.remove(est[i][cur])
            cur+=1
        check.add(est[i][j])
        ans=max(j-cur+1,ans)
print(2*ans)
