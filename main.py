from tkinter import *

# Create window and set dimensions
pv = Tk()
pv.title("Polyrhythm Visualizer")
pv.geometry("1500x1000")

# Create Frame and set dimensions
f = Frame(pv, width=1500, height=200, bg="white")
f.pack()

# Create canvas and set dimensions
canvas = Canvas(pv, width=1500, height=800, bg="white")
canvas.create_oval(50, 50, 80, 80, outline="blue", fill="blue")
canvas.pack()

# Run main loop
while True:
    pv.update_idletasks()
    pv.update()