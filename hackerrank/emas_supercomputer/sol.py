def find_max_plus(grid, n, m):
    max_plus = 0
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == 'G'): # eligible plus center
                plus = 0
                for t, r, b, l in zip(range(i, -1, -1), range(j, m), range(i, n), range(j, -1, -1)):
                    if (grid[t][j] == 'G' and grid[i][r] == 'G' and grid[b][j] == 'G' and grid[i][l] == 'G'):
                        plus += 1
                    else:
                        break
                if (plus > max_plus):
                    max_plus = plus
                    
    return max_plus
                

def find_max_plus_prod(grid, n, m):
    max_prod = 0
    # for each possible plus, find the max possible plus
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == 'G'): # eligible plus center
                pcount = 0
                # copy grid
                new_grid = [list(grid[k]) for k in range(n)]
                for t, r, b, l in zip(range(i, -1, -1), range(j, m), range(i, n), range(j, -1, -1)):
                    if (grid[t][j] == 'G' and grid[i][r] == 'G' and grid[b][j] == 'G' and grid[i][l] == 'G'):
                        pcount += 1
                        new_grid[t][j] = new_grid[i][r] = new_grid[b][j] = new_grid[i][l] = 'B'
                        second_plus = find_max_plus(new_grid, n, m)
                        prod = (4 * (pcount - 1) + 1) * (4 * (second_plus - 1) + 1)
                        if (prod > max_prod):
                            max_prod = prod
                    else:
                        break
                        
                
    return max_prod

n, m = map(int, input().split())
grid = [[] for i in range(n)]
for i in range(n):
    grid[i] = list(map(str, input()))
print(find_max_plus_prod(grid, n, m))
