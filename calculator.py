from tkinter import *

# Function to update display
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear display
def clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate expression
def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Main window
root = Tk()
root.title("Simple Calculator")
root.configure(background="black")

expression = ""

# Variable to store the input expression
input_text = StringVar()

# Entry widget to display the input expression
input_entry = Entry(root, textvariable=input_text, font=("Helvetica", 20, "bold"), bd=20, insertwidth=4, bg="grey", justify="right")
input_entry.grid(columnspan=4)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("/", 4, 3)
]

# Create buttons
for (text, row, col) in buttons:
    button = Button(root, text=text, font=("Helvetica", 20, "bold"), bg="white", fg="black", height=1, width=3)
    button.grid(row=row, column=col, padx=10, pady=10)
    
    # Button command
    if text == "C":
        button.config(command=clear)
    elif text == "=":
        button.config(command=equal)
    else:
        button.config(command=lambda text=text: button_click(text))

root.mainloop()
