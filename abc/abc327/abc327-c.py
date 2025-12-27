# n=int(input())
# n,m=map(int,input().split())

# s=list(input())
flg=0
place=list()
for i in range(9):
    a=list(map(int,input().split()))
    if len(set(a))==9:
        place.append(a)
    else:
        flg=-1
if flg!=-1:
    for j in range(9):
        test=set()
        for i in range(9):
            test.add(place[i][j])
        if len(test)!=9:
            flg=-1
            break
    for i in range(3):
        for j in range(3):
            block=set()
            for k in range(3):
                for l in range(3):
                    block.add(place[i*3+k][j*3+l])
            if len(block)!=9:
                flg=-1
                break
        if flg==-1:
            break

if flg==0:
    print('Yes')
else:
    print('No')