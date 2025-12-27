# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=input()
# grid=[list(input()) for _ in range(h)]
if len(s)%2==0:
    t=''
    for i in range(len(s)-1):
        t+=s[i]
        t+='$'
    t+=s[-1]
    s=t


r=[0 for _ in range(len(s))]
i=0
j=0

while i<len(s):
    while (i-j)>=0 and (i+j)<len(s) and s[i-j]==s[i+j]:
        j+=1
    r[i]=j
    k=1
    while (i-k)>=0 and k+r[i-k]<j:
        r[i+k]=r[i-k]
        k+=1
    i+=k
    j-=k
    print(list(s))
    print(r)