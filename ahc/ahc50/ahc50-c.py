

n,m=map(int,input().split())
grid=[list(input()) for _ in range(n)]


directorys=[(0,1),(1,0),(-1,0),(0,-1)]
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

for i in range(5):
    while wall_cells[i]:
        target = wall_cells[i].pop()
        print(target//n,target%n)
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
