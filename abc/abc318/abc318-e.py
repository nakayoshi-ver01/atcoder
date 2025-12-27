from collections import defaultdict
n=int(input())
#n,m=map(int,input().split())
a=list(map(int,input().split()))
#s=list(input())
numbers=defaultdict(list)
ruinumbers=defaultdict(list)
for i in range(n):
    numbers[a[i]].append(i)
    if ruinumbers[a[i]]:
        ruinumbers[a[i]].append(ruinumbers[a[i]][-1]+i)
    else:
        ruinumbers[a[i]].append(i)

count=0
for i in numbers:
    for j in range(1,len(numbers[i])):
        count+=numbers[i][j]*j-ruinumbers[i][j-1]-j-j*(j-1)//2
print(count)