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


draw()