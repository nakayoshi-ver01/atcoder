# n=int(input())
n,d=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
ave=sum(a)/d
a.sort()
bags=[ave for i in range(d)]
absbags=[ave for i in range(d)]
for i in reversed(a):
    k=bags.index(max(absbags))
    bags[k]-=i
    absbags[k]=(bags[k])

vari=0
for i in bags:
    vari+=i**2
print(vari/d)