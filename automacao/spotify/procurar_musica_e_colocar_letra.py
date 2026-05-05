import pyautogui as py
import time

time.sleep(3)

posicao = py.position()
print(f"X: {posicao.x}")
print(f"Y: {posicao.y}")

