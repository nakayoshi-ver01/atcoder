# n=int(input())
n,a,b,c=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
timesc=list()
dp=[0 for i in range(n)]
for i in range(n):
    z=list(map(int,input().split()))
    timesc.append(z)

dp[-1]=min(timesc[0][n-1]*a,timesc[0][n-1]*b+c)
for i in range(n):
    dp[i]=min(timesc[0][i]*a,timesc[0][i]*b+c)
for i in range(n):
    for j in range(n-1):
        dp[j]=min(dp[j],dp[i]+min(timesc[i][j]*a,timesc[i][j]*b+c))
    dp[n-1]=min(dp[n-1],dp[i]+timesc[i][n-1]*a,dp[i]+timesc[i][n-1]*b+c)
for i in range(n):
    for j in range(n-1):
        dp[j]=min(dp[j],dp[i]+min(timesc[i][j]*a,timesc[i][j]*b+c))
    dp[n-1]=min(dp[n-1],dp[i]+timesc[i][n-1]*a,dp[i]+timesc[i][n-1]*b+c)
print(dp[-1])
