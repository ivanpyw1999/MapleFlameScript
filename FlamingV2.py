import pyautogui
import pytesseract
import time
import keyboard

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
x1, y1, x2, y2 = (869, 634, 930, 654)  # coordinates of region to check
flamesleft = 4290  #number of flames you have, try to add 10-20 just incase it misses the click due to lag
targetrangeincrease = '142000000' #change this for the increase u want

for i in range(flamesleft):
    # Get the text from the specific coordinates
    img = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    text = pytesseract.image_to_string(img)
    # Search for a number under 150000000 in the text


    if targetrangeincrease > text:
        print(text)
        print("No text found over ", targetrangeincrease)
        print("============================")
        # Perform a mouse click
        pyautogui.click(840,673)
        # Perform two enter key presses
        pyautogui.press('enter')
        pyautogui.press('enter')
    else:
        print(text)
        print("Found value over ", targetrangeincrease)
        print("Terminating loop")
        print("============================")
        break

    if keyboard.is_pressed('delete'):
        print("Delete key pressed, terminating script.")
        break
    # Wait 2 seconds before checking again
    time.sleep(1.50)