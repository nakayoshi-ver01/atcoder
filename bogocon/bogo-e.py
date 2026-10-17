from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

for _ in range(t):
    s=input()
    queue=deque()
    for i in range(len(s)):
        if not queue:
            queue.append(s[i])
        else:
            if s[i]==')':
                queue.append(s[i])
            elif s[i]=='(':
                last=queue.pop()
                if last==':':
                    continue
                else:
                    queue.append(last)
                    queue.append(s[i])
            elif s[i]==':':
                last=queue.pop()
                if last==')':
                    continue
                else:
                    queue.append(last)
                    queue.append(s[i])

    ans=0
    for i in range(len(queue)):
        if i!=0:
            if (queue[i-1],queue[i])==('(',':') or (queue[i-1],queue[i])==(':',')'):
                ans+=1
        if i!=len(queue)-1:
            if (queue[i],queue[i+1])==(':',')') or (queue[i],queue[i+1])==('(',':'):
                ans+=1
    print(ans//2,queue)