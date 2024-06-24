# A class for creating and drawing a ball (bouncing circle)
# canvas is the tkinter canvas the ball belongs to
# tag is the name used to identify the ball on teh canvas
# x and y are the coordinates of the top left point of the circle
# radius is the radius of the circle
# color is the color of the circle
# time is the timestamp of the ball, used for calculating its velocity and acceleration
# u and a are the initial velocity and acceleration of the ball respectively

from time import *

class Ball:

    # Initialize the ball object
    def __init__(self, canvas, tags, x, y, radius, color):
        self.canvas = canvas
        self.tags = tags
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.time = time()
        self.u= 0.0
        self.a = 0.0

    # Draw the ball on the canvas
    def draw(self):
        x1 = self.x + (2 * self.radius)
        y1 = self.y + (2 * self.radius)
        self.canvas.create_oval(self.x, self.y, x1, y1, outline=self.color, fill=self.color, tags=self.tags)
        return None

    # Delete the ball from the canvas
    def delete(self):
        self.canvas.delete(self.tags)
        return None

















