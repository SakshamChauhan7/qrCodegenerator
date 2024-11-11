import tkinter as tk

r = tk.Tk()
r.geometry("400x400")
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)

r.mainloop()