from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
t=list(input())

chara_count=defaultdict(list)
# grid=[list(input()) for _ in range(h)]
left=0
right=0

ans=0

for i in range(len(s)):
    chara_count[s[i]].append(i)

flg=True
temp=-1
for i in range(len(s)):
    if flg:
        flg=False
        chara_pos = i
        for j in range(len(t)):
            cand = bisect.bisect_left(chara_count[t[j]], chara_pos)
            if cand==len(chara_count[t[j]]):
                ans += len(s)-i
                temp = len(s)
                break
            else:
                chara_pos = chara_count[t[j]][cand]+1
        else:
            ans += chara_pos-1-i
            temp = chara_pos-1
    else:
        ans += temp-i
    if s[i]==t[0]:
        flg=True
print(ans)