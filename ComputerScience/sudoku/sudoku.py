board1 =     [[0,2,9,0,0,0,4,0,0],
              [0,0,0,5,0,0,1,0,0],
              [0,4,0,0,0,0,0,0,0],
              [0,0,0,0,4,2,0,0,0],
              [6,0,0,0,0,0,0,7,0],
              [5,0,0,0,0,0,0,0,0],
              [7,0,0,3,0,0,0,0,5],
              [0,1,0,0,9,0,0,0,0],
              [0,0,0,0,0,0,0,6,0]]
backtracks = 0

# finds next empty cell
def findNextCellToFill(grid: [[int]]) -> (int,int):
   for i in range(9):
      for j in range(9):
         if grid[i][j] == 0:
            return i,j
   return -1,-1

# chec if the current choice (e in cell i,j) violates any contraints
def isValid(grid: [[int]], i: int, j: int, e: int) -> bool:
   rowOk = all([e != grid[i][x] for x in range(9)])
   if rowOk:
      colOk = all([e != grid[x][j] for x in range(9)])
      if colOk:
        secTopX, secTopY = 3*(i//3), 3*(j//3)
        for x in range(secTopX, secTopX+3):
           for y in range(secTopY, secTopY+3):
              if grid[i][j] == e:
                 return False
        return True
   return False

def solveSudoku(grid: [[int]], i: int = 0, j: int = 0) -> bool:
   global backtracks
   i,j = findNextCellToFill(grid)

   # if there are no empty cells and we get here, grid must be a solution
   if i == -1:
      return True
   for e in range(1,10):
      if isValid(grid,i,j,e):
         grid[i][j] = e
         # check if that choice renders a solution
         if solveSudoku(grid,i,j):
            return True
         backtracks += 1
         #grid[i][j] = 0
   grid[i][j] = 0
   return False

def printSudoku(grid: [[int]]) -> None:
   numrow = 0
   for row in grid:
      if numrow % 3 == 0 and numrow != 0:
         print(' ')
      print(row[0:3], ' ', row[3:6], ' ', row[6:9])
      numrow += 1

printSudoku(board1)
if solveSudoku(board1):
   print(f"Solution ({backtracks}):")
   printSudoku(board1)
