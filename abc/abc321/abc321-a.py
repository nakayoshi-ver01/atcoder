#n=int(input())
#n,m=map(int,input().split())
#a=list(map(int,input().split()))
s=list(input())

flg=0
for i in range(len(s)-1):
    if int(s[i])<=int(s[i+1]):
        flg=1
        break
if flg==0:
    print('Yes')
else:
    print('No')