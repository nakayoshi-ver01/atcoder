n=int(input())
a=list(map(int,input().split()))
dp=[[0 for _ in range(n+1)]for _ in range(n+1)]
dp[0][0]=1
for i in range(n):
    if a[i]!=-1 and i<a[i]:
        dp[i+1][a[i]]=sum(dp[i])
        dp[i+1][a[i]]%=998244353
    elif a[i]!=-1 and i>=a[i]:
        minro=dp[i][a[i]]
        for k in range(1,a[i]):
            minro=min(minro,dp[i+1-k][a[i]])
        dp[i+1][a[i]]=max(0,sum(dp[i])-dp[i+1-a[i]][a[i]])
        dp[i+1][a[i]]%=998244353
    
    else:
        for j in range(1,n+1):
            minro=dp[i][j]
            for k in range(1,j):
                minro=min(minro,dp[i+1-k][j])
            dp[i+1][j]=sum(dp[i])-minro
            dp[i+1][j]%=998244353
print(sum(dp[-1])%998244353)