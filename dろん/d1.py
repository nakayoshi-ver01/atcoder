n,k,t=map(int,input().split())
a=list(map(int,input().split()))
miss=[0 for i in range(n)]
for i in range(k):
    miss[a[i]-1]+=1
fix=list()
counter=0
ans=0
for i in range(t):
    if miss[i]+counter>1:
        if counter>0:
            ans+=miss[i]
            miss[i]=1-counter
        else:
            ans+=miss[i]-1
            miss[i]=1-counter
        counter=1
    elif miss[i]>0:
        counter+=1
    fix.append(miss[i])

for i in range(n-t):
    if miss[i+t]-fix[i]+counter>1:
        ans+=miss[i+t]
        miss[i+t]=0
    elif miss[i+t]-fix[i]>0:
        counter+=1
    elif miss[i+t]-fix[i]==-1:
        counter-=1
    fix.append(miss[i+t])
print(ans)