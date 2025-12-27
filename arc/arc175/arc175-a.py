# from collections import defaultdict,deque
# import math
# import sys

n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
s=list(input())
lspoon=[True for _ in range(n)]
rspoon=[True for _ in range(n)]
ldp=[0 for _ in range(n+1)]
ldp[0]=1
rdp=[0 for _ in range(n+1)]
rdp[0]=1
for i in range(n):
    if s[a[i]-1]=='L':
        if lspoon[a[i]-1]==True:
            ldp[i+1]=ldp[i]
            lspoon[a[i]-1]=False
        else:
            ldp[i+1]=0
            break
    if s[a[i]-1]=='R':
        if lspoon[a[i]%n]==True:
            ldp[i+1]=0
            break
        else:
            ldp[i+1]=ldp[i]
            lspoon[a[i]-1]=False
    if s[a[i]-1]=='?':
        if lspoon[a[i]%n]==False:
            ldp[i+1]=ldp[i]*2
            lspoon[a[i]-1]=False
        else:
            ldp[i+1]=ldp[i]
            lspoon[a[i]-1]=False
    ldp[i+1]%=998244353
    
for i in range(n):
    if s[a[i]-1]=='L':
        if rspoon[a[i]-1]==True:
            rdp[i+1]=0
            break
        else:
            rdp[i+1]=rdp[i]
            rspoon[a[i]%n]=False
    if s[a[i]-1]=='R':
        if rspoon[a[i]%n]==True:
            rdp[i+1]=rdp[i]
            rspoon[a[i]%n]=False
        else:
            rdp[i+1]=0
            rspoon[a[i]%n]=False
    if s[a[i]-1]=='?':
        if rspoon[a[i]-1]==False:
            rdp[i+1]=rdp[i]*2
            rspoon[a[i]%n]=False
        else:
            rdp[i+1]=rdp[i]
            rspoon[a[i]%n]=False
    rdp[i+1]%=998244353

print(ldp[-1]+rdp[-1])