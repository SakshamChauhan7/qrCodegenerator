import qrcode 
import tkinter as tk
from tkinter import * 


def gen_qr():
    qr = qrcode.QRCode(
        version=2,
        box_size=20,
        border=2,
    )


app = tk.Tk()
app.title("QRcode Gen")
app.geometry("400x600")
app.resizable(False,False)


tk.Label(app,text="Welcome to Qrcode Generator")


tk.mainloop()
