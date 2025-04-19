import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Example")

# Create a label
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Create a button
def on_button_click():
    label.config(text="Button Clicked!")

button = ttk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Create an entry widget
entry = ttk.Entry(root)
entry.pack(pady=10)

# Function to get text from entry
def get_text():
    text = entry.get()
    label.config(text=f"You entered: {text}")

# Create a button to get text
get_text_button = ttk.Button(root, text="Get Text", command=get_text)
get_text_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()