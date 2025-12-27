s=list(input())
t=list(input())
if len(s)>len(t):
    s,t=t,s
dp=[[[0,[-1,-1]] for _ in range(len(t)+1)] for _ in range(len(s)+1)]

# 復元は課題にする
for i in range(len(s)+1):
    for j in range(len(t)+1):
        if i<len(s):
            if dp[i+1][j][0]<dp[i][j][0]:
                dp[i+1][j]=dp[i][j]
        if j<len(t):
            if dp[i][j+1][0]<dp[i][j][0]:
                dp[i][j+1]=dp[i][j]
        if i<len(s) and j<len(t):
            if s[i]==t[j]:
                dp[i+1][j+1][0]=dp[i][j][0]+1
                dp[i+1][j+1][1]=[i,j]

target=dp[-1][-1][1]
ans=[]
while target!=[-1,-1]:
    ans.append(s[target[0]])
    target=dp[target[0]][target[1]][1]
ans.reverse()
print(''.join(ans))
