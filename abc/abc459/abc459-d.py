from collections import defaultdict,deque
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
    s=list(input())
    chars=defaultdict(int)
    max_count=0
    max_char=''
    for i in s:
        chars[i]+=1
        if chars[i]>max_count:
            max_count=chars[i]
            max_char=i
    
    if max_count>len(s)//2+len(s)%2:
        print('No')
    else:
        print('Yes')
        v=['' for _ in range(len(s))]
        fill_count=0
        fill_flg=False
        for i in range(max_count):
            v[2*i]=max_char
            fill_count+=1
            if fill_count>=len(s)//2+len(s)%2:
                fill_count=0
                fill_flg=True
        for i in chars:
            if i==max_char:
                continue
            else:
                i_fill_count=0
                while i_fill_count<chars[i]:
                    if fill_count>=len(s)//2+len(s)%2:
                        fill_count=0
                        fill_flg=True
                    if fill_flg:
                        v[2*fill_count+1]=i
                    else:
                        v[2*fill_count]=i
                    fill_count+=1
                    i_fill_count+=1
        print(''.join(v))
