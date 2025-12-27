# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
s=list()
for i in range(n):
    ppp=list(input())
    s.append(ppp)
rui=[[0 for _ in range(n)] for _ in range(n)]
if s[0][0]=='B':
    rui[0][0]=1

for j in range(1,n):
    if s[0][j]=='B':
        rui[0][j]=rui[0][j-1]+1
    else:
        rui[0][j]=rui[0][j-1]
for i in range(1,n):
    if s[i][0]=='B':
        rui[i][0]=rui[i-1][0]+1
    else:
        rui[i][0]=rui[i-1][0]
    for j in range(1,n):
        if s[i][j]=='B':
            rui[i][j]=rui[i][j-1]+rui[i-1][j]-rui[i-1][j-1]+1
        else:
            rui[i][j]=rui[i][j-1]+rui[i-1][j]-rui[i-1][j-1]

for _ in range(q):
    a=list(map(int,input().split()))
    end=(a[2]//n)*(a[3]//n)*rui[-1][-1]+(a[2]//n)*rui[-1][a[3]%n]+(a[3]//n)*rui[a[2]%n][-1]+rui[a[2]%n][a[3]%n]
    if a[0]!=0 and a[1]!=0:
        start=((a[0]-1)//n)*((a[1]-1)//n)*rui[-1][-1]+((a[0]-1)//n)*rui[-1][a[1]%n]+((a[1]-1)//n)*rui[a[0]%n][-1]+rui[(a[0]-1)%n][(a[1]-1)%n]
    elif a[0]==0:
        start=((a[1]-1)//n)*rui[a[0]%n][-1]
    elif a[1]==0:
        start=((a[0]-1)//n)*rui[-1][a[1]%n]
    else:
        start=0
    if a[0]!=0 :
        x=((a[0]-1)//n)*((a[3])//n)*rui[-1][-1]+((a[0]-1)//n)*rui[-1][a[3]%n]+((a[3])//n)*rui[(a[0]-1)%n][-1]+rui[(a[0]-1)%n][(a[3])%n]
    else:
        x=0
    if a[1]!=0:
        y=((a[2])//n)*((a[1]-1)//n)*rui[-1][-1]+((a[2])//n)*rui[-1][(a[1]-1)%n]+((a[1]-1)//n)*rui[a[2]%n][-1]+rui[(a[2])%n][(a[1]-1)%n]
    else:
        y=0
    print(end-x-y+start)