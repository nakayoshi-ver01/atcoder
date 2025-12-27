from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,target=map(int,input().split())
a=list(map(int,input().split()))
# a=[i+1 for i in range(n)]
# s=list(input())
# grid=[list(input()) for _ in range(h)]

divisors=defaultdict(set)

def prime_judge(n):
    num={i for i in range(2,n+1)}
    for i in range(2,int(n**(1/2))+1):
        if i in num:
            for j in range(2,n//i+1):
                if i*j in num:
                    num.remove(i*j)
                if i*j>n:
                    break
    return list(num)

maxa=max(a)
primes=prime_judge(maxa)

def factorization(n):
    global primes
    arr = []
    temp = n
    for i in primes:
        if i>temp:
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

memo=defaultdict(set)
for i in range(n):
    if a[i] not in memo:
        cand=factorization(a[i])
        div={1}
        tmp=set()
        for j in cand:
            for k in range(j[1]+1):
                for l in div:
                    tmp.add(l*(j[0]**k))
            div|=tmp
        memo[a[i]]=div
    else:
        div=memo[a[i]]
    for j in div:
        divisors[j].add(i)

ans_list=[0 for _ in range(n)]
before={i for i in range(n)}
div_keys=list(divisors.keys())
div_keys.sort()
for i in reversed(div_keys):
    if len(divisors[i])>=target:
        decide=before&divisors[i]
        for j in decide:
            ans_list[j]=i
        before-=decide
    # print(divisors[i],i,ans_list)
    

for i in ans_list:
    print(i)