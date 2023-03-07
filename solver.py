sudoku = [[9, 0, 0, 4, 1, 5, 0, 7, 8],
          [1, 8, 5, 7, 0, 0, 0, 0, 9],
          [3, 0, 0, 0, 0, 8, 5, 6, 0],
          [0, 1, 0, 3, 9, 0, 7, 4, 0],
          [0, 0, 0, 1, 0, 0, 0, 3, 0],
          [0, 0, 3, 0, 0, 4, 0, 9, 0],
          [5, 0, 1, 6, 7, 0, 0, 8, 0],
          [8, 0, 0, 0, 0, 9, 6, 0, 0],
          [6, 4, 0, 0, 0, 1, 2, 5, 0]]


# solves the sudoku
def solve(board):
    cell_coordinates = is_free(board)
    if cell_coordinates:
        r, c = cell_coordinates

        for num in range(1, 10):
            if is_valid(r, c, num, board):
                board[r][c] = num

                if solve(board):
                    return True

                board[r][c] = 0

        return False

    return True


# gets the coordinates of the first cell in the 3x3 box, that is to be checked
def get_box_coordinates(r, c):
    x = (r // 3) * 3
    y = (c // 3) * 3
    return x, y


# checks if the number is valid solution for the cell
def is_valid(r, c, number, board):
    # is the number unique for the row
    for i in range(len(board[0])):
        if board[r][i] == number:
            return False

    # is the number unique for the column
    for i in range(len(board)):
        if board[i][c] == number:
            return False

    # is the number unique for the 3x3 box
    x, y = get_box_coordinates(r, c)
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if board[i][j] == number:
                return False

    return True


# returns the coordinates of the first empty cell, if there is one
def is_free(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return r, c

    return None


# prints the sudoku as a board
def print_sudoku(board):
    print(' ')
    for r in range(len(board)):
        if r % 3 == 0 and r != 0:
            print('-------------------------')

        for c in range(len(board[0])):
            if c % 3 == 0:
                print('| ', end='')

            if c == len(board[0]) - 1:
                print(str(board[r][c]) + ' |')
            else:
                print(str(board[r][c]) + ' ', end='')


solve(sudoku)
print_sudoku(sudoku)
