# from collections import defaultdict,deque
import sys
sys.set_int_max_str_digits(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
ans=0
for i in range(n):
    num=int(s[i])
    ans+=num*((i+1)%10)*(10**((i+1)//10))*((10**(n-i)-1)//9)
print(ans)
