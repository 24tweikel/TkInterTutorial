#########################################################################################
#########################################################################################
#                           _____                                                       #
#                          / ____|                                                      #
#                         | |     __ _ _ ____   ____ _ ___                              #
#                         | |    / _` | '_ \ \ / / _` / __|                             #
#                         | |___| (_| | | | \ V / (_| \__ \                             #
#                          \_____\__,_|_| |_|\_/ \__,_|___/                             #
#########################################################################################
#########################################################################################

import tkinter as tk 

window = tk.Tk()

window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)
window.title("Create A Canvas")

# Create a Canvas the size of window
canvas = tk.Canvas(window, width=400, height=400)

# Create two rectangles 
canvas.create_rectangle(0, 0, 200, 200, fill="black")
canvas.create_rectangle(200, 200, 400, 400, fill="black")

# Pack the Canvas so that the rectangles show up
canvas.pack()

window.mainloop()
