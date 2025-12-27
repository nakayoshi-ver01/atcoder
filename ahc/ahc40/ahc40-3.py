n,t,rho=map(int,input().split())
ractangles=[list(map(int,input().split())) for _ in range(n)]
area=0
rui = [0]
for i in ractangles:
    area+=i[0]*i[1]
    rui.append(rui[-1]+max(i))
    if i[0]>i[1]:
        i.append(1)
    else:
        i.append(0)
# print(rui)
target=int(pow(area,0.5))
flame=[0,0]
ans=[0,0]
maxwidth=0
# print(ractangles)
for i in range(t):
    command=list()
    rows=[[-1,0] for _ in range(110)]
    rows_height = [0 for _ in range(110)]
    can_add = [True for _ in range(110)]
    width = target*(1+(0.5/t)*(i+1))
    last_row = False
    now = 0
    checker = False
    for j in range(n):
        p=j
        r=ractangles[j][2]
        d='U'
        b=-1
        ractangle = ractangles[j]
        for k,judge in zip(range(len(rows)),can_add):
            if rows[k][1]+min(ractangle[0],ractangle[1])<=width and judge:
                # print(row,row[1]+min(ractangle[0],ractangle[1]),ractangle,width)
                b=rows[k][0]
                if ractangle[0]>ractangle[1]:
                    ractangle[0],ractangle[1]=ractangle[1],ractangle[0]
                if k>now and last_row:
                    checker=True
                if checker:
                    r=1-r
                    rows[k][1]=rows[k][1]+ractangle[1]
                else:
                    rows[k][1]=rows[k][1]+ractangle[0]
                rows[k][0]=j
                break
        if rui[-1]-rui[j]<=target:
            last_row=True
        # for row,judge in zip(rows,can_add):
        #     if row[1]+min(ractangle[0],ractangle[1])<=width and judge:
        #         # print(row,row[1]+min(ractangle[0],ractangle[1]),ractangle,width)
        #         b=row[0]
        #         if ractangle[0]>ractangle[1]:
        #             ractangle[0],ractangle[1]=ractangle[1],ractangle[0]
        #         row[1]+=ractangle[0]
        #         row[0]=j
        #         break
            # print(j,rows)
        temprows=[]
        for i in range(len(rows)):
            if rows[i][0]==-1:
                now=i-1
                break
        can_add = [True for _ in range(110)]
        for i in range(len(rows)):
            for j in range(i+1,len(rows)):
                if rows[i][1]<rows[j][1]:
                    can_add[i]=False
                    break
        # print(rows)
        # print(can_add)
        command.append((p,r,d,b))
    print(len(command))
    for i in command:
        print(*i)
    ans=list(map(int,input().split()))
# print(rows,width)