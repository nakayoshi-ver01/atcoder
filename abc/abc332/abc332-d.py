# n=int(input())
h,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
ans=0
a=[]
ta=[[0 for i in range(h)] for i in range(w)]
b=[]
tb=[[0 for i in range(h)] for i in range(w)]
hsets={i for i in range(h)}
wsets={i for i in range(w)}
for i in range(h):
    row=list(map(int,input().split()))
    a.append(row)
    for j in range(w):
        ta[j][i]=row[j]
for i in range(h):
    row=list(map(int,input().split()))
    b.append(row)
    for j in range(w):
        tb[j][i]=row[j]
flg=0
for i in range(h):
    a[i].sort()
    b[i].sort()
for i in range(w):
    ta[i].sort()
    tb[i].sort()

for i in range(h):
    for j in hsets:
        x=a[i]
        y=b[j]
        if x==y:
            hsets.remove(j)
            flg+=1
            break
if flg==h:
    for i in range(w):
        for j in wsets:
            x=ta[i]
            y=tb[j]
            x.sort()
            y.sort()
            if x==y:
                wsets.remove(j)
                flg+=1
                break
    if flg==h+w:
        for i in reversed(range(h)):
            for j in range(i):
                x=a[j]
                if x!=b[j]:
                    a[j],a[j+1]=a[j+1],a[j]
                    ans+=1
        for i in reversed(range(w)):
            for j in range(i):
                x=ta[j]
                if x!=tb[j]:
                    ta[j],ta[j+1]=ta[j+1],ta[j]
                    
                    ans+=1
        
if flg==h+w:
    print(ans)
else:
    print(-1)