from collections import defaultdict,deque
from sortedcontainers import SortedList
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
q=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache


MOD=998244353
factorical=[1]
for i in range(1,n+1):
    factorical.append((factorical[-1]*i)%MOD)




def op(x, y):#指定される演算を定義
    return max(x , y)

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
        while p > 1:
            p >>= 1
            self._d[p] = self._op(self._d[p << 1], self._d[p << 1 | 1])

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

A=[0 for _ in range(n+1)]

seg = SegTree(op, e, n+1, A)# nはAの長さ, Aはリスト
ans=1
for i in range(1,n):
    parent=seg.prod(q[i],n+1)
    dist=i-parent
    ans*=dist
    ans%=MOD
    seg.set(q[i],i)
print(ans)