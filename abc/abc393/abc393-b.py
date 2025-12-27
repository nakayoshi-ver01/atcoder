# from collections import defaultdict,deque
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
ans=0
for i in range(1,len(s)//2+1):
    for j in range(len(s)-2*i):
        if s[j]=='A' and s[j+i]=='B' and s[j+2*i]=='C':
            ans+=1
    
print(ans)