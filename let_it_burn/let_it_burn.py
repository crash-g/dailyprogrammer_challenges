import operator

SMOKE = "S"
FIRE = "F"
WALL = "#"
CLOSED_DOOR = "|"
OPEN_DOOR = "/"
DAMAGED_WALL = "="
BROKEN_WALL_DOOR = "_"
EMPTY = " "

FIRE_PASSAGES = [OPEN_DOOR, BROKEN_WALL_DOOR]
ADJACENT_SQUARES = [(0,1),(-1,0),(0,-1),(1,0)]

def burn(fileName):
    with open(fileName, "r") as lines:
        grid = readGrid(lines)
        printGrid(grid)
        line = lines.readline().strip()
        while line:
            coord = tuple(map(int, line.split(" ")))
            if isOnGrid(coord, grid):
                turnToSmoke(coord, grid)
            line = lines.readline().strip()
        printGrid(grid)
            
def readGrid(lines):
    grid = []
    line = lines.readline().strip()
    while line:
        grid.append([])
        for c in line:
            if(c is not "\n"):
                grid[len(grid)-1].append(c)
        line = lines.readline().strip()
    return grid

def printGrid(grid):
    for i in range(0,len(grid)):
        print("".join([grid[i][j] for j in range(0,len(grid[0]))]))
        
def turnToSmoke(coord, grid):
    value = getGridValue(coord, grid)
    if value  == EMPTY:
        setGridValue(coord, grid, SMOKE)
        if(checkIfFireAround(coord, grid)):
            turnToFire(coord, grid)
    elif value == SMOKE:
        turnToFire(coord, grid)

def turnToFire(coord, grid):
    setGridValue(coord, grid, FIRE)
    for square in checkIfSmokeAround(coord, grid):
        turnToFire(square, grid)
    
def checkIfFireAround(coord, grid):
    return len(_checkAround(coord, FIRE, grid)) > 0

def checkIfSmokeAround(coord, grid):
    return _checkAround(coord, SMOKE, grid)

def _checkAround(coord, target, grid):
    neighbors = []
    for direction in ADJACENT_SQUARES:
        square = tuple(map(operator.add, coord, direction))
        while isThere(square, FIRE_PASSAGES, grid):
            square = tuple(map(operator.add, square, direction))
        if isThere(square, target, grid):
            neighbors.append(square)
    return neighbors

def isThere(coord, target, grid):
    if isinstance(target, list):
        return any([isOnGrid(coord, grid) and getGridValue(coord, grid) == t for t in target])
    else:
        return isOnGrid(coord, grid) and getGridValue(coord, grid) == target

def getGridValue(coord, grid):
    return grid[coord[1]][coord[0]]

def setGridValue(coord, grid, value):
    grid[coord[1]][coord[0]] = value

def isOnGrid(coord, grid):
    x = coord[1]
    y = coord[0]
    if x < 0  or x >= len(grid):
        return False
    if y < 0 or y >= len(grid[x]):
        return False
    return True
        
burn("burning_floor.txt")

