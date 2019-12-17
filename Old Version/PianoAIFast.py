from PIL import ImageGrab 
import pyautogui
import pyautogui as cursor
import keyboard
import time
import mss

quitHotkey = 'q'

numClicks = 0

blue = [(54, 159, 198)]
black = [(0, 0, 0), (16, 20, 19)]
searchFor = blue

start_x = 675
start_y = 800

screenParams = (675, 85, 1250, 1040)

time.sleep(1)
sct = mss.mss()
screenDimensions = {"top": 37, "left": 663, "width": 600, "height": 990}
footer = 250

def testTime():
    t1 = time.time()
    for i in range(100):
        img = sct.grab(screenParams)
    t2 = time.time()  
    print(t2 - t1)

while True:
    #Fail safe if it gains sentience
    if keyboard.is_pressed(quitHotkey):
        break

    #Get a screenshot
    im2 = sct.grab(screenDimensions) 
    if searchFor == blue:
        searchHeight = im2.height - footer
    else:
        searchHeight = im2.height

    for i in reversed(range(0, searchHeight)):
        #First Lane
        if im2.pixel(75, i) in searchFor:
            #Prevent Popups
            if i>88:
                cursor.click(75 + 663, i + 37 + 2 )
                numClicks = numClicks + 1
            searchFor = black
            break

        #Second Lane
        elif im2.pixel(255, i) in searchFor:
            cursor.click(255 + 663, i + 37 + 2 )
            numClicks = numClicks + 1
            searchFor = black
            break

        #Third Lane
        elif im2.pixel(375, i) in searchFor:
            cursor.click(375 + 663, i + 37 + 2)
            numClicks = numClicks + 1
            searchFor = black
            break

        #Forth Lane
        elif im2.pixel(525, i) in searchFor:
            cursor.click(525 + 663, i + 37 + 2)
            numClicks = numClicks + 1
            searchFor = black
            break