from tkinter import messagebox
import qrcode 
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


def gen_qr():
    data = entry_data.get()
    file = entry_file.get()

    if not data or not file:
        messagebox.showerror("Error", "Both fields are required!")
        return
    
    qr = qrcode.QRCode(
        version=2,
        box_size=20,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="green", back_color="black")

    #saving files
    file_path = filedialog.asksaveasfilename(initialfile=file,defaultextension=".png",filetypes=[("PNG files", "*.png")])

    if file_path:
        img.save(file_path)
        messagebox.showinfo(message="File saved successfully!!")
        app.destroy()
        


#Just window schematics
app = tk.Tk()
app.title("QRcode Gen")
app.geometry("647x400") #golden ratio
app.resizable(False,False)


#working on label here

tk.Label(app,font=('calibre',20),text= "Welcome QRcode Gen By Sam").pack(pady = 80)

#fileName label and entry
linkLabel = Label(app, font=('calibre',15),text= "Enter the Link or Info: ")
linkLabel.place(x=40,y=150)

entry_data = tk.Entry(app,width=30,font=('calibre',12))
entry_data.place(x=300,y=152)


#pathName label and entry

fileLabel =Label(app, font=('calibre',15),text= "Enter the file Name: ")
fileLabel.place(x= 40,y=200)

entry_file= tk.Entry(app,width=30,font=('calibre',12))
entry_file.place(x=300,y=202)

#button to generate
gen_button = tk.Button(app, font=('calibre',12),text="Generate",command=gen_qr)
gen_button.place(x=500,y=250)

app.mainloop()
