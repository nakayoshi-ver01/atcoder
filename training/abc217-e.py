import heapq
from collections import deque

d=deque()
p=list()

cur=0
for i in range(int(input())):
    a=list(map(int,input().split()))
    if a[0]==1:
        d.append(a[1])
    elif a[0]==2:
        if p:
            print(heapq.heappop(p))
        else:
            print(d.popleft())
    elif a[0]==3:
        lend=len(d)
        for _ in range(lend):
            heapq.heappush(p,d.popleft())

    