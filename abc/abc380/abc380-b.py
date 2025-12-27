# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
a=list(map(str,input().split('|')))
# s=list(input())

ans=[]
for i in range(1,len(a)-1):
    ans.append(len(a[i]))
print(*ans)