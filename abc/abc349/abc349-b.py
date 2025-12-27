from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
komoji=[chr(i) for i in range(97,123)]
dic=defaultdict(set)
for i in komoji:
    dic[s.count(i)].add(i)

for i in range(1,101):
    if len(dic[i])!=0 and len(dic[i])!=2:
        print('No')
        break
else:
    print('Yes')