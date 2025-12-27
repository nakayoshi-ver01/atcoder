# from collections import defaultdict,deque
# import sys
# import math
import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())

otcounter=[[0,0]for _ in range(n+1)]
srplace=[]
for i in range(n):
    if s[i]=='/':
        srplace.append(i+1)
    if s[i]=='1':
        otcounter[i+1][0]=otcounter[i][0]+1
    else:
        otcounter[i+1][0]=otcounter[i][0]
    
for i in range(n):
    if s[-i-1]=='2':
        otcounter[-i-1][1]=otcounter[-i][1]+1
    else:
        otcounter[-i-1][1]=otcounter[-i][1]

otcounter[0][1]=otcounter[1][1]
otcounter.append([otcounter[-1][0],0])

for _ in range(q):
    l,r=map(int,input().split())
    target=bisect.bisect_left(srplace,(l+r)//2)
    if len(srplace)==0:
        print(0)
    else:
        ans=0
        if target>0:
            if l<=srplace[target-1]<=r:
                ans=max(ans,(min(
                    (otcounter[srplace[target-1]][0]-otcounter[l-1][0]),
                    (otcounter[srplace[target-1]][1]-otcounter[r+1][1])
                )*2+1))
        if target<len(srplace):
            if l<=srplace[target]<=r:
                ans=max(ans,(min(
                    (otcounter[srplace[target]][0]-otcounter[l-1][0]),
                    (otcounter[srplace[target]][1]-otcounter[r+1][1])
                )*2+1))
        if target+1<len(srplace):
            if l<=srplace[target+1]<=r:
                ans=max(ans,(min(
                    (otcounter[srplace[target+1]][0]-otcounter[l-1][0]),
                    (otcounter[srplace[target+1]][1]-otcounter[r+1][1])
                )*2+1))
        print(ans)