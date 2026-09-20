# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
a_pair=[(a[i],i) for i in range(n)]
a_pair.sort()
ball_place=[0 for _ in range(n)]
for i in range(n):
    ball_place[a_pair[i][1]]=i
for _ in range(q):
    k=int(input())
    b=list(map(int,input().split()))
    b_pair=[(a[i-1],i-1) for i in b]
    b_pair.sort()
    ans_cur=0
    ans=a_pair[ans_cur][0]
    for i in b_pair:
        if i[1]==a_pair[ans_cur][1]:
            ans_cur+=1
            ans=a_pair[ans_cur][0]
        else:
            print(ans)
            break
    else:
        print(ans)
    