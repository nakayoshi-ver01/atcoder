from collections import defaultdict,deque
# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# s=list(input())
pair=defaultdict(set)
cand=[-1 for i in range(n)]
flg=0
for i in range(m):
    if a[i]!= b[i]:
        pair[a[i]].add(b[i])
        pair[b[i]].add(a[i])
    else:
        flg=-1
        break
if flg!=-1:
    search=deque()
    search.append((1,0))
    cand[0]=0
    before={i+1 for i in range(n)}
    before.remove(1)
    while before or search:#探索場所移動テンプレ
        if not search:
            x=before.pop()
            search.append((x,0))
        k=search.popleft()
        for i in pair[k[0]]:
            if i in before:
                search.append((i,(k[1]+1)%2))
                cand[i-1]=(k[1]+1)%2
                before.remove(i)
                #ここに探索内容を書く
            else:
                if cand[k[0]-1]==cand[i-1]:
                    flg=-1
                    break
        if flg==-1:
            break

if flg==-1:
    print('No')
else:
    print('Yes')