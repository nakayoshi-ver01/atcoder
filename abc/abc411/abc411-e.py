from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
dice=[list(map(int,input().split())) for _ in range(n)]

def modeq(b,a,p):#一次合同式(分子,b:分母,a)
    z=b*pow(a,p-2,p)
    z%=p
    return z

mod=998244353
x=pow(6,n,mod)
x=modeq(1,x,mod)


sur_count=defaultdict(int)
sur_appear=defaultdict(set)
for i in range(n):
    for j in dice[i]:
        sur_appear[j].add(i)
        sur_count[(j,i)]+=1

sur_keys=list(sur_appear.keys())
sur_keys.sort()

flg=n
die_count=[0 for _ in range(n)]
ans=0
prob=defaultdict(int)
pt=0
total=0
for i in range(len(sur_keys)):
    for j in sur_appear[sur_keys[i]]:
        if flg==-1:
            total*=modeq(1,die_count[j],mod)
            total*=die_count[j]+sur_count[(sur_keys[i],j)]
            total%=mod

        if die_count[j]==0:
            flg-=1
        die_count[j]+=sur_count[(sur_keys[i],j)]

        if flg==0:
            total=1
            for k in range(n):
                total*=die_count[k]%mod
            flg=-1
    if i==0:
        prob[sur_keys[i]]=(total*sur_keys[i])%mod
    else:
        prob[sur_keys[i]]=((total-pt)*sur_keys[i])%mod
    pt=total
#     print(die_count,flg)
# print(prob)

result=0
for i in prob:
    result+=prob[i]%mod

print((result*x)%mod)
# sur_acc=defaultdict(int)
# sur_acc[0]=0
# for i in range(len(sur_keys)):
#     if i == 0:
#         sur_acc[sur_keys[i]]=sur_count[sur_keys[i]]
#     else:
#         sur_acc[sur_keys[i]]=sur_count[sur_keys[i]]+sur_count[sur_keys[i-1]]
    
