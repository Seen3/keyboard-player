

#Made to be used in https://virtualpiano.net/
#notes contains data from given music sheets in the same site


import time
import pyautogui
notes = open("notes.txt", "r")
str=notes.read()
notes.close()
key=""
timeindv=0.05 #between individual presses
timespace=0.1 # for ' '
timeline=0.2 #for '|'
together=False
for letter in str:
    key=letter
    if key.isalnum():
        pyautogui.press(key)
        if not together:
            time.sleep(timeindv)
    elif key=='[':
        together=True
        timeindv=0
        timespace=0.001
    elif key==']':
        together=False
        timeindv=0.005
        timespace=0.1
    elif key == ' ':
        time.sleep(timespace)
    elif key == '|':
        time.sleep(timeline)