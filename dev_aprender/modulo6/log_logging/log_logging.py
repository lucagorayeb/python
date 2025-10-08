# Logging

import logging 

"""
debug -> Só estou fornecendo informações para os desenvolvedores.

info -> Só quero informar algo que está acontecendo no programa, mas que não é um erro.

warning -> Quero alertar sobre algo que está contecendo, possivelmente fora do esperado, porém ainda não é um erro, mas pode gerar um futuramente

error -> Um erro ocorreu na aplicação 

critical -> Um erro com consequências graves acaba de ocorrer na aplicação 
"""

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',format='%(levelname)s - %(message)s') # Mudar o nível
logging.debug('Logging nível debug')
logging.info('Logging nível info')
logging.warning('Logging nível warning')
logging.error('Logging nível error')
logging.critical('Logging nível critical')