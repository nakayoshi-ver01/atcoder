# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
k=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
t=list(input())
# grid=[list(input()) for _ in range(h)]

if len(s)==len(t):
    flg=0
    for i in range(len(s)):
        if s[i]!=t[i] and flg==0:
            flg=1
        elif s[i]!=t[i] and flg==1:
            print('No')
            break
    else:
        print('Yes')
elif len(s)==len(t)+1:
    flg=0
    for i in range(len(t)):
        if flg==0:
            if s[i]!=t[i]:
                flg=1
        elif flg==1:
            if s[i]!=t[i-flg]:
                print('No')
                break
    else:
        if flg==0:
            print('Yes')
        else:
            if s[-1]==t[-1]:
                print('Yes')
            else:
                print('No')
elif len(s)==len(t)-1:
    flg=0
    for i in range(len(s)):
        if flg==0:
            if s[i]!=t[i]:
                flg=1
        elif flg==1:
            if s[i-flg]!=t[i]:
                print('No')
                break
    else:
        if flg==0:
            print('Yes')
        else:
            if s[-1]==t[-1]:
                print('Yes')
            else:
                print('No')
else:
    print('No')