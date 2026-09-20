from collections import defaultdict,deque
from sortedcontainers import SortedList, SortedSet
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

MOD=998244353




def modeq(b,a,p):#一次合同式(分子,b:分母,a)
    z=b*pow(a,p-2,p)
    z%=p
    return z

# エラトステネスの篩
def eratosthenes(n):
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if not(is_prime[p]):
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime

k=eratosthenes(10**7+1)
prime_numbers=[]
for i in range(10**7+1):
    if k[i]:
        prime_numbers.append(i)

#高速素因数分解
def factorization(n):
    global prime_numbers
    arr = []
    temp = n
    for i in prime_numbers:
        if i**2>n:
            break
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

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    soinsu_dict=defaultdict(SortedList)
    primes=list()
    for i in range(n):
        x=factorization(a[i])
        primes.append(x)
        for j in x:
            soinsu_dict[j[0]].add(j[1])
    # print(soinsu_dict)

    cand=1
    for p in soinsu_dict:
        cand*=pow(p,soinsu_dict[p][-1],MOD)
        cand%=MOD
    for i in primes:
        test=cand
        for j in i:
            if len(soinsu_dict[j[0]])>=2:
                if soinsu_dict[j[0]][-1]==j[1] and soinsu_dict[j[0]][-2]!=j[1]:
                    sample=pow(j[0],(j[1]-soinsu_dict[j[0]][-2]),MOD)
                    test*=modeq(1,sample,MOD)
                    test%=MOD
            else:
                sample=pow(j[0],j[1],MOD)
                test*=modeq(1,sample,MOD)
                test%=MOD
        print(test,end=' ')
    print()
    