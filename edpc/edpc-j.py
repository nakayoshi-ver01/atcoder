
n=int(input())
a=list(map(int,input().split()))

dp=[[[0 for _ in range(n+2)] for _ in range(n+2)] for _ in range(n+2)]

for k in range(n+1):
    for j in range(n+1):
        for i in range(n+1):
            if i+j+k==0:
                continue
            prob=n/(i+j+k)
            if i>0:
                prob+=dp[i-1][j][k]*i/(i+j+k)
            if j>0:
                prob+=dp[i+1][j-1][k]*j/(i+j+k)
            if k>0:
                prob+=dp[i][j+1][k-1]*k/(i+j+k)
            dp[i][j][k]=prob
dishes=[0,0,0,0]
for i in a:
    dishes[i]+=1

print(dp[dishes[1]][dishes[2]][dishes[3]])