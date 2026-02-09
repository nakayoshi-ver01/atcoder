# from collections import defaultdict,deque
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

import numpy as np

n,k,x=map(int,input().split()) 
a=list(map(int,input().split()))
a.sort(reverse=True)
b=[a[i] for i in range(n)]

d=[a[i] for i in range(n)]


f = np.array(b)
g = np.array(d)
fft_len = 1  # |f|+|g|-1 以上の2の冪数
while fft_len<len(f)+len(g)-1:
    fft_len*=2


# f,gをフーリエ変換
Ff = np.fft.rfft(f, fft_len)
print(Ff)
Fg = np.fft.rfft(g, fft_len)
print(Fg)
 
# 各要素について掛け合わせる
Ffg = Ff * Fg
print(Ffg)
 
# 逆変換後、整数に丸める
fg = np.fft.irfft(Ffg, fft_len)
fg = np.rint(fg)
print(fg)

