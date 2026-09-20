from collections import defaultdict
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

abc=[[0] for _ in range(3)]

for i in range(n):
    if s[i]=='A':
        abc[0].append(abc[0][-1]+1)
        abc[1].append(abc[1][-1])
        abc[2].append(abc[2][-1])
    if s[i]=='B':
        abc[0].append(abc[0][-1])
        abc[1].append(abc[1][-1]+1)
        abc[2].append(abc[2][-1])
    if s[i]=='C':
        abc[0].append(abc[0][-1])
        abc[1].append(abc[1][-1])
        abc[2].append(abc[2][-1]+1)

ab=[abc[0][i]-abc[1][i] for i in range(n+1)]
bc=[abc[1][i]-abc[2][i] for i in range(n+1)]
print(ab)
print(bc)
same_place=set()
not_same_place=set()

ab_num=defaultdict(set)
bc_num=defaultdict(set)    

ans=0
for i in range(n+1):
    ab_num[ab[i]].add(i)
    bc_num[bc[i]].add(i)
    ans+=i+1-len(ab_num[ab[i]]|bc_num[bc[i]]|ab_num[bc[i]]|bc_num[ab[i]])
    print(ab_num[ab[i]]|bc_num[bc[i]]|ab_num[bc[i]]|bc_num[ab[i]])

    print(ans)