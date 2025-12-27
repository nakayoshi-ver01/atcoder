from collections import defaultdict,deque
n=int(input())

tree=defaultdict(set)
# a=list(map(int,input().split()))
# s=list(input())
for i in range(n-1):
    u,v=map(int,input().split())
    tree[u].add(v)
    tree[v].add(u)
if len(tree[1])==1:
    print(1)
else:
    ans=[]
    for i in tree[1]:
        counter=0
        root=deque()
        af={1,i}
        root.append(i)
        while root:
            counter+=1
            now=root.popleft()
            for j in tree[now]:
                if j not in af:
                    af.add(j)
                    root.append(j)
            
        ans.append(counter)
    ans.sort()
    res=0
    for k in range(len(ans)-1):
        res+=ans[k]
    print(res+1)        