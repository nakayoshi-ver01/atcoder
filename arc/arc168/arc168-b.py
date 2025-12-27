from collections import defaultdict
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
# s=list(input())
xor=0
counter=defaultdict(int)
for i in a:
    counter[i]+=1
    xor=xor^i
if xor!=0:
    print(-1)
else:
    for i in reversed(counter):
        if counter[i]%2==1:
            print(i-1)
            break
    else:
        print(0)