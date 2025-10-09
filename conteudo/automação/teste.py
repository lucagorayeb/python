import pyautogui
import time

print("Aperte Ctrl-C para sair.")

while True:
    x, y = pyautogui.position()
    posicao_str = f'X: {x} Y: {y}'
    print(posicao_str, end='\r') # O '\r' faz a linha ser sobrescrita
    time.sleep(0.1) # Pequena pausa para não sobrecarregar o CPU
