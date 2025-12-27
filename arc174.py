t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    p=list(map(int,input().split()))
    nowave=0
    nowp=0
    for i in range(5):
        nowave+=a[i]*(i-2)
    if nowave>=0:
        print(0)
    else:
        if p[3]<p[4]/2:
            print(p[3]*(-nowave))
        else:
            print(p[4]*((-nowave)//2)+min(p[3],p[4])*(-nowave%2))
        