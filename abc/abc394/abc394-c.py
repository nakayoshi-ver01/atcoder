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

stock=deque()
for i in s:
    k=i
    count=0
    if k=='A':
        if stock:
            p=stock.pop()
            if p=='W':
                count+=1
                while stock and p=='W':
                    p=stock.pop()
                    if p=='W':
                        count+=1
            if p!='W':
                stock.append(p)
            stock.append(k)    
            for i in range(count):
                stock.append('C')
        else:
            stock.append(k)
    else:
        stock.append(k)

for i in range(len(stock)):
    print(stock.popleft(),end='')