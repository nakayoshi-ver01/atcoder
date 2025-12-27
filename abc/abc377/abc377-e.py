from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
p=list(map(int,input().split()))
# s=list(input())

for i in range(n):
    p[i]-=1
root=defaultdict(list)
pl=defaultdict(list)
before={i for i in range(n)}

log=deque()
log.append(p[0])
before.remove(p[0])
group=list()
while before or log:
    print(before)
    if not log:
        root[group[0]]=group
        log.append(before.pop())
        group=list()
    now=log.popleft()
    group.append(now)
    pl[now]=[group[0],len(group)-1]
    if p[now] in before:
        log.append(p[now])
        before.remove(p[now])
    print(now)
root[group[0]]=group
pl[now]=[group[0],len(group)-1]
print(root)
print(pl)

ans=list()
for i in range(n):
    print(p[i],pl[p[i]])
    move=pow(2,k,len(root[pl[p[i]][0]]))
    target=root[pl[p[i]][0]][(pl[p[i]][1]+move)%len(root[pl[p[i]][0]])]
    ans.append(target)
result=list()
for i in ans:
    result.append(ans[i]+1)
print(result)