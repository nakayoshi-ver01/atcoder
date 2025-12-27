from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# a=[(i%2)+1 for i in range(n)]
# s=list(input())
# grid=[list(input()) for _ in range(h)]
heights=defaultdict(set)
for i in range(n):
    heights[a[i]].add(i)
ans=1
ansset=set()
for i in heights:
    now=0
    for j in heights[i]:
        now+=1
        for k in range(1,max(heights[i])-j):
            combo=1
            cur=j
            f={j}
            if (j not in ansset) or j==max(ansset): 
                while cur+k in heights[i]:
                    cur+=k
                    f.add(cur)
                    combo+=1
                if len(ansset)<len(f):
                    ansset=f
                if j+k>max(heights[i]):
                    break
                if ans>len(heights[i])-now:
                    break
                ans=max(ans,combo)
print(ans)