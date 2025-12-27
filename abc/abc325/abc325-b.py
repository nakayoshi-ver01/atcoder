n=int(input())

# a=list(map(int,input().split()))
# s=list(input())
place=[0 for i in range(24)]
for i in range(n):
    n,m=map(int,input().split())
    for j in range(9,18):
        place[(m+j)%24]+=n

print(max(place))