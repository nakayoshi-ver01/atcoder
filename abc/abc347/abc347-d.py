# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
a,b,c=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
n=c
pc=list()
k=0
cand={i for i in range(60)}
while n>0:
    if n%2==1:
        pc.append(k)
        cand.remove(k)
    n//=2
    k+=1

if abs(a-b)%2==len(pc)%2 and abs(a-b)<=len(pc) and a+b>=len(pc):
    ansa=0
    ansb=0
    for i in pc:
        if a>=b:
            ansa+=2**i
            a-=1
        else:
            ansb+=2**i
            b-=1
    while a!=0:
        t=cand.pop()
        ansa+=2**t
        ansb+=2**t
        a-=1
        b-=1
    print(ansa,ansb)
else:
    print(2**60-1)