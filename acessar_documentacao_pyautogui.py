'''
import pyautogui as pya
import pandas as pd
from time import sleep


Programa que automatiza toda uma rotina de abertura da documentação da biblioteca pyautogui na internet

link_documentacao_pyautogui = "https://pyautogui.readthedocs.io/en/latest/"
pya.PAUSE = 1.7

pya.press("win")
pya.moveTo(56, 753, duration=3, tween=pya.easeInOutQuad)
pya.click(x=56, y=753)
pya.write("chrome")
pya.press("enter")
pya.click(x=428, y=339)
pya.moveTo(x=261, y=14, duration=3, tween=pya.easeInOutQuad)
pya.click(x=261, y=14)
sleep(3)
pya.moveTo(x=224, y=54, duration=2)
pya.click(x=224, y=54)
pya.write(link_documentacao_pyautogui)
pya.press("enter")
sleep(3)
'''
