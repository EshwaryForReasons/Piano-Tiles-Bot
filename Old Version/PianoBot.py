import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time
# click(1800, 10)

gameCoords = [657, 32, 1262, 1039]

screen = np.array(ImageGrab.grab(bbox=gameCoords))
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

while True:
    mousePos = queryMousePosition()
    if gameCoords[2] > mousePos.x>gameCoords[0]:
        startTime = time.time()
        for y in range(len(screen)):
            for x in range(len(screen[y])):
                if screen[y][x] < 10:
                    # click(x, y)
                    pass
        print("Frame took {} seconds. Up to frame no {}".format((time.time() - startTime), "FUCK YOU"))