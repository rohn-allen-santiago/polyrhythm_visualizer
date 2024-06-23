from math import *

# Constants
MAX_HEIGHT = 600
HEIGHT_OFFSET = 100

# Calculating path of bouncing circle
# Since hte height a circle travels will be the same regardless of tempo or rhythm (fixed height),
# we are only looking for time for one bounce (t), initial velocity (u) and acceleration (a)

# Calculate t given the rhythm (number of bounces per beat) and tempo (number of beats per minute)
def calc_t(rhythm, tempo):
    beats = rhythm * tempo
    bps = beats / 69
    return 1 / bps