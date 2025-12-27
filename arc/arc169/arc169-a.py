from collections import defaultdict,deque

x=defaultdict(list)
longest=defaultdict(set)
n=int(input())
a=list(map(int,input().split()))
p=list(map(int,input().split()))
for i in range(n-1):
    x[p[i]-1].append(i+1)
af={0}
cand=deque()
cand.append((0,0))
ans=0
while cand:
    now=cand.popleft()
    flg=0
    longest[now[1]].add(now[0])
    for i in x[now[0]]:
        if i not in af:
            flg=1
            cand.append((i,now[1]+1))
            af.add(i)

for i in reversed(longest):
    for j in longest[i]:
        ans+=a[j]
    if ans!=0:
        break
if ans==0:
    print(0)
elif ans>0:
    print('+')
elif ans<0:
    print('-')