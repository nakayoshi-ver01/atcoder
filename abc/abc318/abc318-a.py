#n=int(input())
n,m,p=map(int,input().split())
#a=list(map(int,input().split()))
#s=list(input())
k=m

count=0
while k<=n:
    count+=1
    k+=p
print(count)