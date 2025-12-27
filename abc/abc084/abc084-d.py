# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
q=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

def eratosthenes(n):
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if not(is_prime[p]):
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime

primes=eratosthenes(10**5)

like_2017s=[0 for i in range(10**5)]

for i in range(5*10**4):
    k=i*2+1
    if primes[k] and primes[(k+1)//2]:
        like_2017s[k]=1

acc=[like_2017s[0]]
for i in range(1,10**5):
    acc.append(like_2017s[i]+acc[-1])

for i in range(q):
    l,r=map(int,input().split())
    print(acc[r]-acc[l-1])