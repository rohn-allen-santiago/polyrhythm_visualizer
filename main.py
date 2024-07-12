from tkinter import *
from ball import *

# Create window and set dimensions
pv = Tk()
pv.title("Polyrhythm Visualizer")
pv.geometry("1500x1000")

# Create Frame and set dimensions
f = Frame(pv, width=1500, height=200, bg="white")
f.pack()

# Create entry boxes for input
tempoLabel = Label(f, text="Tempo")
tempoLabel.grid(row=0,column=0, pady=5)
tempoInput = Entry(f, bg="white")
tempoInput.grid(row=0,column=1, pady=5)
ballInputs = []
for i in range(5):
    name = "Ball " + str(i + 1)
    Label(f, bg="white", text=name).grid(row=i+1, column=0, pady=5)
    entry = Entry(f, bg="white").grid(row=i+1, column=1, pady=5)
    ballInputs.append(entry)

# Create canvas and set dimensions
canvas = Canvas(pv, width=1500, height=800, bg="white")
canvas.pack()

# Add ground and ceiling lines to canvas
ground = canvas.create_line(0, 700,1500, 700)
ceiling = canvas.create_line(0, 100,1500, 100)

# Add ball(s) to canvas (testing)
balls = []
ball1 = Ball(canvas, "ball1", 400, "blue")
ball1.set_rhythm(2)
ball1.set_speed()
ball1.draw()
balls.append(ball1)
ball2 = Ball(canvas, "ball2", 800, "red")
ball2.set_rhythm(3)
ball2.set_speed()
ball2.draw()
balls.append(ball2)
ball3 = Ball(canvas, "ball3", 1200, "green")
ball3.set_rhythm(4)
ball3.set_speed()
ball3.draw()
balls.append(ball3)

# Set tempo for each ball to global tempo
def change_tempo():
    tempo = tempoInput.get()
    if tempo == "":
        tempo = "60"
    tempo = int(tempo)
    for ball in balls:
        ball.set_tempo(tempo)
        ball.set_speed()
    return None

# Run main loop
while True:
    pv.update_idletasks()
    pv.update()
    change_tempo()
    for ball in balls:
        ball.update()