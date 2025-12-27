# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
vote=[0 for i in range(n+1)]
champ=0
for i in a:
    vote[i]+=1
    if vote[champ]<vote[i]:
        print(i)
        champ=i
    elif vote[champ]==vote[i]:
        if champ<=i:
            print(champ)
        else:
            print(i)
            champ=i
    else:
        print(champ)