# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
p=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

waves=[]
for i in range(n-1):
    if p[i]>p[i+1]:
        waves.append('>')
    else:
        waves.append('<')

runlen=[]
counter=[1,waves[0]]
for i in range(1,n-1):
    if waves[i]!=counter[1]:
        runlen.append(counter)
        counter=[1,waves[i]]
    else:
        counter[0]+=1
runlen.append(counter)
# print(runlen)
ans=0
for i in range(1,len(runlen)-1):
    if runlen[i][1]=='>':
        ans+=runlen[i-1][0]*runlen[i+1][0]
print(ans)