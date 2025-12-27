import math
#n=int(input())
s,p=map(int,input().split())
#a=list(map(int,input().split()))
#s=list(input())
if s**2-4*p>=0:
    ansa=(-s+math.sqrt(s**2-4*p))/2
    ansb=(-s-math.sqrt(s**2-4*p))/2
    
    if ansa.is_integer() and ansb.is_integer() and int(-1*ansa)*int(-1*ansb)==p and int(-1*ansa)+int(-1*ansb)==s:
        print(min(int(-1*ansa),int(-1*ansb)),max(int(-1*ansa),int(-1*ansb)))
    else:
        print(-1)
else:
    print(-1)