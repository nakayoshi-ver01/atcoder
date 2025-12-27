n=int(input())
#n,m=map(int,input().split())
graph=[[0 for i in range(101)]for i in range(101)]
#s=list(input())
for i in range(n):
    ract=list(map(int,input().split()))
    for i in range(ract[0],ract[1]):
        for j in range(ract[2],ract[3]):
            graph[i][j]+=1

count=0
for i in range(101):
    for j in range(101):
        if graph[i][j]>0:
            count+=1
print(count)