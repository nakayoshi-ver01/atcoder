# n=int(input())
k,g,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
glass=0
mug=0
for i in range(k):
    if glass==g:
        glass=0
    elif mug==0:
        mug=m
    else:
        if g-glass<=mug:
            mug-=(g-glass)
            glass=g
        else:
            glass+=mug
            mug=0

print(glass,mug)