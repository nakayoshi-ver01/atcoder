# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    runlen=[]
    tar=[-1,-1]
    for i in range(n):
        if a[i]%k!=tar[0]:
            if tar[0]!=-1:
                runlen.append(tar)
            tar=[a[i]%k,1]
        else:
            tar[1]+=1
    runlen.append(tar)
    print(runlen)
    ans=1
    check_len=0
    for i in range(len(runlen)-1):
        if (runlen[i][0]+runlen[i+1][0])%k==0:
            check_len+=runlen[i][1]+runlen[i+1][1]
        else:
            ans*=check_len
            ans%=998244353
            