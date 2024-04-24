import tkinter as tk

window = tk.Tk()

window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)
window.title("Pickaxe")

canvas = tk.Canvas(window, width=400, height=400)

canvas.create_rectangle(75, 50, 275, 100, fill="black")
canvas.create_rectangle(300, 125, 350, 325, fill="black")
canvas.create_rectangle(300, 50, 350, 100, fill="black")
canvas.create_rectangle(200, 125, 275, 200, fill="black")
canvas.create_rectangle(125, 200, 200, 275, fill="black")
canvas.create_rectangle(50, 275, 125, 350, fill="black")

canvas.pack()

window.mainloop()
