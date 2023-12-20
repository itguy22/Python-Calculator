import tkinter as tk

root = tk.Tk()
root.title("Calculator")

# Operation functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button click function
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_operation(operation):
    first_number = entry.get()
    global f_num
    global math
    math = operation
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math == "addition":
        entry.insert(0, add(f_num, float(second_number)))
    elif math == "subtraction":
        entry.insert(0, subtract(f_num, float(second_number)))
    elif math == "multiplication":
        entry.insert(0, multiply(f_num, float(second_number)))
    elif math == "division":
        entry.insert(0, divide(f_num, float(second_number)))

def button_clear():
    entry.delete(0, tk.END)

# Buttons for numbers
for i in range(1, 10):
    button = tk.Button(root, text=str(i), padx=40, pady=20, command=lambda i=i: button_click(i))
    button.grid(row=(i-1)//3 + 1, column=(i-1)%3)

# Operation buttons
button_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: button_operation("addition"))
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=lambda: button_operation("subtraction"))
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=lambda: button_operation("multiplication"))
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=lambda: button_operation("division"))

# Equal and clear buttons
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Positioning buttons
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=4, column=0, columnspan=2)

root.mainloop()
