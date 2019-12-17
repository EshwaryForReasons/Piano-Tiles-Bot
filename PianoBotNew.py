import mss
import pyautogui as cursor
import pyautogui
import keyboard
import time
from PIL import ImageGrab

blue = [(54, 159, 198)]
black = [(0, 0, 0), (16, 20, 19)]
searchFor = blue

start_x = 675
start_y = 800

bbox = (start_x, start_y, start_x + 570, start_y + 1)

time.sleep(1)
sct = mss.mss()
screenDimensions = {"top": 37, "left": 663, "width": 600, "height": 990}
footer = 250

def test_time():
    with mss.mss() as sct:
        t1 =time.time()
        for i in range(100):
            img = sct.grab(bbox)
            pyautogui.click(69, 610)
        t2 = time.time()
        print(t2 - t1)

while True:
    #Quit hotkey (for emergencies)
    if keyboard.is_pressed('q'):
        break
    #Take a screenshot
    sct_img = sct.grab(screenDimensions)
    if searchFor == blue:
        searchHeight = sct_img.height - footer
    else:
        searchHeight = sct_img.height

    for i in reversed(range(0, searchHeight)):
        #First Lane
        if sct_img.pixel(75, i) in searchFor:
            #Prevent Popups
            if i>88:
                cursor.click(75 + 663, i + 37 + 2)
            searchFor = black
            break

        #Second Lane
        elif sct_img.pixel(255, i) in searchFor:
            cursor.click(255 + 663, i + 37 + 2 )
            searchFor = black
            break

        #Third Lane
        elif sct_img.pixel(375, i) in searchFor:
            cursor.click(375 + 663, i + 37 + 2)
            searchFor = black
            break

        #Forth Lane
        elif sct_img.pixel(525, i) in searchFor:
            cursor.click(525 + 663, i + 37 + 2)
            searchFor = black
            break