#########################################################################################
#########################################################################################
#                          _______ _    _____       _                                   #
#                         |__   __| |  |_   _|     | |                                  #
#                            | |  | | __ | |  _ __ | |_ ___ _ __                        #
#                            | |  | |/ / | | | '_ \| __/ _ \ '__|                       #
#                            | |  |   < _| |_| | | | ||  __/ |                          #
#                            |_|  |_|\_\_____|_| |_|\__\___|_|                          #  
#########################################################################################
#########################################################################################

# Import the tkinter package
import tkinter as tk 
# "import tkinter as tk" allows you to use tk.Tk() instead of tkinter.Tk()

window = tk.Tk()

# Set window size to the size of the CMU Academy canvas size
window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)
window.title("Open A Window")

# Keep window open until the X is clicked
window.mainloop()
















