import tkinter as tk

# Function to update input field
def click(event):
    global expression
    expression += str(event.widget.cget("text"))
    input_text.set(expression)

# Function to clear input
def clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate expression
def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Error")
        expression = ""

# Main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x450")

expression = ""
input_text = tk.StringVar()

# Input field
input_frame = tk.Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bd=0, bg="#eee", justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # Internal padding

# Buttons
button_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for i in range(4):
    for j in range(4):
        btn_text = buttons[i][j]
        if btn_text == "=":
            btn = tk.Button(button_frame, text=btn_text, width=10, height=3, bd=0, bg="#4CAF50", fg="white", command=calculate)
        elif btn_text == "C":
            btn = tk.Button(button_frame, text=btn_text, width=10, height=3, bd=0, bg="#f44336", fg="white", command=clear)
        else:
            btn = tk.Button(button_frame, text=btn_text, width=10, height=3, bd=0, bg="#fff", fg="black")
            btn.bind("<Button-1>", click)
        btn.grid(row=i, column=j, padx=1, pady=1)

root.mainloop()
