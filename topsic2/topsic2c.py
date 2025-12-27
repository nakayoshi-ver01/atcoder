def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr


a,b,n=map(int,input().split())
length=b-a
z=factorization(length)
cand={1}
for i in z:
    newcand=set()
    for j in cand:
        for k in range(i[1]+1):
            newcand.add(j*i[0]**k)
    
    cand=newcand
p=list(cand)
p.sort()
for i in p:
    if length//i+1<=n:
        print(length//i+1)
        break