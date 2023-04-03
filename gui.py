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
            self.root, text='Solve', font=('TkTextFont', 10))
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

    # returns the sudoku board from the user input
    def get_board(self):
        sudoku = []
        buttons = self.frame.winfo_children()
        for button in buttons:
            if button['text'] == '':
                sudoku.append(0)
            else:
                sudoku.append(int(button['text']))
        print(sudoku)

        board = [sudoku[i:i + 9] for i in range(0, len(sudoku), 9)]

        return board

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
