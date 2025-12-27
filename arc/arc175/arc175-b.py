from collections import defaultdict,deque
# import math
# import sys

# n=int(input())
n,a,b=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
l=0
r=0
queue=deque()
for i in range(2*n):
    if not queue:
        queue.append(s[i])
        if s[i]=='(':
            l+=1
        else:
            r+=1
    else:
        if queue[-1]=='(' and s[i]==')':
            queue.pop()
            l-=1
        else:
            queue.append(s[i])
            if s[i]=='(':
                l+=1
            else:
                r+=1

cost=abs(l-r)//2*b
need=(len(queue)-abs(l-r))//2
if b*2<=a:

    cost+=(need+need%2)*b
else:
    cost+=need//2*a
    cost+=need%2*(min(a,2*b))
print(cost)