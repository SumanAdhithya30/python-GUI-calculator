import tkinter as tk

def press_key(key):
    global expression
    expression = expression + str(key)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def evaluate():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

expression = ""

root = tk.Tk()
root.title("Simple Calculator")

equation = tk.StringVar()

display = tk.Entry(root, textvariable=equation, font=('Arial', 20), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16), command=evaluate).grid(row=row, column=col, padx=5, pady=5)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16), command=clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16), command=lambda key=button: press_key(key)).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
