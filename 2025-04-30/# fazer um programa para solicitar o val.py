# fazer um programa para solicitar o valor de uma venda e
# o porcentual da comissão

valorvenda = float(input('digite o valor da venda (R$): '))
percentual = float (input('informe a comissão (%)......: '))

comissao = valorvenda * percentual / 100

print(f'o valor da comissão é R$ {comissao:.2f}')