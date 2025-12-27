# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

def rec(n,k,pc,now):
    if pc==0:
        return pow(2,k,998244353)
    elif k+1<pc:
        return 0
    else:
        ans=0
        for i in reversed(range(k)):
            if now+pow(2,i)<=n:
                p=rec(n,i,pc-1,now+pow(2,i))
                if p==0:
                    continue
                else:
                    ans=max(now+pow(2,i),ans)
        return ans
                # ans%=998244353
        print('ans',ans)
        return ans

for _ in range(t):
    n,k=map(int,input().split())
    bit=0
    while n>=2**bit:
        bit+=1
    print(bit)
    print(rec(n,bit,k,0))