import tkinter as tk

INSTRUCTIONS_TEXT = '''Instructions: insert your sudoku numbers by clicking with the left mouse 
button on the cell, that you want to edit. Each click adds 1 to the cell\'s 
value. If you want to reveal the entire sudoku board after solving it, click 
the checkbox under the board. Alternatively, you can reveal cells by clicking 
on them after you have solved the board.'''


class SudokuGUI:
    def __init__(self):
        # initialize the root
        self.root = tk.Tk()
        self.root.title('Sudoku solver')
        self.root.geometry('500x600')

        # initialize label with instructions
        self.instructions = tk.Label(
            self.root, text=INSTRUCTIONS_TEXT, font=('TkTextFont', 10))
        self.instructions.pack(padx=10, pady=10)

        # initialize the frame
        self.frame = tk.Frame(self.root, width=500, height=600)
        self.frame.pack()

        # initialize sudoku grid buttons
        for i in range(9):
            for j in range(9):
                self.button = tk.Button(
                    self.frame, text='', height=2, width=5, name=f'{i}{j}', relief='solid')
                self.button.grid(row=i, column=j)
                self.button['command'] = lambda btn=self.button: self.on_click(
                    btn)

        # initialize check button
        self.check_btn = tk.Checkbutton(
            self.root, text='reveal entire sudoku', font=('TkTextFont', 10))
        self.check_btn.pack(padx=5, pady=5)

        # initialize solve button
        self.solve_btn = tk.Button(
            self.root, text='Solve', font=('TkTextFont', 10), command=self.solve_btn_action)
        self.solve_btn.pack(padx=5, pady=5)

        # initialize reset button
        self.solve_btn = tk.Button(
            self.root, text='Reset', font=('TkTextFont', 10), command=self.reset)
        self.solve_btn.pack(padx=5, pady=5)

        # make the infinite loop for displaying the app
        self.root.mainloop()

    # reset the sudoku board
    def reset(self):
        buttons = self.frame.winfo_children()
        for button in buttons:
            button['text'] = ''

    # perform actions on click of solve button
    def solve_btn_action(self):
        board = self.get_board()
        self.solve(board)
        self.populate_sudoku(board)

    # returns the sudoku board from the user input
    def get_board(self):
        sudoku = []
        buttons = self.frame.winfo_children()
        for button in buttons:
            if button['text'] == '':
                sudoku.append(0)
            else:
                sudoku.append(int(button['text']))

        board = [sudoku[i:i + 9] for i in range(0, len(sudoku), 9)]

        return board

    # populates the sudoku board with the correct numbers
    def populate_sudoku(self, board):
        buttons = self.frame.winfo_children()
        counter = 0
        for i in range(9):
            for j in range(9):
                button = buttons[counter]
                if button['text'] == '':
                    button['text'] = board[i][j]
                counter += 1

    # solves the sudoku
    def solve(self, board):
        cell_coordinates = self.is_free(board)
        if cell_coordinates:
            r, c = cell_coordinates

            for num in range(1, 10):
                if self.is_valid(r, c, num, board):
                    board[r][c] = num

                    if self.solve(board):
                        return True

                    board[r][c] = 0

            return False

        return True

    # returns the coordinates of the first empty cell, if there is one
    @staticmethod
    def is_free(board):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 0:
                    return r, c

        return None

    # checks if the number is valid solution for the cell
    @staticmethod
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
        x = (r // 3) * 3
        y = (c // 3) * 3
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if board[i][j] == number:
                    return False

        return True

    # determine which button is clicked and change its text content accordingly
    @staticmethod
    def on_click(clicked_button):
        number = clicked_button['text']
        if not number:
            number = 1
        elif number == 9:
            number = ''
        else:
            number = int(number) + 1
        clicked_button['text'] = number


SudokuGUI()
