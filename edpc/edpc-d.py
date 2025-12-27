n,w=map(int,input().split())
product=[tuple(map(int,input().split())) for _ in range(n)]
product.sort()

dp=[[-1 for _ in range(w+1)] for _ in range(n+1)]

dp[0][0]=0

for i in range(n):
    weight=product[i][0]
    value=product[i][1]
    for j in range(w+1):

        if dp[i][j]!=-1:
            dp[i+1][j]=max(dp[i][j],dp[i+1][j])
            if j+weight<w+1:
                dp[i+1][j+weight]=max(dp[i][j]+value,dp[i][j+weight])
print(max(dp[-1]))