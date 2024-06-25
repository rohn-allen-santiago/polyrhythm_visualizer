from tkinter import *
from ball import *

# Create window and set dimensions
pv = Tk()
pv.title("Polyrhythm Visualizer")
pv.geometry("1500x1000")

# Create Frame and set dimensions
f = Frame(pv, width=1500, height=200, bg="white")
f.pack()

# Create canvas and set dimensions
canvas = Canvas(pv, width=1500, height=800, bg="white")
canvas.pack()

# Add ball(s) to canvas (testing)
balls = []
ball1 = Ball(canvas, "ball1", 400, "blue")
ball1.set_speed(2, 120)
ball1.draw()
balls.append(ball1)
ball2 = Ball(canvas, "ball2", 800, "red")
ball2.set_speed(3, 120)
ball2.draw()
balls.append(ball2)
ball3 = Ball(canvas, "ball3", 1200, "green")
ball3.set_speed(4, 120)
ball3.draw()
balls.append(ball3)

# Run main loop
while True:
    pv.update_idletasks()
    pv.update()
    sleep(0.01)
    for ball in balls:
        ball.update()