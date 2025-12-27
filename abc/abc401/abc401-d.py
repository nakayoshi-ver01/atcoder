# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

ans=[i for i in s]
need=k-s.count('o')
for i in range(n):
    if i!=0:
        if ans[i-1]=='o':
            ans[i]='.'
    if i!=n-1:
        if ans[i+1]=='o':
            ans[i]='.'
if need>0:
    runlen=[]
    can_o=0
    tmp=0
    for i in range(n):
        if ans[i]=='?':
            tmp+=1
        else:
            can_o+=(tmp+1)//2
            if tmp>0:
                runlen.append(((i-tmp,i),tmp))
            tmp=0
    can_o+=(tmp+1)//2
    if tmp>0:
        runlen.append(((i-tmp+1,i),tmp))
    tmp=0

    if can_o>need:
        print(''.join(ans))
    else:
        for i in runlen:
            if i[1]%2==1:
                count=0
                for j in range(i[0][0],i[0][1]+1):
                    if count%2==0:
                        ans[j]='o'
                    else:
                        ans[j]='.'
                    count+=1
        print(''.join(ans))
else:
    for i in range(n):
        if ans[i]=='?':
            ans[i]='.'
    print(''.join(ans))