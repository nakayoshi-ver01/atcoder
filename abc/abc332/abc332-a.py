# n=int(input())
n,s,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
cost=0
for i in range(n):
    a,b=map(int,input().split())
    cost+=a*b

if cost<s:
    cost+=k

print(cost)