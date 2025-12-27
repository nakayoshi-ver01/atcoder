# n=int(input())
n,m=map(str,input().split())
# a=list(map(int,input().split()))
n=int(n)
m=list(m)
p=len(m)
ans=list()
for i in range(n):
    s=list(input())
    if p==len(s):
        if m==s:
            ans.append(i+1)
        else:
            error=0
            for j in range(p):
                if m[j]!=s[j]:
                    error+=1
            if error==1:
                ans.append(i+1)
    elif p-1==len(s):
        flg=0
        for j in range(p):
            if flg==0 and m[j]!=s[j-flg]:
                flg=1
            elif flg==1 and m[j]!=s[j-flg]:
                flg=2
                break
            if flg==0 and j==p-2:
                break
        if flg==0 or flg==1:
            ans.append(i+1)
    elif p+1==len(s):
        flg=0
        for j in range(p+1):
            if flg==0 and m[j-flg]!=s[j]:
                flg=1
            elif flg==1 and m[j-flg]!=s[j]:
                flg=2
                break
            if flg==0 and j==p-1:
                break
        if flg==0 or flg==1:
            ans.append(i+1)
print(len(ans))
print(*ans)