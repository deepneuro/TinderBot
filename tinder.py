import numpy as np
import pyautogui
import time
from random import randint

i = 0
x = 5
a, b = pyautogui.position()
c, d = 0, 0

print('Click position: ',a, b)
pyautogui.FAILSAFE = True
while True:
    time.sleep(0.2)
    pyautogui.click(a+c, b+d)
    i += 1
    try:
        if i % x == 0:
            time.sleep(0.2)
            pyautogui.click(a-165+c, b+d)
            x = randint(4, 6)
            print(x)
            c, d = randint(-3, 4), randint(-5, 5)
            print(c,d)
    except:
        continue
    c, d = randint(-5, 5), randint(-5, 5)

    print('click: ',i)
    if i == 90:
        break

