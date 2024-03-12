import pyautogui
import time
import keyboard

def work(image_path):
    while True:
        try:
            image_location = pyautogui.locateOnScreen(image_path)
            
            if keyboard.is_pressed('q'):
                exit()

            if image_location is not None:
                image_center = pyautogui.center(image_location)
                pyautogui.moveTo(image_center)
                pyautogui.click()

                time.sleep(0.5)
        except Exception:
            print("Something Went Wrong")
            exit()


image_path = 'target.png'
print("Press q to end script early")
work(image_path)
