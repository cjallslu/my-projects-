import pyautogui as ptg

text = "Stop it, you can be QUIET. YES YOU CAAAAAN"

for t in text.split():
    ptg.write(t)
    ptg.press("enter")

