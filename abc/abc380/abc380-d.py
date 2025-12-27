# from collections import defaultdict,deque
import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n,m=map(int,input().split())
s=list(input())
q=int(input())
k=list(map(int,input().split()))
ans=list()
checklog=dict()
length=len(s)
for i in k:
    d=i-1
    check=d//length
    pop=0
    while check!=0:
        if check%2==1:
            pop+=1
        check//=2
    if pop%2:
        if s[d%length].islower():
            ans.append(s[d%length].upper())

        if s[d%length].isupper():
            ans.append(s[d%length].lower())

    else:
        ans.append(s[d%length])

print(*ans)