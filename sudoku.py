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


def if_possible(x,y,n):
   for i in range(9):
      if n == grid[x][i]:
         return False
   for i in range(9):
      if n == grid[i][y]:
         return False
   return True
         
         
print(if_possible(1, 3, 3))
print(np.matrix(grid))