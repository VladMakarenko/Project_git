import time
import os
import pynput

ballX = 7
ballY = 5
ballDirX = 0.6
ballDirY = 0.6
width = 30
height = 10
racket1Y = 1
racket2Y = 5
racketLenght = 3

def draw():
    y = 0
    while y < height:
        x = 0
        result = ''
        while x < width:
            if x == round(ballX) and y == round(ballY):
                result += 'o'
            elif x == 0 and (y >= racket1Y and y < racket1Y + racketLenght):
                result += '|'
            elif x == width - 1 and (y >= racket2Y and y < racket2Y + racketLenght):
                result += '|'
            elif y == 0 and (x >= 1 and x <= width):
                result += '_'
            elif y == height - 1 and (x >= 1 and x <= width):
                result += '_'
            else:
                result += ' '
            x += 1
        print(result)
        y += 1

def press_instruction(key):
    global racket1Y, racket2Y
    if key == pynput.keyboard.KeyCode.from_char('w'):
        racket1Y -= 1
        if racket1Y == 0:
            racket1Y += 1
    elif key == pynput.keyboard.KeyCode.from_char('s'):
        racket1Y += 1
        if racket1Y == height - 2:
            racket1Y -= 1
    if key == pynput.keyboard.Key.down:
        racket2Y += 1
        if racket2Y == height - 2:
            racket2Y -= 1
    elif key == pynput.keyboard.Key.up:
        racket2Y -= 1
        if racket2Y == 0:
            racket2Y += 1

def release_instruction(key):
    print(key)

pynput.keyboard.Listener(
    on_press=press_instruction,
    on_release=release_instruction
).start()

while True:
    ballX += ballDirX
    ballY += ballDirY



    os.system('cls')
    draw()
    time.sleep(0.1)
