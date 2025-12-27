# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
import time

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
ans=0
primes=prime_judge(int(n**(1/2)))
for i in primes:
    if i**8<=n:
        ans+=1
    else:
        break

for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        if (primes[i]*primes[j])**2<=n:
            ans+=1
        else:
            break

print(ans)