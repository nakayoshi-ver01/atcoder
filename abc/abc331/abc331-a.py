# n=int(input())
M,D=map(int,input().split())
y,m,d=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
if m==M and d==D:
    print(y+1,1,1)
elif m==M and d!=D:
    print(y,m,d+1)
elif m!=M and d==D:
    print(y,m+1,1)
else:
    print(y,m,d+1)