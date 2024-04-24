import tkinter as tk

def rgb(rgb):

    return '#%02x%02x%02x' % rgb

window = tk.Tk()

window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)
window.title("France Flag")

canvas = tk.Canvas(window, width=400, height=400)

canvas.create_rectangle(50, 100, 150, 300, fill=rgb((0, 0, 128)))
canvas.create_rectangle(150, 100, 250, 300, fill='white')
canvas.create_rectangle(250, 100, 350, 300, fill=rgb((220, 20, 60)))

canvas.pack()

window.mainloop()