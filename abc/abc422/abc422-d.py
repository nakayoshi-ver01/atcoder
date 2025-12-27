# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

def rec(n,array):
    if n==1:
        result=[]
        for i in array:
            result.append(i//2)
            result.append(i//2+i%2)            
        return result
    else:
        result=[]
        for i in array:
            result.append(i//2)
            result.append(i//2+i%2)
        return rec(n-1,result)


ans=rec(n,[k])
u=max(ans)-min(ans)
print(u)
print(*ans)