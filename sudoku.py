import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

listb = [[2,3], [4,5]]
def if_possible(x,y,n):
   for i in range(9):
      if n == grid[x][i]:
         return False
   for i in range(9):
      if n == grid[i][y]:
         return False
   x0=(x//3)*3
   y0=(y//3)*3
   for i in range(3):
      for j in range(3):
         if grid[x0+i][y0+j] == n:
            return False
   return True
         
def sudoku_solver():
   for x in range(9):
      for y in range(9):
         if grid[x][y] == 0:
            for n in range(1,10):
               if if_possible(x,y,n):
                  grid[x][y] = n
                  sudoku_solver()
                  grid[x][y] = 0
            return
   print(np.matrix(grid))
			
#print(if_possible(0, 2, 1))
#print(grid[7][5])
print(np.matrix(grid))
print()
sudoku_solver()

