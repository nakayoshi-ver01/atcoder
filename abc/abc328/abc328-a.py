# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
to=0
for i in a:
    if i<=m:
        to+=i

print(to)