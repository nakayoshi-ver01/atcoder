# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
l,r,d,u=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

ans=0
for i in range(max(abs(l),abs(r),abs(u),abs(d))+1):
    if i%2==0:
        if i==0:
            if l<=0<=r and d<=0<=u:
                ans+=1
        else:
            if d<=i<=u:
                if l<=i and -i<=r:
                    left=min(max(l,-i),i)
                    right=max(min(r,i),-i)
                    # print(left,right,'a')
                    ans+=right-left+1
            if d<=-i<=u:
                if l<=i and -i<=r:
                    left=min(max(l,-i),i)
                    right=max(min(r,i),-i)
                    # print(left,right,'b')
                    ans+=right-left+1
            if l<=i<=r:
                if d<=i and -i<=u:
                    down=min(max(d,-i),i)
                    up=max(min(u,i),-i)
                    # print(down,up,'c')
                    ans+=up-down+1
            if l<=-i<=r:
                if d<=i and -i<=u:
                    down=min(max(d,-i),i)
                    up=max(min(u,i),-i)
                    # print(down,up,'d')
                    ans+=up-down+1
            if l<=-i<=r and d<=-i<=u:
                ans-=1
            if l<=i<=r and d<=-i<=u:
                ans-=1
            if l<=-i<=r and d<=i<=u:
                ans-=1
            if l<=i<=r and d<=i<=u:
                ans-=1
print(ans)