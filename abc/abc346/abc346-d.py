# from collections import defaultdict,deque
# import math
# import sys

n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
a=list(map(int,input().split()))

counter=0
x=list()
if n!=2:
    fdp=[[0,0] for i in range(n)]
    bdp=[[0,0] for i in range(n)]
    for i in range(n):
        if i%2==0:
            if s[i]=='0':
                fdp[i][0]=fdp[i-1][0]+a[i]
                fdp[i][1]=fdp[i-1][1]
            if s[i]=='1':
                fdp[i][0]=fdp[i-1][0]
                fdp[i][1]=fdp[i-1][1]+a[i]
        if i%2==1:
            if s[i]=='0':
                fdp[i][0]=fdp[i-1][0]
                fdp[i][1]=fdp[i-1][1]+a[i]
            if s[i]=='1':
                fdp[i][0]=fdp[i-1][0]+a[i]
                fdp[i][1]=fdp[i-1][1]
    fdp.insert(0,[0,0])
    s.reverse()
    for i in range(n):
        if i%2==0:
            if s[i]=='0':
                bdp[i][0]=bdp[i-1][0]+a[-i-1]
                bdp[i][1]=bdp[i-1][1]
            if s[i]=='1':
                bdp[i][0]=bdp[i-1][0]
                bdp[i][1]=bdp[i-1][1]+a[-i-1]
        if i%2==1:
            if s[i]=='0':
                bdp[i][0]=bdp[i-1][0]
                bdp[i][1]=bdp[i-1][1]+a[-i-1]
            if s[i]=='1':
                bdp[i][0]=bdp[i-1][0]+a[-i-1]
                bdp[i][1]=bdp[i-1][1]
    bdp.reverse()
    bdp.append([0,0])
    ans=10**30
    if n%2==0:
        for i in range(1,n-1):
            ans=min(ans,fdp[i][0]+bdp[i+1][0],fdp[i][1]+bdp[i+1][1])
    else:
        for i in range(1,n-1):
            ans=min(ans,fdp[i][0]+bdp[i+1][1],fdp[i][1]+bdp[i+1][0])
    print(ans)
else:
    if s[0]==s[1]:
        print(0)
    else:
        print(min(a))