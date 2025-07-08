import os

strDir = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{strDir}//carta.txt','r', encoding='utf-8')
except FileNotFoundError:
    print('Erro: arquivo não encontrado!')
except Exception as erro:
    print(f'Erro: {erro}!')
else:
    strconteudo = arqLeitura.readline()
    arqLeitura.close()
    print(strconteudo)