import math
#n=int(input())
a,m,l,r=map(int,input().split())
#a=list(map(int,input().split()))
#s=list(input())
l-=a
r-=a
print(r//m-(l-1)//m)