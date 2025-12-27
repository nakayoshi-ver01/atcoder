from collections import defaultdict,deque
import sys
n=int(input())
node=list()
after=set()
sys.setrecursionlimit(1000010)
def dfs(s,i,afnode):
    global node
    afnode.add(i)
    for d in s[i]:
        if d not in afnode:
            dfs(s,d,afnode)
    if i not in after and i!=1:
        after.add(i)
        node.append(i)
    return node
#n,m=map(int,input().split())

#s=list(input())
know=defaultdict(set)

for i in range(n):
    a=list(map(int,input().split()))
    know[i+1]=set(a[1:])


ans=dfs(know,1,set())
print(*ans)