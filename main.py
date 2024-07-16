from tkinter import *
from ball import *

# Constants
MAX_TEMPO = 120
MAX_RHYTHM = 9

# Create window and set dimensions
pv = Tk()
pv.title("Polyrhythm Visualizer")
pv.geometry("1500x1000")

# Create Frame and set dimensions
f = Frame(pv, width=1500, height=200, bg="white")
f.pack()

# Create labels and entry boxes for input
tempoLabel = Label(f, text="Tempo")
tempoLabel.grid(row=0,column=4, pady=40)
tempoInput = Entry(f, bg="white")
tempoInput.grid(row=0,column=5, pady=40)
rhythms = []
for i in range(5):
    name = "Ball " + str(i + 1)
    Label(f, bg="white", text=name).grid(row=1, column=(i * 2), padx = 35, pady=40)
    entry = Entry(f, bg="white")
    entry.grid(row=1, column=(i * 2) + 1, padx = 35, pady=40)
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

# Keep count of how many labels contain a number
count = 0

# Set tempo for each ball to user inputted tempo
def change_tempo():
    tempo = tempoInput.get()
    # Handle non digit characters
    if not any(char.isdigit() for char in tempo):
        tempoInput.delete(0, len(tempo))
        return None
    if tempo == "":
        tempo = "0"
    tempo = int(tempo)
    for ball in balls:
        ball.set_tempo(tempo)
        ball.set_speed()
    return None

# Set rhythm for each ball to user inputted rhythm
def change_rhythm():
    tempCount = 0
    for i in range(5):
        ball = balls[i]
        rhythm = rhythms[i].get()
        if rhythm == "":
            rhythm = "0"
        else:
            tempCount += 1
        rhythm = int(rhythm)
        ball.set_rhythm(rhythm)
        ball.set_speed()
    global count
    if tempCount > count:
        reset_all()
    count = tempCount
    return None

# Reset every ball to ground position
def reset_all():
    for ball in balls:
        ball.reset()
    return None

# Run main loop
while True:
    pv.update_idletasks()
    pv.update()
    change_tempo()
    change_rhythm()
    for ball in balls:
        ball.update()