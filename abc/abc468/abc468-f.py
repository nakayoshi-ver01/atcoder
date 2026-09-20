from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

n=int(input())
p=list(map(int,input().split()))

neg=-10**18
size=1
while size<n+1:
    size*=2

# seg[p]には d[i][p] から全体加算分を引いた値を持つ
seg=[neg]*(2*size)
seg[size]=0  # d[0][0]=0
for i in range(size-1,0,-1):
    seg[i]=max(seg[2*i],seg[2*i+1])

def range_max(l,r):
    res=neg
    l+=size
    r+=size
    while l<r:
        if l%2:
            res=max(res,seg[l])
            l+=1
        if r%2:
            r-=1
            res=max(res,seg[r])
        l//=2
        r//=2
    return res

def point_chmax(pos,value):
    pos+=size
    if seg[pos]>=value:
        return
    seg[pos]=value
    pos//=2
    while pos:
        seg[pos]=max(seg[2*pos],seg[2*pos+1])
        pos//=2

current_max=0
add=0

for x in p:
    if x>current_max:
        # 全ての d[i-1][p] に 1 を加算する
        add+=1
        current_max=x
    else:
        # d[i][x] = max(d[i-1][x], max_{0<=j<x} d[i-1][j]+1)
        point_chmax(x,range_max(0,x)+1)

print(seg[1]+add)