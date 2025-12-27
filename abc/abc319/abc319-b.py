n=int(input())
#n,m=map(int,input().split())
#a=list(map(int,input().split()))
#s=list(input())
ans=['1']
for i in range(1,n+1):
    flg=0
    for j in range(1,10):
        if n%j==0 and i%(n//j)==0:
            flg=1
            ans.append(str(j))
            break
    if flg==0:
        ans.append('-')

p=''.join(ans)
print(p)