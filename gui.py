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
            self.root, text='Reset', font=('TkTextFont', 10), command=self.reset_buttons)
        self.solve_btn.pack(padx=5, pady=5)

        # make the infinite loop for displaying the app
        self.root.mainloop()

    def reset_buttons(self):
        buttons = self.frame.winfo_children()
        for button in buttons:
            button['text'] = ''

    # determine which button is clicked and change its text content accordingly
    @staticmethod
    def on_click(clicked_button):
        print(clicked_button)
        print(str(clicked_button)[-2:])
        number = clicked_button['text']
        if not number:
            number = 1
        elif number == 9:
            number = ''
        else:
            number = int(number) + 1
        clicked_button['text'] = number


SudokuGUI()
