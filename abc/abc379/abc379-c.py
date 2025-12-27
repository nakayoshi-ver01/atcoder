# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
randx=list(map(int,input().split()))
randa=list(map(int,input().split()))
sortedplace=list()
for i,j in zip(randx,randa):
    sortedplace.append((i,j))
sortedplace.sort()
x=list()
a=list()
for i in sortedplace:
    x.append(i[0])
    a.append(i[1])
if sum(a)!=n:
    print(-1)
elif x[0]!=1:
    print(-1)
else:
    ans=0
    for i in range(m-1):
        if x[i+1]-x[i]>a[i]:
            print(-1)
            break
        else:
            ans+=((a[i]-1+a[i]-1-x[i+1]+x[i]+1)*(x[i+1]-x[i]))//2
            a[i+1]+=a[i]-1-x[i+1]+x[i]+1
    else:
        if n-x[-1]!=a[-1]-1:
            print(-1)
        else:
            ans+=((a[-1]-1+a[-1]-1-n+x[-1]+1)*(n-x[-1]))//2
            print(ans)