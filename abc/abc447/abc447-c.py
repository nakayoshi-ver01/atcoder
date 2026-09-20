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
t=list(input())
# grid=[list(input()) for _ in range(h)]

ans=0
s_cur=0
t_cur=0
flg=True
while s_cur<len(s) and t_cur<len(t):
    if s[s_cur]!=t[t_cur]:
        if s[s_cur]!='A' and t[t_cur]!='A':
            flg=False
            break
        elif t[t_cur]!='A':
            ans+=1
            s_cur+=1
        elif s[s_cur]!='A':
            ans+=1
            t_cur+=1
    else:
        s_cur+=1
        t_cur+=1

if len(s)-s_cur>0:
    for i in range(s_cur,len(s)):
        if s[i]=='A':
            ans+=1
        else:
            flg=False
elif len(t)-t_cur>0:
    for i in range(t_cur,len(t)):
        if t[i]=='A':
            ans+=1
        else:
            flg=False

if flg:
    print(ans)
else:
    print(-1)