
import numpy as np

fname = "testGrid.txt"
with open(fname) as f:
    grid = f.readlines()
grid = [x.strip() for x in grid] 
grid = [list(x) for x in grid]

# find dimentions of grid
height = len(grid)
width = len(grid[0])

# Generate co-ordinates of outer row
gridTop = [[i, 0] for i in range(width)]
gridRight = [[width-1, i] for i in range(1, height-1)]
gridBottom = [[i, height-1] for i in reversed(range(width))]
gridLeft = [[0, i] for i in reversed(range(1, height-1))]
gridOuter = gridTop + gridRight + gridBottom + gridLeft

for x in grid: print(x)
print("\n")
print(gridOuter)
