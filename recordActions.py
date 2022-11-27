import time 
import cv2 as cv
import pyautogui
from pynput.keyboard import Key, KeyCode, Listener as KeyListener
from pynput.mouse import Button, Controller, Listener as MouseListener
import json

from constants import FARM


# class Record:
positionList = []
holdList = []
prevStamp = float(0)


def addToHoldList(key):
  holdList.append(key)

def on_click(x, y, button, pressed):
  if pressed: 
    global prevStamp

    pressedBtn = "left" if button == Button.left else "right"
    pyautogui.mouseUp(button=pressedBtn)

    ts = time.time()
    pause = ts - prevStamp if prevStamp > 0 else 0
    prevStamp = time.time()

    modifier = None
    if Key.shift in holdList or Key.alt in holdList or Key.ctrl in holdList or Key.cmd in holdList: modifier = str(holdList[0]).split('.')[1]
    newPosition = dict(
      x=round(x), 
      y=round(y), 
      button=pressedBtn, 
      pause=round(pause, 3), 
      modifier=modifier
    )
    print(newPosition)

    positionList.append(newPosition)

def start( filename):
  mouseListener = MouseListener(on_click=on_click)

  def on_release(key):
    if key == Key.cmd and Key.shift in holdList:
      mouseListener.start()
      print("START RECORDING")

    if key == KeyCode.from_char('r'):
      pyautogui.click(*pyautogui.position(), 1, 0, "right")

    if key == KeyCode.from_char('e'):
      pyautogui.click(*pyautogui.position(), 1, 0, "left")
    
    if key == Key.alt and Key.shift in holdList:
      file = open('data/{0}.json'.format(filename), 'w')
      json_string = json.dumps(positionList)
      file.write(json_string)
      file.close()
      print("SAVED RECORDING")

    holdList.remove(key)

    if key == Key.esc:
      MouseListener.stop(self=mouseListener)
      return False

  with KeyListener(on_press=addToHoldList, on_release=on_release) as listener:
    listener.join()

start("test")