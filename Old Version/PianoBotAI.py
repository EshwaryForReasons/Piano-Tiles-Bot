import pyautogui
import time
from mss import mss
import keyboard

start_x = 675
start_y = 800

bbox = (start_x, start_y, start_x + 570, start_y + 1)

cords_x = [300, 100, 100, 350]

def test_time():
    with mss() as sct:
        t1 =time.time()
        for i in range(100):
            img = sct.grab(bbox)
            pyautogui.click(69, 610)
        t2 = time.time()
        print(t2 - t1)

def print_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)

def start():
    with mss() as sct:
        while True:
            #Fail safe if it gains sentience
            if keyboard.is_pressed('q'):
                break

            img = sct.grab(bbox)
            for cord in cords_x:
                if img.pixel(cord, 0)[0] < 100:
                    pyautogui.click(start_x + cord, start_y)
                    break

time.sleep(1)
start()