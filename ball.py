# A class for creating and drawing a ball (bouncing circle)
# canvas is the tkinter canvas the ball belongs to
# tag is the name used to identify the ball on teh canvas
# x and y are the coordinates of the top left point of the circle
# radius is the radius of the circle
# color is the color of the circle
# time is the timestamp of the ball, used for calculating its velocity and acceleration

class Ball:
    def __init__(self, canvas, tag, x, y, radius, color, time):
        self.canvas = canvas
        self.tag = tag
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.time = time