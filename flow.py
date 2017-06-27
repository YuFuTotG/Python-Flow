
import numpy as np

# Reading in problem instance
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
gridLeft = [[0, i] for i in reversed(range(0, height-1))]
gridOuter = gridTop + gridRight + gridBottom + gridLeft

# Generate list of Colour Cells
cellDict = {}
coordDict = {}
for i in range(width):
    for j in range(height):
        if (grid[i][j] != '0'):
            if (grid[i][j] in cellDict):
                cellDict[grid[i][j]].add((i, j))
            else:
                cellDict[grid[i][j]] = {(i, j)}
            coordDict[(i,j)] = grid[i][j]



def find_path(grid, cycle):
    prevCol = -1
    trace = []
    for c in cycle:
        cell = grid[c[0]][c[1]]
        trace.append(c)
        #print(trace)
        if prevCol == cell:
            for x in trace:
                grid[x[0]][x[1]] = cell
            return True
        elif cell != '0':
            prevCol = cell
            trace = []
    return False


class FlowCell():
    def __init__(self, x, y, col):
        self.p1 = (x, y)
        self.col = col

    def AddPoint (self, x, y):
        self.p2 = (x, y)

    def PrintCell(self):
        print (self.col),
        print (p2),
        print (p1)

        

class FlowGrid():
    def __init__(self, fname):
        # Reading in problem instance
        with open(fname) as f: g = f.readlines()
        g = [x.strip() for x in g] 
        self.grid = [list(x) for x in g]

        # Generate list of Colour Cells

        # find dimentions of grid
        self.height = len(self.grid)
        self.width = len(self.grid[0])

        # Generate co-ordinates of outer row
        gridTop = [[i, 0] for i in range(width)]
        gridRight = [[width-1, i] for i in range(1, height-1)]
        gridBottom = [[i, height-1] for i in reversed(range(width))]
        gridLeft = [[0, i] for i in reversed(range(1, height-1))]
        self.outerGrid = gridTop + gridRight + gridBottom + gridLeft

    # Find neibours of a cell
    #def find_path(cell, boundaries):





# Test output
for x in grid: print(x)
print("\n")
print(gridOuter)
print(find_path(grid, gridOuter))
print("\n")
for x in grid: print(x)
