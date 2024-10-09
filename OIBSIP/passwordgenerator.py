
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate password based on user options
def generate_password():


    # Get user preferences
    length = length_var.get()
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    # Ensure at least one character type is selected
    if not (include_upper or include_lower or include_digits or include_special):
        messagebox.showerror("Error", "Please select at least one character type!")
        return

    # Build the character set based on user preferences
    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the generated password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Initialize the main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")

# Variables to store user preferences
length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

# Create widgets for password length and options
tk.Label(root, text="Password Length:").pack(pady=5)
length_spinbox = tk.Spinbox(root, from_=8, to_=32, textvariable=length_var, width=5)
length_spinbox.pack(pady=5)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(pady=5)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(pady=5)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(pady=5)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(pady=5)

# Entry widget to display generated password
password_entry = tk.Entry(root, width=40, font=("Arial", 14))
password_entry.pack(pady=20)

# Buttons to generate password and copy to clipboard
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
