from collections import defaultdict
n=int(input())


flg=0
flavor2=list()
for i in range(n):
    f,s=map(int,input().split())

    flavor2.append((f,s))
flavor2.sort(key=lambda x:x[1])

if flavor2[-1][0]!=flavor2[-2][0]:
    print(flavor2[-1][1]+flavor2[-2][1])
    flg=1
else:
    for i in range(1,n+1):
        if flavor2[-1][0]!=flavor2[-i][0]:
            print(max(flavor2[-1][1]+(flavor2[-2][1]//2),flavor2[-1][1]+flavor2[-i][1]))
            flg=1
            break
if flg==0:
    print(flavor2[-1][1]+(flavor2[-2][1]//2))