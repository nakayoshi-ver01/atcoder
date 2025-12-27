n=int(input())
#n,m=map(int,input().split())
#a=list(map(int,input().split()))
#s=list(input())
president=list()
taka=list()
takamem=0
ao=list()
todo=list()
sumtodo=0
aomem=0
for i in range(n):
    a=list(map(int,input().split()))
    president.append(a)
    if a[0]>a[1]:
        taka.append(a)
        takamem+=a[2]
    else:
        ao.append(a)
        todo.append([(a[1]-a[0])//2+1,a[2]])
        sumtodo+=(a[1]-a[0])//2+1
        aomem+=a[2]
if takamem>aomem:
    print(0)
else:
    todo.sort()
    
    dp=[10000000 for i in range(takamem+aomem+1)]
    dp[0]=0
    for i in range(len(president)):
        if president[i][0]<president[i][1]:
            for j in reversed(range(president[i][2],len(dp))):
                dp[j]=min(dp[j],dp[j-president[i][2]]+(president[i][1]-president[i][0])//2+1)
        else:
            for j in reversed(range(president[i][2],len(dp))):
                dp[j]=min(dp[j],dp[j-president[i][2]])
    mind=100000000
    for k in range((takamem+aomem)//2,len(dp)):
        mind=min(dp[k],mind)
    print(mind)