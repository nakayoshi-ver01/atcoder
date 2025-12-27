from collections import defaultdict
n=int(input())
query=list()
# a=list(map(int,input().split()))
# s=list(input())
potion=defaultdict(int)
monster=defaultdict(int)
bag=0
maxbag=0
flg=0
gets=list()
for i in range(n):
    a=list(map(int,input().split()))
    # if a[0]==1:
    #     potion[a[1]].append(i)
    # if a[0]==1:
    #     monster[a[1]].append(i)
    query.append(a)
for i in reversed(range(n)):
    q=query[i]
    if q[0]==1:
        if monster[q[1]]>0:
            gets.append(1)
            monster[q[1]]-=1
        else:
            gets.append(0)
    elif q[0]==2:
        monster[q[1]]+=1

gets.reverse()
for i in monster:
    if monster[i]>0:
        print(-1)
        break
else:
    cur=0
    for q in query:
        if q[0]==1 and gets[cur]==1:
            bag+=1
            maxbag=max(bag,maxbag)
            cur+=1
        elif q[0]==1 and gets[cur]==0:
            cur+=1
        else:
            bag-=1
    print(maxbag)
    print(*gets)
    