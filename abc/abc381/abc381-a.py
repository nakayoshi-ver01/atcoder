# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())

d=set()
if len(s)%2==0:
    for i in range(len(s)//2):
        if s[2*i]==s[2*i+1] and s[2*i] not in d:
            d.add(s[2*i])
        else:
            print('No')
            break
    else:
        print('Yes')
else:
    print('No')