
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
nums=[0 for i in range(10**6+1)]
for i in a:
    nums[i]+=i
rui=[0]
for i in range(1,10**6+1):
    rui.append(rui[-1]+nums[-i])
rui.reverse()


for i in range(n):
    print(rui[a[i]],end=' ')