from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

def pattern(memo,m):
    ans=0
    if m==1:
        return 2**memo[1]%998244353
    else:
        t=factorization(m)
        for prime in t:
            for count in range(1,prime[1]):
                ans+=(2**memo[(prime[0]**count)]%998244353)*pattern(memo,m//(prime[0]**count))%998244353
        return ans

memo=defaultdict(int)
for i in range(n):
    memo[a[i]]+=1

ok=pattern(memo,m)