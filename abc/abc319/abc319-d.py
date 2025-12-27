#n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
#s=list(input())



minw=(sum(a)+n-1)//m
maxw=(max(a)*n+n-1)//m
center=(minw+maxw)//2

while minw+1<maxw:
    p=0
    row=1
    for i in range(n):
        if a[i]>center:
            row=m+1
            break
        if p+a[i]<center:
            p+=a[i]+1
        elif p+a[i]==center:
            p+=a[i]
        else:
            p=a[i]
            row+=1
    if row<=m:
        maxw=center
        center=(minw+maxw)//2
    else:
        minw=center
        center=(minw+maxw)//2
print(m)