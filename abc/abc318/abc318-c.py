#n=int(input())
n,d,p=map(int,input().split())
f=list(map(int,input().split()))
f.sort(reverse=True)
#s=list(input())
# left=0
# right=n
# center=(left+right)//2
# while left+1<right:
#     if f[center]>p/d:
#         right=center
#         center=(left+right)//2
#     else:
#         left=center
#         center=(left+right)//2
# print(center)

stack=[0 for i in range(n//d+1)]
for i in range(n):
    stack[i//d]+=f[i]

count=0
for i in range(len(stack)):
    if stack[i]>p:
        count+=p
    else:
        count+=stack[i]
print(count)