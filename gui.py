import tkinter as tk


class SudokuGUI:
    def __init__(self):
        # initialize the root
        self.root = tk.Tk()
        self.root.title('Sudoku solver')

        # initialize label with instructions
        self.instructions = tk.Label(
            self.root, text='Instructions for using the application', font=('TkTextFont', 12))
        self.instructions.pack(padx=5, pady=5)

        # initialize the frame
        self.frame = tk.Frame(self.root, width=500, height=600)
        self.frame.pack()

        # initialize sudoku grid buttons
        for i in range(9):
            for j in range(9):
                self.button = tk.Button(
                    self.frame, text='', height=2, width=5, command=self.on_click)
                self.button.grid(column=i, row=j)

        # initialize check button
        self.check_btn = tk.Checkbutton(
            self.root, text='reveal entire sudoku', font=('TkTextFont', 10))
        self.check_btn.pack(padx=5, pady=5)

        # initialize solve button
        self.solve_btn = tk.Button(
            self.root, text='Solve', font=('TkTextFont', 10))
        self.solve_btn.pack(padx=5, pady=5)

        # end command
        self.root.mainloop()

    def on_click(self):
        print('button clicked')


SudokuGUI()
