# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
ocount=0
ren=0
need=0
for i in range(n):
    if s[i]=='0':
        need=max(need,ren-min(m,ocount))
        ren=0
        ocount=0
    if s[i]=='1':
        ocount+=1
        ren+=1
    if s[i]=='2':
        ren+=1
need=max(need,ren-min(m,ocount))
print(need)