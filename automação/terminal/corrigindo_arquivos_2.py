import pyautogui
import time as t

def sleep():
    t.sleep(1)

def enter():
    pyautogui.press('enter')

def mudar_arquivos_exercicios():
    pyautogui.write('cd Documentos/java/exercicios/beecrowd/iniciante/')
    enter()
    sleep()
    mudancas = ['area','calculosimples','consumo','diferenca','esfera', 'helloworld', 'lanche',  'media2', 'produtosimples', 'selecao', 'teste'
                ,'areacirculo' , 'cedulas', 'conversaotempo', 'distancia', 'extremamentebasico', 'idadedias', 'maior', 'media3', 'salario', 'somasimples',
                'triangulo', 'bhaskara', 'cedulasmoedas', 'coordenadas', 'distanciaentredoispontos', 'gastocombustivel', 'intervalo', 'media1', 'multiplos',
                'salariocombonus', 'sort_simples']
    repeticao(mudancas)

def repeticao(mudancas):
    for mudanca in mudancas:
        pyautogui.write(f'cd {mudanca}')
        enter()
        sleep()
        pyautogui.write('mv src/* lib/')
        sleep()
        enter()
        sleep()
        pyautogui.write('mv lib/*Test.* src/')
        sleep()
        enter()
        sleep()
        pyautogui.write('cd ..')
        sleep()
        enter()
        sleep()




def abrir_novo_terminal():
    pyautogui.hotkey('ctrl','t')
    sleep()
    pyautogui.click()
    sleep()
    mudar_arquivos_exercicios()

abrir_novo_terminal()
