
# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
a=int(input())
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

def rec(now,lim):
    ans=set()
    if now[0]!='0' and len(now)==lim:
        return {now}
    elif now[0]=='0' and len(now)==lim:
        return set()
    else:
        for i in range(10):
            ans|=rec(str(i)+now+str(i),lim)
    return ans

def reccheck(now,lim,n):
    ans=set()
    if len(now)==lim:
        if now[0]!='0' and int(now)<=n:
            return {now}
        else:
            return set()
    else:
        for i in range(10):
            if i*(10**(len(now)+1))+int(now)*10+i<=n:
                ans|=reccheck(str(i)+now+str(i),lim,n)
    return ans

test=set()
for i in range(1,len(str(n))+1):
    if i<len(str(n)):
        if i%2==0:
            for j in range(10):
                test|=rec(str(j)*2,i)
        else:
            for j in range(10):
                test|=rec(str(j),i)
    else:
        if i%2==0:
            for j in range(10):
                test|=reccheck(str(j)*2,i,n)
        else:
            for j in range(10):
                test|=reccheck(str(j),i,n)

ans=0
for i in test:
    k=int(i)
    p=k
    ans+=k
    a_k=[]
    while k!=0:
        a_k.append(k%a)
        k//=a
    for j in range(len(a_k)//2):
        if a_k[j]!=a_k[-j-1]:
            ans-=p
            break
print(ans)