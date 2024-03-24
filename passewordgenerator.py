import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showwarning("Warning", "Password length should be at least 8 characters.")
            return
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number for password length.")
        return

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Ensure the password contains at least one of each character type
    password_characters = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(symbols)
    ]

    # Fill the rest of the password with random characters
    password_characters += random.choices(lowercase + uppercase + numbers + symbols, k=length - 4)

    # Shuffle the password characters to mix the order
    random.shuffle(password_characters)

    password = ''.join(password_characters)
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create main window
root = tk.Tk()
root.title("Random Password Generator")

# Password length label and entry
length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12))
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root, font=("Helvetica", 12))
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12), command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Password entry
password_label = tk.Label(root, text="Generated Password:", font=("Helvetica", 12))
password_label.grid(row=2, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, font=("Helvetica", 12))
password_entry.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
