# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
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
# from functools import cmp_to_key, lru_cache

def check(arr,x,length):
    test=[]
    d=x
    for i in range(length):
        test.append(arr[i]-d)
        d//=2
    for i in range(n):
        if test[i]<0:
            return False
        if i!=n-1:
            if test[i]>=test[i+1]*2:
                pass
            else:
                return False
    else:
        return True

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    test_arr=a[::]
    while any(test_arr[i] for i in range(n)):
        test=10**10
        for i in reversed(range(1,n)):
            if test_arr[i]==0 and test_arr[i-1]!=0:
                test=1
            elif test_arr[i]!=0:
                test=min(2*test+1,test_arr[i-1],2*test_arr[i]+1)
        if test==0:
            print(-1)
            break
        one_time=10**10
        for i in range(n):
            if test//(2**i)>0:
                one_time=min(test_arr[i]//(test//(2**i)),one_time)
        print(test,one_time)
        for i in range(n):
            test_arr[i]-=test*one_time
            test//=2
        ans+=one_time
        print(test_arr)
    else:
        print(ans)