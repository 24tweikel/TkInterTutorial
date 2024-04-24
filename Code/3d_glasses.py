import tkinter as tk 

def rgb(rgb):

    return '#%02x%02x%02x' % rgb

window = tk.Tk()

window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)
window.title("3D Glasses")

canvas = tk.Canvas(window, width=400, height=400)

# Create Face
canvas.create_rectangle(0, 0, 400, 400, fill=rgb((210, 180, 140)))

# Create Eyes
canvas.create_rectangle(125, 80, 155, 160, fill="black")
canvas.create_rectangle(245, 80, 275, 160, fill="black")

# Create Mouth
canvas.create_rectangle(50, 200, 75, 275, fill="black")
canvas.create_rectangle(75, 275, 325, 315, fill="black")
canvas.create_rectangle(325, 200, 350, 275, fill="black")

# Create Glasses Frame
canvas.create_rectangle(0, 100, 60, 140, fill="white", width=0)
canvas.create_rectangle(185, 110, 215, 130, fill="white", width=0)
canvas.create_rectangle(340, 100, 400, 140, fill="white", width=0)

# Create Glasses
canvas.create_rectangle(60, 60, 185, 180, fill="red", stipple="gray50", width=0)
canvas.create_rectangle(215, 60, 340, 180, fill="blue", stipple="gray50", width=0)

canvas.pack()

window.mainloop()
