import time
import pyautogui

# 5 second delay, then open the bee movie script
time.sleep(5)
f = open("beeMovieScript", "r")

# for each line in the script,
for word in f:
    # type the line wherever it is, press enter, wait .5 seconds
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(.2)

f.close()
