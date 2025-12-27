n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
ans=0
for i in range(1,n+1):
    p=list(str(i))
    if len(p)==p.count(p[0]):
        j=int(p[0])
        for k in range(3):
            if j<=a[i-1]:
                ans+=1
                j=10*j+int(p[0])
        # while j<=a[i]:
        #     ans+=1
        #     j=10*j+int(p[0])
print(ans)