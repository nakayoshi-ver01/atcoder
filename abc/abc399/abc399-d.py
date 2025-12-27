from collections import defaultdict,deque
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

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    pairset=set()
    pairs=defaultdict(list)
    for i in range(2*n):
        pairs[a[i]].append(i)
    # print(pairs)
    # for pair in pairs:
    #     if pairs[pair][0]+1!=pairs[pair][1]:
    #         pairset.add(tuple(pairs[pair]))
    # print(pairset)
    ans=0
    for pair in pairs:
        if pairs[pair][0]+1!=pairs[pair][1]:
            pairset.add(tuple(pairs[pair]))
        else:
            continue
        cand=[[1,1],[1,-1],[-1,-1],[-1,1]]
        for i in cand:
            test=(pairs[pair][0]+i[0],pairs[pair][1]+i[1])
            # print(test,pairs[pair])
            if test in pairset:
                ans+=1
        # print(pairset)
    print(ans)