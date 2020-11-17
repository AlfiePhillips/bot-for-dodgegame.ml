import webbrowser
import pyautogui
import time
import keyboard

def num1Press(x, y):
    pyautogui.press("num1")

def num2Press(x, y):
    pyautogui.press("num2")

def bot():
    while(1):
        box1 = pyautogui.pixel(780, 750)
        box2 = pyautogui.pixel(960, 750)
        if keyboard.is_pressed("p"):
            break
        if box1[0] > 150:
            num2Press(960, 750)
        elif box2[0] > 150:
            num1Press(780, 750)
        elif box2[1] > 150:
            num2Press(960, 750)
        elif box1[1] > 150:
            num1Press(780, 750)
       

def main():
    easyorhard = input("Would you like easy or hard")
    if easyorhard == ("easy"):
        webbrowser.open("http://dodgegame.ml/")
        time.sleep(2)
        pyautogui.moveTo(960, 658)
        time.sleep(2)
        pyautogui.click(960, 658)
        pyautogui.press("c")
        bot()
    elif easyorhard == ("hard"):
        webbrowser.open("http://dodgegame.ml/")
        time.sleep(5)
        pyautogui.moveTo(954, 774)
        time.sleep(1)
        pyautogui.click(954, 774)
        time.sleep(1)
        pyautogui.moveTo(936, 850)
        time.sleep(1)
        pyautogui.click(936, 850)
        time.sleep(1)
        pyautogui.moveTo(960, 658)
        time.sleep(1)
        pyautogui.click(960, 658)
        pyautogui.press("c")
        bot()
                
if __name__ == "__main__":
    main()
