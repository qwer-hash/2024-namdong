x, y = 0, 0

def move(direction);
    global x, y

    if direction == 'up':
            y += 1
    elif direction == 'down':
            y -= 1
    elif direction == 'left':
            x -= 1
    elif direction == 'right':
            x += 1
