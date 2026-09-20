from collections import defaultdict
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

start=defaultdict(list)
end=defaultdict(list)
clothes=[]
clothes_count=defaultdict(int)
for i in range(m):
    l,r=map(int,input().split())
    clothes.append((l,r))
    clothes_count[(l,r)]+=1
clothes.sort()

for l,r in clothes:
    start[l].append(r)
    end[r].append(l)
for i in end:
    end[i].sort()

q=int(input())
for _ in range(q):
    s,t=map(int,input().split())
    if clothes_count[(s,t)]>1:
        print('Yes')
    elif clothes_count[(s,t)]==1:
        s_test=bisect.bisect_left(end[t],s+1)
        if s_test!=len(end[t]):
            print('Yes')
            continue
        t_test=bisect.bisect_left(start[s],t-1)
        if t_test!=0 or start[s][t_test]==t-1:
            print('Yes')
            continue
        print('No')
    else:
        if (s not in start) or (t not in end):
            print('No')
            continue
        s_test=bisect.bisect_left(end[t],s)
        t_test=bisect.bisect_left(start[s],t)
        if s_test==len(end[t]):
            print('No')
            continue
        elif t_test==len(start[s]):
            t_test-=1
        if s<=end[t][s_test]<=start[s][t_test]+1:
            print('Yes')
        else:
            print('No')