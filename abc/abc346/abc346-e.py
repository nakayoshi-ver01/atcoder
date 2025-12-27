from collections import defaultdict,deque
# import math
# import sys

# n=int(input())
h,w,m=map(int,input().split())
tate=[False for i in range(h)]
yoko=[False for j in range(w)]
t=list()
y=list()
color=defaultdict(int)
# a=list(map(int,input().split()))
# s=list(input())
query=list()
for _ in range(m):
    q=list(map(int,input().split()))
    query.append(q)
query.reverse()
for q in query:
    if q[0]==1:
        if not tate[q[1]-1]:
            tate[q[1]-1]=q[2]
            t.append(q[2])
            color[q[2]]+=w-len(y)
    if q[0]==2:
        if not yoko[q[1]-1]:
            yoko[q[1]-1]=q[2]
            y.append(q[2])
            color[q[2]]+=h-len(t)

color[0]+=(h-len(t))*(w-len(y))

p=list(color.keys())
p.sort()


print(len(p))
for i in p:
  if color[i]!=0:
    print(i,color[i])