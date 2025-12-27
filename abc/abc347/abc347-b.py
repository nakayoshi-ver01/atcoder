# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
s=input()
k=set()
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        k.add(s[i:j])
print(len(k))