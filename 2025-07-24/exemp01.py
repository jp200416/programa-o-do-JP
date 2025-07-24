import requests

try:
    reqHTTP = requests.get('https://opi.cartolafc.globo.com/atletras/mercado')
except Exception as erro:
    print(f'Erro: {erro}')

else:
    if reqHTTP.status_code != 200:
        print('erro na aquisição')
    dictcartola = reqHTTP.json()
    print(dictcartola)