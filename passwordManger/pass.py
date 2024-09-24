import tkinter as tk
import random
import string
import pyperclip

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
    """
    Generates a strong password based on the specified criteria.

    Args:
        length (int): The desired length of the password.
        include_uppercase (bool): Whether to include uppercase letters.
        include_lowercase (bool): Whether to include lowercase letters.
        include_numbers (bool): Whether to include numbers.
        include_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password.
    """

    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    try:
        password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
        password_label.config(text=password)
        copy_button.config(state=tk.NORMAL)  # Enable the copy button
    except ValueError:
        password_label.config(text="Please select at least one character type.")

def copy_password():
    pyperclip.copy(password_label.cget("text"))

# Create the main window
window = tk.Tk()
window.title("Password Manager")

# Create GUI elements
length_label = tk.Label(window, text="Password Length:")
length_entry = tk.Entry(window)
uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(window, text="Include Uppercase", variable=uppercase_var)
lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(window, text="Include Lowercase", variable=lowercase_var)
numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(window, text="Include Symbols", variable=symbols_var)
generate_button = tk.Button(window, text="Generate Password", command=generate_password_gui)
password_label = tk.Label(window, text="")
copy_button = tk.Button(window, text="Copy Password", command=copy_password, state=tk.DISABLED)

# Arrange GUI elements
length_label.grid(row=0, column=0)
length_entry.grid(row=0, column=1)
uppercase_check.grid(row=1, column=0)
lowercase_check.grid(row=2, column=0)
numbers_check.grid(row=3, column=0)
symbols_check.grid(row=4, column=0)
generate_button.grid(row=5, column=0)
password_label.grid(row=6, column=0, columnspan=2)
copy_button.grid(row=5, column=1)

# Run the GUI
window.mainloop()