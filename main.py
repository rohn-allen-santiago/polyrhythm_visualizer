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
rhythms = []
for i in range(5):
    name = "Ball " + str(i + 1)
    Label(f, bg="white", text=name).grid(row=i+1, column=0, pady=5)
    entry = Entry(f, bg="white")
    entry.grid(row=i+1, column=1, pady=5)
    rhythms.append(entry)

# Create canvas and set dimensions
canvas = Canvas(pv, width=1500, height=800, bg="white")
canvas.pack()

# Add ground and ceiling lines to canvas
ground = canvas.create_line(0, 700,1500, 700)
ceiling = canvas.create_line(0, 100,1500, 100)

# Add ball(s) to canvas (testing)
balls = []
ball1 = Ball(canvas, "ball1", 250, "blue")
ball1.draw()
balls.append(ball1)
ball2 = Ball(canvas, "ball2", 500, "red")
ball2.draw()
balls.append(ball2)
ball3 = Ball(canvas, "ball3", 750, "green")
ball3.draw()
balls.append(ball3)
ball4 = Ball(canvas, "ball4", 1000, "yellow")
ball4.draw()
balls.append(ball4)
ball5 = Ball(canvas, "ball5", 1250, "purple")
ball5.draw()
balls.append(ball5)

# Set tempo for each ball to user inputted tempo
def change_tempo():
    tempo = tempoInput.get()
    if tempo == "":
        return None
    tempo = int(tempo)
    for ball in balls:
        ball.set_tempo(tempo)
        ball.set_speed()
    return None

# Set rhythm for each ball to user inputted rhythm
def change_rhythm():
    for i in range(5):
        print(type(rhythms))
        rhythm = rhythms[i].get()
        if rhythm == "":
            continue
        rhythm = int(rhythm)
        balls[i].set_rhythm(rhythm)
        balls[i].set_speed()
    return None

# Run main loop
while True:
    pv.update_idletasks()
    pv.update()
    change_tempo()
    change_rhythm()
    for ball in balls:
        ball.update()