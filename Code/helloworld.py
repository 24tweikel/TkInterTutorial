import tkinter as tk
from tkinter import messagebox

def button_handler():

    messagebox.showinfo("Hello", "Hello, World!")

window = tk.Tk()

window.geometry("300x300")
window.minsize(300, 300)
window.maxsize(300, 300)

button = tk.Button(window, text="Click Me!", command=button_handler)
button.place(x=150, y=150)

window.mainloop()
