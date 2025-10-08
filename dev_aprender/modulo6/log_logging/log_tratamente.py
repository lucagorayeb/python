import logging

logging.basicConfig(level=logging.DEBUG, filename='app1.log', filemode='a',format='%(levelname)s - %(message)s - %(asctime)s')
try:

    email = input('Digite o seu email: ')
    senha = int(input('Digite a sua senha bancária: '))
    if senha == 1234:
        print('Login feito com sucesso!')
        logging.info(f'{email} entrou em sua conta bancária')
except ValueError as erro:
    print('Digite apenas números')
    logging.info(erro)