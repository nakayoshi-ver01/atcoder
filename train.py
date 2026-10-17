n,k=map(int,input().split())
a=list(map(int,input().split()))

dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
dp[0][0]=1
test_num=0
MOD=10**9+7
for i in range(n):
    acc=[0]
    for j in range(k+1):
        acc.append(acc[-1]+dp[i][j])
    dp[i+1][0]=1
    test_num=min(test_num+a[i],k)
    for j in range(1,test_num+1):
        dp[i+1][j]=(acc[j+1]-acc[max(j-a[i],0)])%MOD

print(dp[-1][-1])