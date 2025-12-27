n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
flg=0
s=list(input())
for i in range(n-1):
    if s[i]=='a' and s[i+1]=='b':
        flg=1
        break
    elif s[i]=='b' and s[i+1]=='a':
        flg=1
        break
if flg:
    print('Yes')
else:
    print('No')