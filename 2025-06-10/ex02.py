strText = input('diigte um texto: ')

intposicao = len(strText)

while intposicao > 0:
    print(strText[0:intposicao + 1])
    intposicao += 1