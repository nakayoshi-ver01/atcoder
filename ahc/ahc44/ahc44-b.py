from collections import deque
n,l=map(int,input().split())
t=list(map(int,input().split()))
t_mem=[(t[i],i) for i in range(n)]
t_mem.sort(reverse=True)
go_count=[0 for i in range(n)]
count=0

a=[-1 for _ in range(n)]
b=[-1 for _ in range(n)]
group=[[] for _ in range(20)]
for i in range(n):
    count=0
    if t[i]==0:
        continue
    while abs(2**count-t[i]-1)>abs(2**(count+1)-t[i]-1):
        count+=1
    group[count].append(i)

for i in range(len(group)):
    if len(group[0])==0:
        del group[0]
    else:
        break
for i in reversed(range(len(group))):
    if len(group[i])==0:
        del group[i]
    else:
        break
group=group[::-1]
for i in range(len(group)-1):
    if not group[i]:
        count=1
        for j in range(i+1,len(group)):
            if len(group[j])>0:
                x=group[j].pop()
                group[i].append(x)
                break
        else:
            break

for i in reversed(range(len(group))):
    if not group[i]:
        del group[i]
    else:
        break
for i in range(len(group)):
    for j in range(len(group[i])-1):
        a[group[i][j]]=group[i][j+1]
        b[group[i][j]]=group[i][j+1]
    a[group[i][-1]]=group[(i+1)%len(group)][0]
    b[group[i][-1]]=group[0][0]



for i in range(n):
    print(a[i],b[i])