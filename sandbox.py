import tkinter as tk
from tkinter import messagebox


# Create the main application window
app = tk.Tk()

# Set the title of the window
app.title("My First Tkinter App")

# Set the window size
app.geometry("400x300")

# Prevent the window from being resized
app.resizable(False, False)

#code here




# Label to display text
label = tk.Label(app, text="Enter your name:", font=("Arial", 14))
label.pack(pady=10)

# Entry widget for user input
entry = tk.Entry(app, font=("Arial", 12))
entry.pack(pady=5)

# Function to run when button is clicked
def greet():
    user_name = entry.get()
    if user_name:
        messagebox.showinfo("Greeting", f"Hello, {user_name}!")
    else:
        messagebox.showerror("Error", "Please enter your name.")

# Button widget
button = tk.Button(app, text="Greet Me", font=("Arial", 12), command=greet)
button.pack(pady=20)
app.mainloop()