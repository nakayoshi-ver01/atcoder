from collections import defaultdict

import sys
sys.setrecursionlimit(1000010)
def dfs(s,i,afnode,dis):
    global maxdis
    afnode.add(i)
    for d in s[i]:
        if d[0] not in afnode:
            dfs(s,d[0],afnode|{d[0]},dis+d[1])
        maxdis=max(maxdis,dis)
    return maxdis

#n=int(input())
n,m=map(int,input().split())
root=defaultdict(list)
for i in range(m):
    a=list(map(int,input().split()))
    root[a[0]].append((a[1],a[2]))
    root[a[1]].append((a[0],a[2]))



maxdis=-1
for i in range(1,n+1):
    k=dfs(root,i,{i},0)

print(maxdis)