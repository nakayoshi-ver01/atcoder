# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]



runlen=[]
tar=''
combo=0
for i in s:
    if i!=tar:
        if tar!='':
            runlen.append((int(tar),combo))
        tar=i
        combo=1
    else:
        combo+=1

runlen.append((int(tar),combo))

# print(runlen)
ans=0
for i in range(len(runlen)-1):
    if runlen[i][0]+1==runlen[i+1][0]:
        ans+=min(runlen[i][1],runlen[i+1][1])

print(ans)