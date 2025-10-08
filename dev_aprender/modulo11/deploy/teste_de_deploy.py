import time 
import random

while True: 
    print(random.randint(1, 100))
    time.sleep(3)

# Para adicionar itens na pasta do arquivo executável nós usamos o seguinte comando 
# pyinstaller --add-data "caminho_da_pasta";"nome_que_a_pasta_vai_ter" 
# No mac e no linux não usamos o (;), usamos os (:).
# Para adicionar um executável dentro do programa, usamos o comando
# pyinstaller --add-binary "caminho_do_arquivo";"nome_da_pasta" 
# --noconfirm usado apenas no windows para que não haja necessidade de confirmação 
# --noconsole não vai exibir o console quando estiver executando 
#flaticon para ter icones no programa e depois converter para ico 
# pyinstaller nome_do_arquivo_executavel_que_vai_receber_o_icone --icon=nome_do_arquivo.ico