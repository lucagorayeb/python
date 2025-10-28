import pyautogui as py
import time as t

def sleep():
    t.sleep(1)

def enter():
    py.press('enter')

def mudar_arquivos_exercicios():
    py.write('code_java')
    enter()
    sleep()
    py.write('cd exercicios/beecrowd/iniciante')
    enter()
    sleep()
    mudancas = ['area','calculosimples','consumo','diferenca','esfera', 'helloworld', 'lanche',  'media2', 'produtosimples', 'selecao', 'teste'
                ,'areacirculo' , 'cedulas', 'conversaotempo', 'distancia', 'extremamentebasico', 'idadedias', 'maior', 'media3', 'salario', 'somasimples',
                'triangulo', 'bhaskara', 'cedulasmoedas', 'coordenadas', 'distanciaentredoispontos', 'gastocombustivel', 'intervalo', 'media1', 'multiplos',
                'salariocombonus', 'sort_simples']
    repeticao(mudancas)

def alterar_300_exercicios():
    py.write('code_java')
    sleep()
    enter()
    sleep()
    py.write('cd teste/exercicios_logica_programacao/300_ideias_para_programas')
    sleep()
    enter()
    sleep()
    mudancas = ['ex007','ex008','ex009','ex010','ex011','ex012','ex013','ex014','ex015']
    repeticao(mudancas)

def repeticao(mudancas):
    for mudanca in mudancas:
        py.write(f'cd {mudanca}')
        sleep()
        enter()
        sleep()
        py.write('java_project')
        sleep()
        enter()
        sleep()
        py.write('mv domain/* src/')
        sleep()
        enter()
        sleep()
        py.write('mv test/* lib/')
        sleep()
        enter()
        sleep()
        py.write('rm -rf domain && rm -rf test')
        sleep()
        enter()
        sleep()
        py.write('cp exercise.txt README.md')
        sleep()
        enter()
        sleep()
        py.write('rm -rf exercise.txt')
        sleep()
        enter()
        sleep()
        py.write('cd ..')
        sleep()
        enter()
        sleep()




def abrir_novo_terminal():
    py.hotkey('ctrl','t')
    sleep()
    py.click()
    sleep()
    alterar_300_exercicios()
    mudar_arquivos_exercicios()

abrir_novo_terminal()
