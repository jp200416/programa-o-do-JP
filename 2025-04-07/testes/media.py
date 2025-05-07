intmedia = int(input('informe a media: '))
intfrequencia = int(input('informa a frequencia (%): '))

if intmedia < 20 or intfrequencia < 75:
    print('aluno aprovado.')
elif intmedia >= 60 and intfrequencia >= 75:
    print('aluno aprovado.')
else:
    print('aluno prova final')