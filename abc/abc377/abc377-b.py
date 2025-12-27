# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=[list(input()) for _ in range(8)]

rooks=set()
for i in range(8):
    for j in range(8):
        if s[i][j]=='#':
            rooks.add((i,j))
    
for rook in rooks:
    for i in range(8):
        s[i][rook[1]]='x'
        s[rook[0]][i]='x'

ans=0
for i in range(8):
    for j in range(8):
        if s[i][j]=='.':
            ans+=1
print(ans)