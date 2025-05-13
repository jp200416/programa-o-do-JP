from logging import exception
import sys


try: 
    intdividendo = int(input('digite o dividendo: '))
    intdivisor = int(input('digiteo dividendo: '))
    fitresultado = intdividendo / intdivisor
except ValueError:
    print('erro: informe um valor que possa ser convertido em inteiro.')
except exception as tipoexceçao:
    print(f'erro: {tipoexceçao}')
    print(f'erro: {sys.exc_info()}')
else:
    print(f'erro: {fitresultado}')
