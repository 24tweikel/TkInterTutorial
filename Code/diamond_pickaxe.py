import tkinter as tk

def rgb(rgb):

    return '#%02x%02x%02x' % rgb

window = tk.Tk()

window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)
window.title("Diamond Pickaxe")

canvas = tk.Canvas(window, width=400, height=400)

canvas.create_rectangle(75, 50, 275, 100, fill=rgb((0, 191, 255)))
canvas.create_rectangle(300, 125, 350, 325, fill=rgb((0, 191, 255)))
canvas.create_rectangle(300, 50, 350, 100, fill=rgb((128, 0, 0)))
canvas.create_rectangle(200, 125, 275, 200, fill=rgb((128, 0, 0)))
canvas.create_rectangle(125, 200, 200, 275, fill=rgb((128, 0, 0)))
canvas.create_rectangle(50, 275, 125, 350, fill=rgb((128, 0, 0)))

canvas.pack()

window.mainloop()
