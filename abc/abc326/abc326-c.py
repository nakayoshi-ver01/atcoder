# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
a.sort()
b=list()
for i in a:
    b.append(i+m)
cur=0
can=list()
for i in range(n):

    while b[i]>a[cur] and cur<n-1:
        cur+=1
    if b[i]>a[-1]:
        can.append(n-i)
    else:
        can.append(cur-i)
print(max(can))