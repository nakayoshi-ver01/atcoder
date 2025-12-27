n,w=map(int,input().split())
product=[tuple(map(int,input().split())) for _ in range(n)]
product.sort(key=lambda x:x[1])

dp=[[10**15 for _ in range(n*product[-1][1]+1)] for _ in range(n+1)]
dp[0][0]=0
for i in range(n):
    weight=product[i][0]
    value=product[i][1]
    for j in range(n*product[-1][1]+1):
        if dp[i][j]!=10**15:
            dp[i+1][j]=min(dp[i][j],dp[i+1][j])
            if dp[i][j]+weight<=w:
                dp[i+1][j+value]=min(dp[i][j]+weight,dp[i+1][j+value])
maxvalue=0
for i in range(len(dp[-1])):
    if dp[-1][i]!=10**15:
        maxvalue=i
print(maxvalue)