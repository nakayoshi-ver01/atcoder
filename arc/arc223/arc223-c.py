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

#セグメント木
import sys

def op(x, y):#指定される演算を定義
    return x + y

def e():#演算の単位元を定義(掛け算なら1,足し算なら0など)
    return 0


class SegTree:
    def __init__(self, op, e, n, v=None):#与えられた引数で初期化
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def set(self, p, x):#セグ木に値を入れる
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1

    def get(self, p):#セグ木の値を取り出す
        return self._d[p + self._size]

    def prod(self, l, r):#セグ木内の[l,r)の範囲で計算を行う
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    def all_prod(self):#全体の計算結果を返す
        return self._d[1]

    def check(self):#セグ木全体の中身の確認
        print(self._d)
        return 0
    





for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    remain_check=[True for _ in range(n)]
    for i in range(n):
        if remain_check[a[i]%n]:
            remain_check[a[i]%n]=False
        else:
            print(0)
            break
    else:
        A=[0 for _ in range(n)]
        seg = SegTree(op, e, n, A)# nはAの長さ, Aはリスト
        for i in range(n):
            if i%2==0:
                seg.set((i)%n)
            else:
                print(seg.prod(i,min(i+2,n-1)))
            seg.check()
        ans=1
        for i in range(1,n):
            ans*=pow(i,n-i,n)
            ans%=n
        print(ans)