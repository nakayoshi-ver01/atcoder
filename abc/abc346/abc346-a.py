# from collections import defaultdict,deque
# import math
# import sys

n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
b=list()
for i in range(n-1):
    b.append(a[i]*a[i+1])
print(*b)