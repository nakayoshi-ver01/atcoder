# 
n,q=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
ans=[0]
for i in range(n-1):
    if s[i]==s[i+1]:
        ans.append(ans[-1]+1)
    else:
        ans.append(ans[-1])

for i in range(q):
    l,r=map(int,input().split())
    print(ans[r-1]-ans[l-1])
