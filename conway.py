from typing import List
from random import choice

GRID = List[List[int]]

def initial_condition(grid_size: int) -> GRID:
    grid = []
    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            cell_value = choice([0, 1])
            row.append(cell_value)
        grid.append(cell_value)
    return grid

def get_next_state(grid: GRID, x_position: int, y_position: int) -> int:
    count_neighbors = 0
    status = grid[y_position][x_position]
    grid_size = len(grid)
    for y in [y_position-1, y_position, y_position+1]:
        for x in [x_position-1, x_position, x_position+1]:
            if x > 0 and x < (grid_size - 1 ) and y > 0 and y < (grid_size - 1):
                count_neighbors += grid[y][x]
    count_neighbors -= status
    if status == 1 and (count_neighbors == 2 or count_neighbors ==3):
        return 1
    if status == 0 and count_neighbors == 3:
        return 1
    return 0






    