import pyautogui
import pytesseract
import time
import keyboard

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
x1, y1, x2, y2 = (835, 625, 995, 704)  # coordinates of region to check
x3, y3, x4, y4 = (828, 602, 892, 622)  # coordinates of region to check for result text, if not there cancel loop
flamesleft = 2549 # number of flames you have, try to add 10-20 just incase it misses the click due to lag
statTarget = ['INT: +112', 'All Stats: +7%'] # what kind of stats you're looking for?
time.sleep(2)

for i in range(flamesleft):

    #takes a screenshot to check of the flame UI
    checkifbugged = pyautogui.screenshot(region=(x3, y3, x4-x3, y4-y3))
    checker = pytesseract.image_to_string(checkifbugged, lang='eng+osd')

    #checks if the flaming UI is on
    if checker != "":
        # Take a screenshot of the region with the stats
        img = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))

        #read stats in the image and convert them to text
        text = pytesseract.image_to_string(img, lang='eng+osd')
        splittext = text.split('\n')

        #if the stat you want is part of the flame RNG, it will stop
        if (set(statTarget).issubset(set(splittext))):
            print(text)
            print("TARGET FOUND! ", statTarget)
            print("Terminating loop")
            print("============================")
            break

        #else this will continue rolling if your desired flames is not found
        else:

            print(text)
            print("Target not found ", statTarget)
            print("============================")
            # Perform a mouse click
            pyautogui.click(886, 748)
            # Perform two enter key presses
            pyautogui.press('enter')
            pyautogui.press('enter')

        #Hold delete to stop the script
        if keyboard.is_pressed('delete'):
            print("Delete key pressed, terminating script.")
            break

    #if the flame ui is not open, this will stop the loop
    else:
        print("Flame UI Not Opened")
        print("============================")
        break

    # Wait 1.5 seconds before checking again
    time.sleep(1.50)