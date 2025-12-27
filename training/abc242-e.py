t=int(input())
mod=998244353
for _ in range(t):
    n=int(input())
    s=list(input())
    ans=0
    cur=0
    prefix=s[:(n+1)//2]
    rev=prefix[::-1]
    if n%2==0:
        palindrome=prefix+rev
    else:
        palindrome=prefix[:-1]+rev
    for i in reversed(prefix):
        ans+=(ord(i)-65)*pow(26,cur,mod)
        cur+=1
        ans%=mod
    ans+=1
    ans%=mod
    if ''.join(palindrome)>''.join(s):
        ans-=1
        ans%=mod
    print(ans)