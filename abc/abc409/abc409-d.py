from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
komoji=[chr(i) for i in range(97,123)]
for _ in range(t):
    n=int(input())
    s=input()
    front=-1
    for i in range(n-1):
        if s[i]>s[i+1]:
            front=i
            break
    back=n
    if front!=-1:
        for i in range(front+1,n):
            if s[front]<s[i]:
                back=i
                break
        print(s[:front]+s[front+1:back]+s[front]+s[back:])
    else:
        print(s)
