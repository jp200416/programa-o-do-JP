strTexto = input('diigte um texto: ')

strvogais = 'aeiouãõáéíóú'

vogais = 0

for strLetra in strTexto:
    if strLetra in strvogais:
        vogais += 1

print(f'o texto possui {vogais} vogais')