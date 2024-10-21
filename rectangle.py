import tkinter

window = tkinter.Tk()
canvasWidget = tkinter.Canvas(window, bg="white", height=512, width=512)
canvasWidget.pack()

# Draw a rectangle
canvasWidget.create_rectangle(50, 50, 450, 450, fill="blue", outline="blue")

window.mainloop()