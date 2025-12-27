# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
import bisect
# import heapq
q=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
def prime_judge(n):
    num={i for i in range(2,n+1)}
    for i in range(2,int(n**(1/2))+1):
        if i in num:
            for j in range(2,n//i+1):
                if i*j in num:
                    num.remove(i*j)
                if i*j>n:
                    break
    return num

t=prime_judge(10**3)
def factorization(n):
    global t 
    flg=0
    test=n
    if n in t:
        return False
    else:
        for i in t:
            if test%i==0 and flg==0:
                flg+=1
                while test%i==0:
                    test//=i
                if test==1:
                    return False
                elif test in t:
                    return True
            elif test%i==0 and flg==1:
                flg+=1
                while test%i==0:
                    test//=i
                if test==1:
                    return True
                else:
                    return False
        else:
            if flg==0:
                return False
            if flg==1:
                return True

four_hundred_like=[]
for i in range(6,10**6+1):
    if factorization(i):
        four_hundred_like.append(i**2)

for _ in range(q):
    n=int(input())
    x=bisect.bisect_right(four_hundred_like,n)
    print(four_hundred_like[x-1])