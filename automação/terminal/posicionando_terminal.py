import pyautogui as py 
import time

def sleep():
    time.sleep(1)

def terminal_superior_direito():
    py.hotkey('ctrl','t')
    sleep()
    py.moveTo(1154,208)
    sleep()
    py.dragTo(0,47,1,button='left')

def terminal_inferior_direito():
    py.hotkey('ctrl','t')
    sleep()
    py.moveTo(1239,61)
    sleep()
    py.dragTo(0,1073,1,button='left')
    py.click()

def terminal_superior_esquerdo():
    py.hotkey('ctrl','t')
    sleep()
    py.moveTo(329, 110)
    sleep()
    py.dragTo(1919,24,1,button='left')

def terminal_inferior_esquerdo():
    py.hotkey('ctrl','t')
    sleep()
    py.moveTo(1239,61)
    sleep()
    py.dragTo(1916,1062,1,button='left')
    py.click()

def funcao_chama_terminais():
    terminal_superior_direito()
    terminal_inferior_direito()
    terminal_inferior_esquerdo()
    terminal_superior_esquerdo()

funcao_chama_terminais()
