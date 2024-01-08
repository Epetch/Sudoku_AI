import numpy as np

test_sudoku = np.array([[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 4],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]],
                       np.int32)


def sudoku_solver(sudoku):
    length = 9
    temp_sudoku = [[[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []],
                   [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []],
                   [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []],
                   [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []],
                   [[], [], [], [], [], [], [], [], []]]

    def mod_temp_sudoku(num, row, col):
        lower_row = (row // 3) * 3
        upper_row = lower_row + 3
        lower_col = (col // 3) * 3
        upper_col = lower_col + 3
        for a in range(length):
            if num in temp_sudoku[row][a]:
                temp_sudoku[row][a].remove(num)
            if num in temp_sudoku[a][col]:
                temp_sudoku[a][col].remove(num)
        for b in range(lower_row, upper_row):
            for c in range(lower_col, upper_col):
                if num in temp_sudoku[b][c]:
                    temp_sudoku[b][c].remove(num)

    def is_valid(row, col, num):
        lower_row = (row // 3) * 3
        upper_row = lower_row + 3
        lower_col = (col // 3) * 3
        upper_col = lower_col + 3
        for a in range(length):
            if a != col and sudoku[row][a] == num:
                return False
            if a != row and sudoku[a][col] == num:
                return False
        for b in range(lower_row, upper_row):
            for c in range(lower_col, upper_col):
                if ((b != row) or (c != col)) and sudoku[b][c] == num:
                    return False
        return True

    for i in range(length):
        for j in range(length):
            for k in range(1, 10):
                temp_sudoku[i][j].append(k)

    for i in range(length):
        for j in range(length):
            if sudoku[i][j] != 0:
                mod_temp_sudoku(sudoku[i][j], i, j)

    def find_zero():
        for a in range(length):
            for b in range(length):
                if sudoku[a][b] == 0:
                    return a, b
        return None

    def loop():
        empty = find_zero()
        if not empty:
            return sudoku  # Base case: solved sudoku
        else:
            row, col = empty
        for i in temp_sudoku[row][col]:
            if is_valid(row, col, i):
                sudoku[row][col] = i
                if row == length - 1 and col == length - 1:
                    return sudoku  # Base case: solved sudoku
                else:
                    result = loop()
                    if result is not None:
                        return result
                    sudoku[row][col] = 0
        return None

    solved_sud = loop()
    if solved_sud is None:
        for i in range(length):
            for j in range(length):
                sudoku[i][j] = -1
        return sudoku
    else:
        return solved_sud


print(sudoku_solver(test_sudoku))
