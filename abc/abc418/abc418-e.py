from collections import defaultdict
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]


inclinations=defaultdict(int)
inclinations_length=defaultdict(int)
points=[]
for i in range(n):
    points.append(tuple(map(int,input().split())))

# dy/dx
for i in range(n):
    for j in range(i+1,n):
        pa=points[i]
        pb=points[j]
        dx=pa[0]-pb[0]
        dy=pa[1]-pb[1]
        if pa[0]==pb[0]:
            inclinations['inf']+=1
            inclinations_length[('inf',dx**2+dy**2)]+=1
        else:
            dx=pa[0]-pb[0]
            dy=pa[1]-pb[1]
            gcd=math.gcd(dx,dy)
            if dx>0:
                inclinations[(dx//gcd,dy//gcd)]+=1
                inclinations_length[(dx//gcd,dy//gcd,dx**2+dy**2)]+=1
            else:
                inclinations[(-dx//gcd,-dy//gcd)]+=1
                inclinations_length[(-dx//gcd,-dy//gcd,dx**2+dy**2)]+=1


# print(inclinations_length)
diff=0
for i in inclinations_length:
    diff+=(inclinations_length[i]*(inclinations_length[i]-1))//2

ans=0
for i in inclinations:
    ans+=(inclinations[i]*(inclinations[i]-1))//2

print(ans-diff//2)