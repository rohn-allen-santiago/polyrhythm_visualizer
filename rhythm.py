from math import *

# Constants
MAX_HEIGHT = 500
HEIGHT_OFFSET = 100

# Calculating path of bouncing circle
# Since hte height a circle travels will be the same regardless of tempo or rhythm (fixed height),
# we are only looking for time for one bounce (t), initial velocity (u) and acceleration (a)

# Calculate t given the rhythm (number of bounces per beat) and tempo (number of beats per minute)
def calc_t(rhythm, tempo):
    beat = 60.0 / tempo
    bar = 4.0 * beat
    return bar / rhythm

# Calculate u given t
# s is fixed, and we know v is 0 at the apex of the bounce at time t/2
def calc_u(t):
    return (2.0 * MAX_HEIGHT) / (t/2.0)

# Calculate a given u and t
# We know s is 0 at time t
def calc_a(t, u):
    return (-2.0 * (u * t)) / pow(t, 2.0)

# Calculate s given a, u and t
# If s < 0,  set s to 0
# If s > 600, set s to 500 (should not be possible)
def calc_s(t, u, a):
    s = (u * t) + (0.5 * a * pow(t, 2.0))
    if s < 0:
        return 0
    elif s > MAX_HEIGHT:
        return MAX_HEIGHT
    else:
        return round(s)