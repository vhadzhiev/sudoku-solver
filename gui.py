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
                    self.frame, text='0', height=2, width=5, name=f'{i}{j}')
                self.button.grid(row=i, column=j)
                self.button['command'] = lambda btn=self.button: self.which_button(
                    btn)

        # initialize check button
        self.check_btn = tk.Checkbutton(
            self.root, text='reveal entire sudoku', font=('TkTextFont', 10))
        self.check_btn.pack(padx=5, pady=5)

        # initialize solve button
        self.solve_btn = tk.Button(
            self.root, text='Solve', font=('TkTextFont', 10))
        self.solve_btn.pack(padx=5, pady=5)

        # make the infinite loop for displaying the app
        self.root.mainloop()

    def on_click(self):
        print(f'{self.button} clicked')

    @staticmethod
    def which_button(clicked_button):
        print(clicked_button)
        number = clicked_button['text']
        if not number:
            clicked_button['text'] = 1
        elif number == 9:
            clicked_button['text'] = ''
        else:
            number += 1
        clicked_button['text'] = number


SudokuGUI()
