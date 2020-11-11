import pyautogui

def num1Press(x, y):
    pyautogui.press("num1")

def num2Press(x, y):
    pyautogui.press("num2")

while(1):
    if pyautogui.pixel(780, 750)[0] > 150:
            num2Press(960, 750)
    elif pyautogui.pixel(960, 750)[0] > 150:
            num1Press(780, 750)
    elif pyautogui.pixel(960, 750)[1] > 150:
            num2Press(960, 760)
    elif pyautogui.pixel(780, 750)[1] > 150:
        num1Press(780, 750)
   
