import itertools
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
num=['1','2','3','4','5','6','7','8','9','0']
count=0
flg=0
anslist=list()
for i in range(1,11):
    c=itertools.combinations(num,i)
    for j in c:
        k=list(j)
        k.sort(reverse=True)
        anslist.append(int(''.join(k)))
        count+=1
        if count>n:
            flg=1
anslist.sort()
print(anslist[n])
