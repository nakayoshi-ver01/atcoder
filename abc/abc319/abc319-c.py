import itertools,math
#n=int(input())
#n,m=map(int,input().split())
l=[i for i in range(9)]
per=itertools.permutations(l)

bingo=list()
for i in range(3):
    a=list(map(int,input().split()))
    bingo.append(a)
#s=list(input())
reach=list()
line=[{0,1,2},{0,3,6},{0,4,8},{1,4,7},{2,5,8},{3,4,5},{6,7,8},{2,4,6}]
for i in line:
    flg=0
    for j in i:
        for k in i:
            if j!=k and bingo[j//3][j%3]==bingo[k//3][k%3]:
                ll=i-{j,k}
                lll=ll.pop()
                reach.append((j,k,lll))
                flg=1
                break
        if flg==1:
            break
count=0
for i in per:
    o=list(i)
    for j in reach:
        if o.index(j[0])<o.index(j[2]) and o.index(j[1])<o.index(j[2]):
            count+=1
            break
print(1-count/math.perm(9,9))