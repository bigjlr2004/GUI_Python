import tkinter

# Create the main window
window = tkinter.Tk()
window.title("Test Shapes")

# Create a canvas widget
canvasWidget = tkinter.Canvas(window, bg="white", height=300, width=300)
canvasWidget.pack()

# Draw a rectangle
canvasWidget.create_rectangle(50, 50, 250, 250, fill="blue", outline="black")

# Draw an arc
canvasWidget.create_arc(50, 50, 250, 250, start=0, extent=270, fill="red", outline="black")

# Start the Tkinter event loop
window.mainloop()