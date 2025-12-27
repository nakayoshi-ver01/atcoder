n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
anslist=list()
for i in range(1,10):
    for j in range(0,10):
        if i*j<10:
            k=[str(i),str(j),str(i*j)]
            p=int(''.join(k))
            anslist.append(p)

for i in anslist:
    if i>=n:
        print(i)
        break