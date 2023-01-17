class Sudoku:
    def __init__(self, row, col, num):
        self.row = row
        self.col = col
        self.num = num
    grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]
    def possible(self):
        for i in range(0, 9):
            if Sudoku.grid[self.row][i] == self.num:
                return False
        for i in range(0, 9):
            if Sudoku.grid[i][self.col] == self.num:
                return False
        x = (self.row // 3) * 3
        y = (self.col // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if Sudoku.grid[x + i][y + j] == self.num:
                    return False
        return True

def solve():
    for row in range(0, 9):
        for col in range(0, 9):
            if Sudoku.grid[row][col] == 0:
                for num in range(1, 10):
                    sudoku = Sudoku(row, col, num)
                    if sudoku.possible() == True:
                        Sudoku.grid[row][col] = num
                        solve()
                        Sudoku.grid[row][col] = 0
                return
    for i in range (0, len(Sudoku.grid)):
        temp = Sudoku.grid[i]
        print(temp)
    input('More possible solutions')
solve()

