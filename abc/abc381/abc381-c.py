# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
runlen=list()
now=''
combo=0
for i in range(n):
    if s[i]==now:
        combo+=1
    else:
        if now!='':
            runlen.append((now,combo))
        now=s[i]
        combo=1
runlen.append((now,combo))

maxlen=0
if runlen[0][0]=='/' or runlen[-1][0]=='/':
    maxlen=1
for i in range(1,len(runlen)-1):
    if runlen[i][0]=='/' :
        maxlen=max(maxlen,1)
    if runlen[i-1][0]=='1' and runlen[i]==('/', 1) and runlen[i+1][0]=='2':
        maxlen=max(maxlen,2*min(runlen[i-1][1],runlen[i+1][1])+1)
print(maxlen)