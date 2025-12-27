# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
ans=0
l=1
r=2
for i in range(q):
    h,t=map(str,input().split())
    t=int(t)%n
    if h=='L':
        flg=0
        now=l
        for j in range(100):
            if now==t:
                ans+=j
                flg=1
                break
            elif now==r:
                now=l
                break
            now-=1
            now%=n
        if flg==0:
            for j in range(100):
                if now==t:
                    ans+=j
                    break
                elif now==r:
                    now=l
                    break
                now+=1
                now%=n
        l=t
    else:
        flg=0
        now=r
        for j in range(100):
            if now==t:
                ans+=j
                flg=1
                break
            elif now==l:
                now=r
                break
            now-=1
            now%=n
        if flg==0:
            for j in range(100):
                if now==t:
                    ans+=j
                    break
                elif now==l:
                    now=r
                    break
                now+=1
                now%=n
        r=t
print(ans)
