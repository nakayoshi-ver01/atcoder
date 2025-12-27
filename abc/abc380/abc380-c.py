from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
runlenz=deque()
runleno=deque()
now=s[0]
combo=1

for i in range(1,n):
    if s[i]==now:
        combo+=1
    else:
        if now=='0':
            runlenz.append(combo)
        else:
            runleno.append(combo)
        now=s[i]
        combo=1

if now=='0':
    runlenz.append(combo)
else:
    runleno.append(combo)


ans=''
if s[0]=='1':
    cur=0
    while runlenz or runleno:
        if runleno:
            ans+='1'*runleno.popleft()
            cur+=1
        if cur==k-1:
            ans+='1'*runleno.popleft()
            cur+=1
            if runlenz:
                ans+='0'*runlenz.popleft()
        if runlenz:
            ans+='0'*runlenz.popleft()
else:
    cur=0
    while runlenz or runleno:
        if runlenz:
            ans+='0'*runlenz.popleft()
        if runleno:
            ans+='1'*runleno.popleft()
            cur+=1
        if cur==k-1:
            ans+='1'*runleno.popleft()
            cur+=1
            if runlenz:
                ans+='0'*runlenz.popleft()
print(ans)