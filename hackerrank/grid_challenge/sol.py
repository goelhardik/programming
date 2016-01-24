def is_column_sorted(grid, j, n):
    for i in range(n - 1):
        if (grid[i][j] > grid[i + 1][j]):   # if column not sorted, return False
            return False
        
    return True

def can_be_lex_sorted(grid, n):
    for i in range(n):
        grid[i] = ''.join(sorted(grid[i]))  # sort each row horizontally
    for j in range(n):
        if (not is_column_sorted(grid, j, n)):  # check if each column is sorted vertically
            return False
        
    return True

# driver code
tests = int(input())
for i in range(tests):
    n = int(input())
    grid = []
    for j in range(n):
        grid.append(str(input()))
    if (can_be_lex_sorted(grid, n)):
        print("YES")
    else:
        print("NO")
