n,k=map(int,input().split())
h=list(map(int,input().split()))

dp=[10**10 for _ in range(n)]
dp[0]=0
for i in range(n):
    for j in range(k+1):
        if i+j<n:
            dp[i+j]=min(dp[i]+abs(h[i]-h[i+j]),dp[i+j])
        else:
            break
print(dp[-1])