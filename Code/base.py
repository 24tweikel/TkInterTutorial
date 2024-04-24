import tkinter as tk

def rgb(rgb):

    return '#%02x%02x%02x' % rgb

window = tk.Tk()

window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)

window.mainloop()