n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
block=list()
counter=0
for i in range(n-1):
    if s[i]=='>':
        counter+=1
        flg=0
    elif s[i]=='<' and counter>0:
        block.append(counter)
        counter=0
        flg=1
    else:
        flg=1
if flg==0:
    block.append(counter)
ans=0
for i in block:
    ans+=i*(i+1)//2
print(ans)