# import tkinter
# from tkinter import messagebox

# window = tkinter.Tk()

# canvasWidget = tkinter.Canvas(window, bg="white", height=512, width=512 )

# coord = 10, 50, 512, 512
# arcObject = canvasWidget.create_arc(coord, start = 0, extent = 270, fill = "red")

# canvasWidget.pack()
# window.mainloop()

import tkinter

# Create the main window
window = tkinter.Tk()
window.title("Red Arc Example")

# Create a canvas widget
canvasWidget = tkinter.Canvas(window, bg="white", height=512, width=512)
canvasWidget.pack()

# Define the coordinates for the arc
coord = 50, 50, 450, 450  # Ensure the arc is within the canvas

# Create the arc on the canvas
canvasWidget.create_arc(coord, start=0, extent=270, fill="red", outline="red")

# Start the Tkinter event loop
window.mainloop()