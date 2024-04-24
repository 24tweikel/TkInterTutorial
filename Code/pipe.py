import tkinter as tk

def rgb(rgb):

    return '#%02x%02x%02x' % rgb

window = tk.Tk()

window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)
window.title("Pipe")

canvas = tk.Canvas(window, width=400, height=400)

canvas.create_rectangle(0, 0, 400, 275, fill=rgb((135, 206, 235)))
canvas.create_rectangle(0, 275, 400, 400, fill=rgb((210, 180, 140)))
canvas.create_rectangle(100, 125, 300, 175, fill=rgb((0, 100, 0)))
canvas.create_rectangle(125, 175, 275, 275, fill=rgb((0, 100, 0)))

canvas.pack()

window.mainloop()