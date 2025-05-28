import sys

try:
    intmultiplicador = int(input('digite o multiplicador: '))
    intmultiplicando = int(input('digite o multiplicando: '))
except ValueError:
    sys.exit('erro: não foi informado um valor valido inteiro...')
except Exception as e:
    sys.exit(f'erro: {e}')
else:
    if intmultiplicador  <= 0:
        sys.exit('erro: informe um multiplicador positivo...')
    if intmultiplicando <= 0:
        sys.exit('erro: informe multiplicando positivo...')

    intproduto = 0
    intcontador = 1
    while intcontador <= intmultiplicador:
        intproduto += intmultiplicando
        intcontador += 1
    print(f'{intmultiplicador} x {intmultiplicando} = {intproduto}')
        
