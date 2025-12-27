import itertools
n=int(input())
r=list(input())
c=list(input())

ansflg=0
testlist=[set() for i in range(n)]
for i in range(n):
    test=[r[i]]
    for j in range(n-2):
        z=['.' for b in range(n-3-j)]
        for k in {'A','B','C'}-{r[i]}:
            z.append(k)
        p=itertools.permutations(z)
        for k in p:
            testlist[i].add(tuple(test+list(k)))
        test.insert(0,'.')
if n==3:
    for i in testlist[0]:
        for j in testlist[1]:
            for k in testlist[2]:
                flag=0
                for l in range(n):
                    col=[i[l],j[l],k[l]]
                    
                    if not {'A','B','C'}<=set(col):
                        flag=1
                    else:
                        scol={'A','B','C'}-{c[l]}
                        t=scol.pop()
                        q=scol.pop()
                        if col.index(c[l])>col.index(t):
                            flag=1
                        elif col.index(c[l])>col.index(q):
                            flag=1
                        for end in {'A','B','C'}:
                            if col.count(end)>1:
                                flag=1
                                break
                if flag==0:
                    ansflg=1
                    print('Yes')
                    print(''.join(i))
                    print(''.join(j))
                    print(''.join(k))
                    break
            if flag==0:
                break
        if flag==0:
            break
    if ansflg==0:
        print('No')
if n==4:
    for i in testlist[0]:
        for j in testlist[1]:
            for k in testlist[2]:
                for g in testlist[3]:
                    flag=0
                    for l in range(n):
                        col=[i[l],j[l],k[l],g[l]]
                        if not {'A','B','C'}<=set(col):
                            flag=1
                        else:
                            scol={'A','B','C'}-{c[l]}
                            t=scol.pop()
                            q=scol.pop()
                            if col.index(c[l])>col.index(t):
                                flag=1
                            elif col.index(c[l])>col.index(q):
                                flag=1
                            for end in {'A','B','C'}:
                                if col.count(end)>1:
                                    flag=1
                                    break
                    if flag==0:
                        ansflg=1
                        print('Yes')
                        print(''.join(i))
                        print(''.join(j))
                        print(''.join(k))
                        print(''.join(g))
                        break
                if flag==0:
                    break
            if flag==0:
                break
        if flag==0:
            break
    if ansflg==0:
        print('No')
if n==5:
    
    for i in testlist[0]:
        for j in testlist[1]:
            for k in testlist[2]:
                for g in testlist[3]:
                    for d in testlist[4]:
                        flag=0
                        for l in range(n):
                            col=[i[l],j[l],k[l],g[l],d[l]]
                            if not {'A','B','C'}<=set(col):
                                flag=1
                            else:
                                scol={'A','B','C'}-{c[l]}
                                t=scol.pop()
                                q=scol.pop()
                                if col.index(c[l])>col.index(t):
                                    flag=1
                                elif col.index(c[l])>col.index(q):
                                    flag=1
                                for end in {'A','B','C'}:
                                    if col.count(end)>1:
                                        flag=1
                                        break
                        if flag==0:
                            ansflg=1
                            print('Yes')
                            print(''.join(i))
                            print(''.join(j))
                            print(''.join(k))
                            print(''.join(g))
                            print(''.join(d))
                            break
                    if flag==0:
                        break
                if flag==0:
                    break
            if flag==0:
                break
        if flag==0:
            break
    if ansflg==0:
        print('No')