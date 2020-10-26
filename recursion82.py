def path(grid, x, y):
    if x == len(grid[x]) and y == len(grid):
        return "Finish"
    if x+1 < len(grid[x]):
        if grid[y][x+1] != 0:
            return path(grid, x + 1, y)
    if y+1 < len(grid):
        if grid[y+1][x] != 0:
            return path(grid, x, y+1)