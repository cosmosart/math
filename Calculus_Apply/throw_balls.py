def height(time, init, speed, g):
    h = init + speed*time - g * time**2
    return h

def velocity(speed, g):
    # velocity(t) = h'(t)
    v = speed - g * 2
    return 'Velocity = ' + str(v) + '/sec'

def acceleration(g):
    # acceleration(t) = v'(t)
    return 'Acceleration = ' + str(-g * 2) + '/sec^2'