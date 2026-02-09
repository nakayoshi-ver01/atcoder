from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# a=[1]*100
# s=list(input())
# grid=[list(input()) for _ in range(h)]

dig=[0 for _ in range(200010)]

for i in a:
    dig[i-1]+=1

dig_up=[0 for _ in range(200010)]
ans=deque()
this_dig=n
for i in range(200010):
    temp_dig=this_dig+dig_up[i]
    ans.appendleft(temp_dig%10)
    count=1
    while temp_dig>=10:
        temp_dig//=10
        dig_up[i+count]+=temp_dig%10
        count+=1
    this_dig-=dig[i]
    # print(dig[:10],this_dig,temp_dig)
    # print(dig_up[:10])
flg=False
while ans:
    k=ans.popleft()
    if not flg and k==0:
        continue
    elif not flg and k!=0:
        flg=True
    print(k,end='')