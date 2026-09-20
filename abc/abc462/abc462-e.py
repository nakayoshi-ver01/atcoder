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
    a,b,x,y=map(int,input().split())
    ans=0
    cur_x,cur_y=0,0
    while abs(cur_x-x)+abs(cur_y-y)>1:
        warp_num=min(abs(cur_x-x),abs(cur_y-y))
        slide_num=max(abs(cur_x-x),abs(cur_y-y))
        if warp_num>0:
            ans+=warp_num*min(a,b)*2
            if x>0:
                cur_x+=warp_num
            else:
                cur_x-=warp_num
            if y>0:
                cur_y+=warp_num
            else:
                cur_y-=warp_num
        else:
            if slide_num>=2:
                if (min(a,b)*2)*2<=(a+b):
                    ans+=(min(a,b)*2)*((slide_num//2))*2
                else:
                    ans+=(a+b)*((slide_num//2))
            if abs(cur_x-x)==0:
                if y>0:
                    cur_y+=((slide_num//2)*2)
                else:
                    cur_y-=((slide_num//2)*2)
            else:
                if x>0:
                    cur_x+=((slide_num//2)*2)
                else:
                    cur_x-=((slide_num//2)*2)
    if abs(x-cur_x)==1:
        ans+=min(3*b,a)
        cur_x+=x-cur_x
    elif abs(y-cur_y)==1:
        ans+=min(3*a,b)
        cur_y+=y-cur_y
    print(ans)