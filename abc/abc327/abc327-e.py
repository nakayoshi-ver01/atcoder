n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
dp=[[0 for i in range(n+1)] for j in range(n+1)]
b=[0.9**(i) for i in range(n)]
bunbo=[0]
for i in range(n):
    bunbo.append(bunbo[-1]+b[i])

for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1:
            dp[i][j]=max(dp[i-1][1],a[i-1])
        elif i==j:
            dp[i][j]=0.9*dp[i-1][i-1]+a[i-1]
        else:
            dp[i][j]=max(dp[i-1][j],0.9*dp[i-1][j-1]+a[i-1])

ans=-9999999999
for i in range(1,n+1):
    ans=max(ans,dp[-1][i]/bunbo[i]-1200/(i**(1/2)))
print(ans)