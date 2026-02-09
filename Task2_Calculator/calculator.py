# Task 2: Calculator

import tkinter as tk

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())   
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def create_button(text, row, col, command, bg="#484746", fg="white"):
    tk.Button(root, text=text, width=6, height=2, font=("Arial", 18),
              bg=bg, fg=fg, command=command).grid(row=row, column=col, padx=5, pady=5)

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("400x500")
root.configure(bg="#333")  

display = tk.Entry(root, width=20, font=("Arial", 24),
                   borderwidth=8, relief="sunken",
                   bg="#f0f0f0", fg="#000", justify="right")
display.grid(row=0, column=0, columnspan=4, pady=10)

for (text, row, col) in [
    ('7',1,0), ('8',1,1), ('9',1,2),
    ('4',2,0), ('5',2,1), ('6',2,2),
    ('1',3,0), ('2',3,1), ('3',3,2),
    ('0',4,0), ('.',4,1)
]:
    create_button(text, row, col, lambda t=text: button_click(t))

for (text, row, col) in [
    ('/',1,3), ('',2,3), ('-',3,3), ('+',4,2)
]:
    create_button(text, row, col, lambda t=text: button_click(t), bg="#FBBF47")

create_button('=', 4, 3, calculate, bg="#2196F3")

create_button('C', 5, 0, clear_display, bg="#f44336")

root.mainloop()