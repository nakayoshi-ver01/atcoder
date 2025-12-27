M=int(input())
D=list(map(int,input().split()))
C=[]
S=(sum(D)+1)/2#まんなかを探す
Q=0
P=[]
for i in range(M+1):#月積算リスト
    X=(D[0:i])
    C.append(sum(X))

if M==1:
    m=[1,int(S)]
    print(*m)
    
else:
    for i in range(M):#どの月の範囲か探す
        if C[i]<=S<C[i+1]:
            P.append(C[i])
            Q+i
            break
    Q=C.index(P[0])#何月？
    d=S-P[0]#何日目？
    m=[Q+1,int(d)] 
    print(P,C)
    print(*m)
        