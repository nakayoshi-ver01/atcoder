#n=int(input())
#n,m=map(int,input().split())
#a=list(map(int,input().split()))
s=list(input())
k=list()
for i in s:
    if i not in {'a','e','i','o','u'}:
        k.append(i)
print(''.join(k))
