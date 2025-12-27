from collections import defaultdict
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
p=defaultdict(int)
c=s[0]
p[c]=1
counter=1
if n>1:

    for i in range(1,n):
        if s[i]==c:
            counter+=1
            if p[c]:
                p[c]=max(counter,p[c])
            else:
                p[c]=counter
        else:
            counter=1
            c=s[i]
            if p[c]:
                p[c]=max(counter,p[c])
            else:
                p[c]=counter

ans=0
for i in p:
    ans+=p[i]
print(ans)