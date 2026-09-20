# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
h,w,n=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
pieces_h=list()
pieces_w=list()
for i in range(n):
    piece=list(map(int,input().split()))
    pieces_h.append((*piece,i))
    pieces_w.append((*piece,i))

pieces_h.sort(reverse=True)
pieces_w.sort(key= lambda x:x[1],reverse=True)
ans_list=[[0,0] for _ in range(n)]
unset_flg=[True for _ in range(n)]
h_cur=0
w_cur=0
current_h=h
current_w=w
tar='h'
while h_cur<n and w_cur<n:
    if tar=='h':
        if not unset_flg[pieces_h[h_cur][2]]:
            h_cur+=1
        elif pieces_h[h_cur][0]==current_h:
            ans_list[pieces_h[h_cur][2]]=[h-current_h+1,w-current_w+1]
            current_w-=pieces_h[h_cur][1]
            unset_flg[pieces_h[h_cur][2]]=False
            h_cur+=1
        else:
            tar='w'
    if tar=='w':
        if not unset_flg[pieces_w[w_cur][2]]:
            w_cur+=1
        elif pieces_w[w_cur][1]==current_w:
            ans_list[pieces_w[w_cur][2]]=[h-current_h+1,w-current_w+1]
            current_h-=pieces_w[w_cur][0]
            unset_flg[pieces_w[w_cur][2]]=False
            w_cur+=1
        else:
            tar='h'


for i in ans_list:
    print(*i)