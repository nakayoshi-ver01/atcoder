# n=int(input())
n,s,m,l=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
dp=[100000000 for i in range(n+1)]
dp[0]=0
for i in range(1,n+1):
    dp[i]=min(dp[max(0,i-6)]+s,dp[i])
    dp[i]=min(dp[max(0,i-8)]+m,dp[i])
    dp[i]=min(dp[max(0,i-12)]+l,dp[i])
print(dp[-1])
