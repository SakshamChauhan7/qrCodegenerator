import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

# Function to generate QR Code
def generate_qr():
    data = entry_data.get()
    filename = entry_filename.get()
    
    if not data or not filename:
        messagebox.showerror("Error", "Both fields are required!")
        return

    # Create QR Code
    qr = qrcode.QRCode(
        version=2,
        box_size=20,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="green", back_color="black")

    # Save the QR Code image
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", f"QR code saved as {file_path}")
        show_qr(img)

# Function to display the generated QR code
def show_qr(img):
    img = img.resize((200, 200), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# Set up the main application window
app = tk.Tk()
app.title("QR Code Generator")
app.geometry("400x500")
app.resizable(False, False)

# Widgets for user input
tk.Label(app, text="Enter the link or text for QR Code:", font=("Arial", 12)).pack(pady=10)
entry_data = tk.Entry(app, font=("Arial", 12), width=30)
entry_data.pack(pady=5)

tk.Label(app, text="Enter the file name (without extension):", font=("Arial", 12)).pack(pady=10)
entry_filename = tk.Entry(app, font=("Arial", 12), width=30)
entry_filename.pack(pady=5)

# Generate Button
generate_btn = tk.Button(app, text="Generate QR Code", font=("Arial", 12), command=generate_qr)
generate_btn.pack(pady=20)

# Label to show the QR code
qr_label = tk.Label(app)
qr_label.pack(pady=20)

# Run the application
app.mainloop()
