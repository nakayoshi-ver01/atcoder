from collections import defaultdict,deque
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

ans=0
a_queue=deque()
b_queue=deque()
c_queue=deque()
for i in range(len(s)):
    if s[i]=='A':
        a_queue.append(i)
    elif s[i]=='B':
        b_queue.append(i)
    elif s[i]=='C':
        c_queue.append(i)



while a_queue:
    a_min=a_queue.popleft()
    flg=False
    while b_queue:
        b_min=b_queue.popleft()
        if b_min<a_min:
            continue
        while c_queue:
            c_min=c_queue.popleft()
            if c_min<b_min:
                continue
            else:
                ans+=1
                flg=True
                break
        if flg:
            break

print(ans)