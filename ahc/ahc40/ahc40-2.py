n,t,rho=map(int,input().split())
ractangles=[list(map(int,input().split())) for _ in range(n)]
rui = [0]
area=0
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
    columns_height = [0 for _ in range(110)]
    columns_last = [-1 for _ in range(110)]
    can_add = [True for _ in range(110)]
    lines=[[] for _ in range(110)]
    width = target*(0.8+(0.6/t)*(i+1))
    last_row = False
    now = 0
    checker = False
    for j in range(n):
        p=j
        r=ractangles[j][2]
        d='U'
        b=-1
        ractangle = ractangles[j]
        if not last_row:
            for k,judge in zip(range(now+1),can_add):
                if rows[k][1]+min(ractangle[0],ractangle[1])<=width and judge:
                    b=rows[k][0]
                    if ractangle[0]>ractangle[1]:
                        ractangle[0],ractangle[1]=ractangle[1],ractangle[0]
                    columns_height[len(lines[k])]+=ractangle[1]
                    columns_last[len(lines[k])]=j
                    if k>now and last_row:
                        checker=True
                    if checker:
                        r=1-r
                        rows[k][1]=rows[k][1]+ractangle[1]
                    else:
                        rows[k][1]=rows[k][1]+ractangle[0]
                    rows[k][0]=j
                    lines[k].append(j)
                    break
            else:
                b=rows[now+1][0]
                if ractangle[0]>ractangle[1]:
                    ractangle[0],ractangle[1]=ractangle[1],ractangle[0]
                columns_height[0]+=ractangle[1]
                columns_last[0]=j
                rows[now+1][1]=rows[now+1][1]+ractangle[0]
                rows[now+1][0]=j
                lines[now+1].append(j)
        else:
            for k,judge in zip(range(now+1),can_add):
                if rows[k][1]+min(ractangle[0],ractangle[1])<=width and judge:
                    b=rows[k][0]
                    if ractangle[0]>ractangle[1]:
                        ractangle[0],ractangle[1]=ractangle[1],ractangle[0]
                    columns_height[len(lines[k])]+=ractangle[1]
                    columns_last[len(lines[k])]=j
                    if k>now and last_row:
                        checker=True
                    if checker:
                        r=1-r
                        rows[k][1]=rows[k][1]+ractangle[1]
                    else:
                        rows[k][1]=rows[k][1]+ractangle[0]
                    rows[k][0]=j
                    lines[k].append(j)
                    break
            else:
                r=1-r
                minbrocks=10**3
                for line in lines[:now]:
                    minbrocks=min(len(line),minbrocks)
                height=10**10
                min_column=0
                target_column = columns_height[:minbrocks].index(min(columns_height[:minbrocks]))  
                columns_height[target_column]+=ractangle[0]*100
                b=columns_last[target_column]
                columns_last[target_column]=j
                rows[now+1][1]=rows[now+1][1]+ractangle[1]
        if rui[-1]-rui[j]<=target:
            last_row=True
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