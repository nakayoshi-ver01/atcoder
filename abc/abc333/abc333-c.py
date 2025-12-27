import heapq
n=int(input())
#n,m=map(int,input().split())
# a=list(map(int,input().split()))
#s=list(input())
t=[]
repone=[1]
for i in range(100):
    repone.append(repone[-1]*10+1)
for i in range(len(repone)):
    for j in range(i,len(repone)):
        for k in range(j,len(repone)):
            heapq.heappush(t,repone[i]+repone[j]+repone[k])
for i in range(n-1):
    x=heapq.heappop(t)
print(heapq.heappop(t))