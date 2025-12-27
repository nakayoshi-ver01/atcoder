# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())

if s.count('1')==1 and s.count('2')==2 and s.count('3')==3:
    print('Yes')
else:
    print('No')