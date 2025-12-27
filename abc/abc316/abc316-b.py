n=int(input())
#n,m=map(int,input().split())
a=list(map(int,input().split()))
#s=list(input())
a.sort()
flg=0
for i in range(min(a),min(min(a)+n+1,1000)):
    if i not in a:
        flg=1
        print(i)
        break
if flg==0:
    print(min(a)-1)