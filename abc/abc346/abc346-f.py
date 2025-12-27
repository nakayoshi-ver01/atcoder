# from collections import defaultdict,deque
# import math
# import sys

# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
total=m*(m+1)//2
af=set()
for i in a:
    if i not in af and i<=m:
        total-=i
        af.add(i)
print(total)