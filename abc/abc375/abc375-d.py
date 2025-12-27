from collections import defaultdict,deque
# import sys
# import math
import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())

chara=defaultdict(list)

for i in range(len(s)):
    chara[s[i]].append(i)

ans=0
for i in chara:
    for j in chara[i]:
        for k in chara:
            if i!=k:
                pos=bisect.bisect_left(chara[k],j)
                ans+=pos*(len(chara[k])-pos)

for i in chara:
    length=len(chara[i])
    if len(chara[i])>=3:
        ans+=length*(length-1)*(length-2)//6

print(ans)