#!/usr/bin/env python3

import keyboard
import pyautogui
import signal
import sys
import os

def cleanup():
    pyautogui.mouseUp(button='middle')
    
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def signal_handler():
    cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def hookCallback(e:keyboard.KeyboardEvent):
    if (e.name == 'command'):
        if e.event_type == keyboard.KEY_DOWN:
            pyautogui.mouseDown(button='middle')
        elif e.event_type == keyboard.KEY_UP:
            pyautogui.mouseUp(button='middle')

keyboard.hook(hookCallback)
notify('Middlemouse','Middlemouse proxy enabled')
print('Press CMD + ESC everywhere or CTRL+C on this shell to quit ')
keyboard.wait('command+esc')
notify('Middlemouse','Middlemouse proxy disabled')