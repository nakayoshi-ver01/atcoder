grid=[['.' for _ in range(40)] for _ in range(40)]

counter=0
for i in range(20):
    if i%2==1:
        for j in range(i,40-i):
            grid[i][j]='#'
            grid[39-i][j]='#'
            grid[j][i]='#'
            grid[j][39-i]='#'
            counter+=4
        counter-=4

print(40,counter)
for i in grid:
    print(''.join(i))