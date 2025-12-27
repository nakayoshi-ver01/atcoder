# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
if n%2==1:
    if s[:n//2]==['1' for _ in range(n//2)] and s[n//2]=='/' and s[n//2+1:]==['2'for _ in range(n//2)]:
        print('Yes')
    else:
        print('No')
else:
    print('No')