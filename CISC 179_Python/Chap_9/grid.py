grid[<row>][<column>]

from grid import Grid
grid = Grid(rows = 3, columns = 4, fillValue = 0)
print(grid)
grid[1][2] = 5
print(grid)
print(grid.find(6))
for row in range(grid.getHeight()):
    for column in range(grid.getWidth()):
        grid[row][column] = (row, column)
print(grid)
