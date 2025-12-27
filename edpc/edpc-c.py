n=int(input())

dp=[[0,0,0] for _ in range(n+1)]

for i in range(1,n+1):
    activity=list(map(int,input().split()))
    dp[i][0]=max(dp[i-1][1],dp[i-1][2])+activity[0]
    dp[i][1]=max(dp[i-1][0],dp[i-1][2])+activity[1]
    dp[i][2]=max(dp[i-1][0],dp[i-1][1])+activity[2]
print(max(dp[-1]))