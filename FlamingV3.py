import pyautogui
import pytesseract
import time
import keyboard
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
x1, y1, x2, y2 = (878, 572, 1030, 650)  # coordinates of region to check
x3, y3, x4, y4 = (875, 552, 930, 570)  # coordinates of region to check for result text, if not there cancel loop
flamesleft = 3000  # number of flames you have, try to add 10-20 just incase it misses the click due to lag
int_min = 110  # minimum INT required
all_stat_min = 7  # minimum All Stat required
time.sleep(2)

for i in range(flamesleft):

    # takes a screenshot to check of the flame UI
    checkifbugged = pyautogui.screenshot(region=(x3, y3, x4 - x3, y4 - y3))
    checker = pytesseract.image_to_string(checkifbugged, lang='eng+osd')

    # checks if the flaming UI is on
    if checker != "":
        # Take a screenshot of the region with the stats
        img = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

        # read stats in the image and convert them to text
        text = pytesseract.image_to_string(img, lang='eng+osd')
        splittext = text.split('\n')

        # check if INT and All Stat are both greater than the required minimum
        int_found = False
        all_stat_found = False

        for line in splittext:
            if "INT" in line:
                int_value = int(re.search(r"INT\s*[:=\.]*\s*(\+?\d+)", line).group(1))
                print(int_value)
                if int_value >= int_min:
                    int_found = True
            elif "All Stats" in line and "+" in line:
                all_stat_value = int(line.split(":")[1].strip().split("+")[1].split("%")[0])
                if all_stat_value >= all_stat_min:
                    all_stat_found = True

        if int_found and all_stat_found:
            print(text)
            print("TARGET FOUND! INT >=", int_min, "and All Stat >=", all_stat_min)
            print("Terminating loop")
            print("============================")
            break

        # else this will continue rolling if your desired flames is not found
        else:

            print(text)
            print("Target not found. INT >=", int_min, "and All Stat >=", all_stat_min)
            print("============================")
            # Perform a mouse click
            pyautogui.click(935, 696)
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