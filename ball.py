# A class for creating and drawing a ball (bouncing circle)
# canvas is the tkinter canvas the ball belongs to
# tag is the name used to identify the ball on teh canvas
# x and y are the coordinates of the top left point of the circle
# radius is the radius of the circle
# color is the color of the circle
# time is the timestamp of the ball, used for calculating its velocity and acceleration
# u and a are the initial velocity and acceleration of the ball respectively

from time import *
from rhythm import *
from pygame import mixer

class Ball:

    # Initialize the ball object
    def __init__(self, canvas, tags, x, color):
        self.canvas = canvas
        self.tags = tags
        self.x = x
        self.y = 600
        self.radius = 50
        self.color = color
        self.time = time()
        self.u= 0.0
        self.a = 0.0
        self.tempo = 0.0
        self.rhythm = 0.0

    # Set ball's tempo
    def set_tempo(self, tempo):
        self.tempo = tempo
        return None

    # Get ball's tempo
    def get_tempo(self):
        return self.tempo

    # Set bal's rhythm
    def set_rhythm(self, rhythm):
        self.rhythm = rhythm
        return None

    # Get ball's tempo
    def get_rhythm(self):
        return self.rhythm

    # Draw the ball on the canvas
    def draw(self):
        x1 = self.x + (2 * self.radius)
        y1 = self.y + (2 * self.radius)
        self.canvas.create_oval(self.x, self.y, x1, y1, outline=self.color, fill=self.color, tags=self.tags)
        self.play_audio("audio/metronome.mp3")
        self.time = time()
        return None

    # Delete the ball from the canvas
    def delete(self):
        self.canvas.delete(self.tags)
        return None

    # Move ball on the canvas
    def move(self, dx, dy):
        self.canvas.move(self.tags, dx, dy)
        return None

    # Calculate and update u and a given a rhythm and tempo
    def set_speed(self):
        if self.tempo == 0 or self.rhythm==0:
            return None
        rhythm = self.get_rhythm()
        tempo = self.get_tempo()
        t = calc_t(rhythm, tempo)
        u = calc_u(t)
        a = calc_a(t, u)
        self.u = u
        self.a = a
        return None

    # Update the ball's position on the canvas
    def update(self):
        if self.tempo == 0 or self.rhythm==0:
            return None
        t = time() - self.time
        s = calc_s(t, self.u, self.a)
        if s <= 0:
            self.time = time()
            self.play_audio("audio/metronome.mp3")

        # Convert s into the correct coordinate on the canvas
        ds = MAX_HEIGHT - s
        y = HEIGHT_OFFSET + ds
        dy = y - self.y
        self.y = self.y + dy

        # Move the ball by the calculated dy
        self.move(0, round(dy))

        return None

    # Play metronome sound
    def play_audio(self, path):
        mixer.init()
        mixer.music.load("audio/metronome.mp3")
        mixer.music.play()
        return None