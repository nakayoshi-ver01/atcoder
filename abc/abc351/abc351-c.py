from collections import defaultdict,deque
# import sys
# sys.setrecursionlimit(1000010)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
balls=deque()
for i in range(n):
    if not balls:
        balls.append(a[i])
    else:
        k=balls.pop()
        if k==a[i]:
            j=1
            while balls:
                t=balls.pop()
                if t==(a[i]+j):
                    j+=1
                else:
                    balls.append(k)
                    balls.append(a[i]+j)
                    break
            else:
                balls.append(a[i]+j)
        else:
            balls.append(k)
            balls.append(a[i])
print(balls)