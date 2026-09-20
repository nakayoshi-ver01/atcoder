from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

MOD=998244353

kaijo_log=[1]
for i in range(1,n+1):
    kaijo_log.append((kaijo_log[-1]*i)%MOD)

def combination(n,r):
    # 事前計算でn!,n-r!,r!を用意しておいて、nCrを計算する,(n,rともに一定の範囲内で何度も計算する場合に有効)
    result=kaijo_log[n]
    for i in r:
        result*=pow(kaijo_log[i],MOD-2,MOD)
        result%=MOD
    return result


edge=defaultdict(set)

for i in range(m):
    a=list(map(int,input().split()))
    edge[a[0]-1].add(a[1]-1)
    edge[a[1]-1].add(a[0]-1)

cur=0
bf=[True for _ in range(n)]
ans=1

mono_flg=True

state=deque()
state.append(0)
bf[0]=False
chars=defaultdict(int)
chars[s[0]]+=1
while 1:
    if state:
        now=state.popleft()
        for i in edge[now]:
            if bf[i]:
                chars[s[i]]+=1
                state.append(i)
                bf[i]=False
    if not state:
        r=list()
        total=0
        for i in chars:
            if chars[i]>1:
                mono_flg=False
            total+=chars[i]
            r.append(chars[i])
        ans*=combination(total,r)
        ans%=MOD
        chars=defaultdict(int)
        while cur<n:
            if bf[cur]:
                state.append(cur)
                chars[s[cur]]+=1
                bf[cur]=False
                break
            cur+=1
        else:
            break

if mono_flg:
    ans*=pow(kaijo_log[2],MOD-2,MOD)
    ans%=MOD
    print(ans)
else:
    print(ans)