from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache


# エラトステネスの篩
def eratosthenes(n):
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if not(is_prime[p]):
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime


prime=eratosthenes(10**7)

chars=defaultdict(list)
for i in range(len(s)):
    chars[s[i]].append(i)

shapes=set()
for i in chars:
    shapes.add(tuple(chars[i]))
for i in range(2,10**7):
    if prime[i]:
        nums=defaultdict(list)
        str_i=str(i)
        for j in range(len(str_i)):
            nums[str_i[j]].append(j)
        num_shapes=set()
        for j in nums:
            num_shapes.add(tuple(nums[j]))
        for j in shapes:
            if j not in num_shapes:
                break
        else:
            for j in num_shapes:
                if j not in shapes:
                    break
            else:
                print(i)
                break
else:
    print(-1)