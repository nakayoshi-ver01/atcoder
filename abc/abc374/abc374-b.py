# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
t=list(input())
for i in range(min(len(s),len(t))):
    if s[i]!=t[i]:
        print(i+1)
        break
else:
    if len(s)!=len(t):
        print(min(len(s),len(t))+1)
    else:
        print(0)