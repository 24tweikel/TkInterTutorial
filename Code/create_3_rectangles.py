#########################################################################################
#########################################################################################
#                  ____    _____           _                    _                       #
#                 |___ \  |  __ \         | |                  | |                      #
#                   __) | | |__) |___  ___| |_ __ _ _ __   __ _| | ___  ___             #
#                  |__ <  |  _  // _ \/ __| __/ _` | '_ \ / _` | |/ _ \/ __|            #
#                  ___) | | | \ \  __/ (__| || (_| | | | | (_| | |  __/\__ \            #
#                 |____/  |_|  \_\___|\___|\__\__,_|_| |_|\__, |_|\___||___/            #
#                                                          __/ |                        #
#                                                         |___/                         #
#########################################################################################
#########################################################################################

import tkinter as tk

window = tk.Tk()

window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)
window.title("Create 3 Rectangles")

canvas = tk.Canvas(window, width=400, height=400)

canvas.create_rectangle(0, 200, 100, 400, fill="black")
canvas.create_rectangle(100, 0, 200, 200, fill="black")
canvas.create_rectangle(200, 200, 400, 400, fill="black")

canvas.pack()

window.mainloop()