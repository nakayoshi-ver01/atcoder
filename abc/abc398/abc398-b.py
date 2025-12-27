from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
cards=defaultdict(int)
for i in range(7):
    cards[a[i]]+=1

two=set()
three=set()
for i in range(1,14):
    if cards[i]>=3:
        three.add(i)
    elif cards[i]>=2:
        two.add(i)
# print(two,three)
if len(three)>=2:
    print('Yes')
elif len(three)==1 and len(two)>=1:
    print('Yes')
else:
    print('No')