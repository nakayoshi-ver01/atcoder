from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

seq=deque()

for i in s:
    k=i
    if k in{'(' ,'[' ,'<'}:
        seq.append(k)
    elif k==')':
        if seq:
            last=seq.pop()
            if last!='(':
                seq.append(last)
                seq.append(k)
        else:
            seq.append(k)
    elif k==']':
        if seq:
            last=seq.pop()
            if last!='[':
                seq.append(last)
                seq.append(k)
        else:
            seq.append(k)
    elif k=='>':
        if seq:
            last=seq.pop()
            if last!='<':
                seq.append(last)
                seq.append(k)
        else:
            seq.append(k)

if seq:
    print('No')
else:
    print('Yes')