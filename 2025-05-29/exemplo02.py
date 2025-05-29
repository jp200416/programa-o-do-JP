from logging import exception
import sys
import sys

try:
    intvalor = (input('digite um numero inteiro'))
except ValueError:
    sys.exit('erro: digite um numero inteiro')
except Exception as e:
    sys.exit(f'Erro: {e}')
else:
    if intvalor <0:
        print('não existe fatorial')
    elif intvalor <2:
        print(f'{intvalor}!=1')
