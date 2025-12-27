

n,m=map(int,input().split())
grid=[list(input()) for _ in range(n)]


directorys=[(0,1),(0,-1),(1,0),(-1,0)]
wall_cells=[set() for _ in range(7)]
for i in range(n):
    for j in range(n):
        if grid[i][j]=='#':
            wall_cells[6].add(i*n+j)
        else:
            wall_cell=0
            for directory_i,directory_j in directorys:
                next_point=(i+directory_i,j+directory_j)
                if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
                    if grid[next_point[0]][next_point[1]]=='#':
                        wall_cell+=1
                else:
                    wall_cell+=1
            wall_cells[wall_cell].add(i*n+j)



for i in range(2):
    while wall_cells[i]:
        target = wall_cells[i].pop()
        print(target//n,target%n)
        grid[target//n][target%n]='#'
        wall_cells[6].add(target)
        for directory_i,directory_j in directorys:
             next_point=((target//n)+directory_i,(target%n)+directory_j)
             if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
                 next_point_decrypt=next_point[0]*n+next_point[1]
                 for j in range(i,4):
                    if next_point_decrypt in wall_cells[j]:
                        wall_cells[j].remove(next_point_decrypt)
                        wall_cells[j+1].add(next_point_decrypt)
                        break
    # print(i,len(wall_cells[i]),len(wall_cells[i]))
    # print(i+1,len(wall_cells[i+1]),wall_cells[i+1])

used_four_cell=set()

for cell in wall_cells[4]:
    if cell//n not in {0,n-1} and cell%n not in {0,n-1}:
        print(cell//n,cell%n)
        wall_cells[6].add(target)
        used_four_cell.add(cell)

wall_cells[4]-=used_four_cell

two_patterns=[set(),set()]
# directorys=[(0,1),(0,-1),(1,0),(-1,0)]
for two_wall_cell in wall_cells[2]:
    wall_cell=0
    for directory_i,directory_j in directorys[:2]:
        next_point=((two_wall_cell//n)+directory_i,(two_wall_cell%n)+directory_j)
        if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
            if grid[next_point[0]][next_point[1]]=='#':
                wall_cell+=1
        else:
            wall_cell+=1
    if wall_cell in {0,2}:
        two_patterns[0].add(two_wall_cell)
    else:
        two_patterns[1].add(two_wall_cell)
    

already_three=wall_cells[3]
move_three=set()

# for i in grid:
#     print(''.join(i))



# print('-------------------------------------')
# print(len(two_patterns[0]))
# print(len(two_patterns[1]))
# print(len(move_three))
# print(len(already_three))
# print(len(wall_cells[4]))
# print('-------------------------------------')


while two_patterns[0]:
    target = two_patterns[0].pop()
    print(target//n,target%n)
    wall_cells[6].add(target)
    for directory_i,directory_j in directorys:
        next_point=((target//n)+directory_i,(target%n)+directory_j)
        if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
            next_point_decrypt=next_point[0]*n+next_point[1]
            if next_point_decrypt in two_patterns[0]:
                two_patterns[0].remove(next_point_decrypt)
                move_three.add(next_point_decrypt)
            elif next_point_decrypt in two_patterns[1]:
                two_patterns[1].remove(next_point_decrypt)
                move_three.add(next_point_decrypt)
            elif next_point_decrypt in already_three:
                already_three.remove(next_point_decrypt)
                wall_cells[4].add(next_point_decrypt)


used_two_cell = set()

for target in two_patterns[1]:
    if (target//n not in {0,n-1}) and (target%n not in {0,n-1}) and (target not in used_two_cell):
        print(target//n,target%n)
        wall_cells[6].add(target)
        for directory_i,directory_j in directorys:
            next_point=((target//n)+directory_i,(target%n)+directory_j)
            if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
                next_point_decrypt=next_point[0]*n+next_point[1]
                if next_point_decrypt in two_patterns[1] and next_point_decrypt not in used_two_cell:
                    used_two_cell.add(next_point_decrypt)
                    move_three.add(next_point_decrypt)
                elif next_point_decrypt in already_three:
                    already_three.remove(next_point_decrypt)
                    wall_cells[4].add(next_point_decrypt)
        used_two_cell.add(target)

two_patterns[1]-=used_two_cell

while two_patterns[1]:
    target = two_patterns[1].pop()
    print(target//n,target%n)
    wall_cells[6].add(target)
    for directory_i,directory_j in directorys:
        next_point=((target//n)+directory_i,(target%n)+directory_j)
        if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
            next_point_decrypt=next_point[0]*n+next_point[1]
            if next_point_decrypt in two_patterns[1]:
                two_patterns[1].remove(next_point_decrypt)
                move_three.add(next_point_decrypt)
            elif next_point_decrypt in already_three:
                already_three.remove(next_point_decrypt)
                wall_cells[4].add(next_point_decrypt)

used_three_cell = set()

for target in move_three:
    if (target//n not in {0,n-1}) and (target%n not in {0,n-1}) and (target not in used_three_cell):
        print(target//n,target%n)
        wall_cells[6].add(target)
        for directory_i,directory_j in directorys:
            next_point=((target//n)+directory_i,(target%n)+directory_j)
            if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
                next_point_decrypt=next_point[0]*n+next_point[1]
                if next_point_decrypt in move_three and next_point_decrypt not in used_three_cell:
                    used_three_cell.add(next_point_decrypt)
                    wall_cells[4].add(next_point_decrypt)
                elif next_point_decrypt in already_three:
                    already_three.remove(next_point_decrypt)
                    wall_cells[4].add(next_point_decrypt)
        used_three_cell.add(target)

move_three-=used_three_cell

# print('-------------------------------------')
# print(len(two_patterns[0]))
# print(len(two_patterns[1]))
# print(len(move_three))
# print(len(already_three))
# print(len(wall_cells[4]))
# print('-------------------------------------')

while move_three:
    target = move_three.pop()
    print(target//n,target%n)
    wall_cells[6].add(target)
    for directory_i,directory_j in directorys:
        next_point=((target//n)+directory_i,(target%n)+directory_j)
        if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
            next_point_decrypt=next_point[0]*n+next_point[1]
            if next_point_decrypt in move_three:
                move_three.remove(next_point_decrypt)
                wall_cells[4].add(next_point_decrypt)
            elif next_point_decrypt in already_three:
                already_three.remove(next_point_decrypt)
                wall_cells[4].add(next_point_decrypt)

used_three_cell = set()

for target in already_three:
    if (target//n not in {0,n-1}) and (target%n not in {0,n-1}) and (target not in used_three_cell):
        print(target//n,target%n)
        wall_cells[6].add(target)
        for directory_i,directory_j in directorys:
            next_point=((target//n)+directory_i,(target%n)+directory_j)
            if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
                next_point_decrypt=next_point[0]*n+next_point[1]
                if next_point_decrypt in already_three and next_point_decrypt not in used_three_cell:
                    used_three_cell.add(next_point_decrypt)
                    wall_cells[4].add(next_point_decrypt)
        used_three_cell.add(target)

already_three-=used_three_cell

while already_three:
    target = already_three.pop()
    print(target//n,target%n)
    wall_cells[6].add(target)
    for directory_i,directory_j in directorys:
        next_point=((target//n)+directory_i,(target%n)+directory_j)
        if 0<=next_point[0]<=n-1 and 0<=next_point[1]<=n-1:
            next_point_decrypt=next_point[0]*n+next_point[1]
            if next_point_decrypt in already_three:
                already_three.remove(next_point_decrypt)
                wall_cells[4].add(next_point_decrypt)

used_four_cell=set()

for cell in wall_cells[4]:
    if cell//n not in {0,n-1} and cell%n not in {0,n-1}:
        print(cell//n,cell%n)
        wall_cells[6].add(target)
        used_four_cell.add(cell)

wall_cells[4]-=used_four_cell

while wall_cells[4]:
    target = wall_cells[4].pop()
    print(target//n,target%n)
    wall_cells[6].add(target)
