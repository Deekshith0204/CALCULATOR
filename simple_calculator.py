import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.expression = ""
        self.input_text = tk.StringVar()

        # Entry to display input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        self.input_field = tk.Entry(
            self.input_frame, textvariable=self.input_text, font=('Arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right'
        )
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        # Buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for (text, row, col, *span) in buttons:
            colspan = span[0] if span else 1
            button = tk.Button(
                self.buttons_frame, text=text, width=9 if text == '=' else 5, height=2, font=('Arial', 14),
                command=lambda t=text: self._on_button_click(t)
            )
            button.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2)

    def _on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = SimpleCalculator(root)
    root.mainloop()