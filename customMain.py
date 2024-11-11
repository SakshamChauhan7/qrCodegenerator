from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from tkinter import filedialog
import qrcode

ctk.set_default_color_theme("dark-blue")

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
        


#Window Schematics

app = ctk.CTk()
app.title("QRcode Gen")
app.geometry("647x400") #golden ratio
app.resizable(False,False)

#Main label at lop
ctk.CTkLabel(app,font=('calibre',25,"bold"),text= "Welcome To QRcode Gen By Sam").pack(pady = 60)

#data label and entry
linkLabel =CTkLabel(app, font=('calibre',20),text= "Enter the Link or Info  ")
linkLabel.place(x=50,y=150)

entry_data = CTkEntry(app,width=350,font=('calibre',17))
entry_data.place(x=250,y=150)


#pathName label and entry

fileLabel =CTkLabel(app, font=('calibre',20),text= "Enter the File Name    ")
fileLabel.place(x= 50,y=200)

entry_file= CTkEntry(app,width=350,font=('calibre',17))
entry_file.place(x=250,y=200)


#button to generate
gen_button = CTkButton(app,width=50,height=40, corner_radius= 10,font=('calibre',20),text="Generate",command=gen_qr)
gen_button.place(x=500,y=250)



app.mainloop()